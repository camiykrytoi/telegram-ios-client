#!/usr/bin/env python3
import sys
import os
import json
import subprocess
import urllib.request
import urllib.error

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

TOKEN = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("GITHUB_TOKEN", "")
if not TOKEN:
    print("[ERROR] Token must be provided as argument or GITHUB_TOKEN environment variable")
    sys.exit(1)

REPO_NAME = "telegram-ios-client"

headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "Antigravity-Agent"
}

print("1. Verifying GitHub Token...")
req = urllib.request.Request("https://api.github.com/user", headers=headers)
try:
    with urllib.request.urlopen(req) as resp:
        user_data = json.loads(resp.read().decode())
        username = user_data["login"]
        print(f"[OK] Authenticated as: {username}")
except urllib.error.HTTPError as e:
    print(f"[ERROR] Token authentication failed: {e.code} - {e.read().decode()}")
    sys.exit(1)

print("2. Configuring git and pushing clean commit...")
def run_cmd(cmd):
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding='utf-8', errors='replace')
    if res.returncode != 0 and "already exists" not in res.stderr:
        print(f"Command: {cmd}")
        if res.stdout:
            print(f"Stdout: {res.stdout.strip()}")
        if res.stderr:
            print(f"Stderr: {res.stderr.strip()}")
    return res

run_cmd('git config user.name "camiykrytoi"')
run_cmd('git config user.email "camiykrytoi@users.noreply.github.com"')
run_cmd('git checkout --orphan temp_branch')
run_cmd('git add -A')
run_cmd('git commit -m "feat: Telegram iOS Client for Android with native iOS UI and GitHub Actions"')
run_cmd('git branch -D main')
run_cmd('git branch -m main')

remote_url = f"https://camiykrytoi:{TOKEN}@github.com/camiykrytoi/{REPO_NAME}.git"
run_cmd('git remote remove origin')
run_cmd(f'git remote add origin {remote_url}')
push_res = run_cmd('git push -u origin main --force')

if push_res.returncode == 0:
    print(f"[SUCCESS] Code successfully pushed to https://github.com/camiykrytoi/{REPO_NAME}")
else:
    print(f"[PUSH ERROR] Stderr: {push_res.stderr}")
    sys.exit(1)

print("3. Triggering GitHub Actions APK build workflow...")
dispatch_req = urllib.request.Request(
    f"https://api.github.com/repos/{username}/{REPO_NAME}/actions/workflows/build-apk.yml/dispatches",
    data=json.dumps({"ref": "main"}).encode(),
    headers=headers,
    method="POST"
)
try:
    with urllib.request.urlopen(dispatch_req) as resp:
        print("[SUCCESS] GitHub Actions workflow triggered!")
except urllib.error.HTTPError as e:
    print(f"[NOTE] Actions dispatch note: {e.code} - {e.read().decode()}")

print("4. Checking active workflow runs...")
import time
time.sleep(3)
runs_req = urllib.request.Request(
    f"https://api.github.com/repos/{username}/{REPO_NAME}/actions/runs",
    headers=headers
)
try:
    with urllib.request.urlopen(runs_req) as resp:
        runs_data = json.loads(resp.read().decode())
        runs = runs_data.get("workflow_runs", [])
        if runs:
            latest = runs[0]
            print(f"🚀 Active Run ID: {latest['id']}")
            print(f"🔗 Run URL: {latest['html_url']}")
            print(f"Status: {latest['status']}")
        else:
            print(f"Workflow runs link: https://github.com/{username}/{REPO_NAME}/actions")
except urllib.error.HTTPError as e:
    print(f"Runs check note: {e.code}")

print("\n✨ ALL DONE! Build is active in GitHub Actions.")
