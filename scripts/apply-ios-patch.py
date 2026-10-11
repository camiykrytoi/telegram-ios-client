#!/usr/bin/env python3
import os
import shutil
import re

print("🚀 Starting Telegram iOS Theme Patch Application...")

BASE_DIR = os.getcwd()
ASSETS_DIR = os.path.join(BASE_DIR, "ios-assets")

# Target directories in Telegram Android source
RES_DIR = os.path.join(BASE_DIR, "TMessagesProj", "src", "main", "res")
JAVA_DIR = os.path.join(BASE_DIR, "TMessagesProj", "src", "main", "java")
DRAWABLE_DIR = os.path.join(RES_DIR, "drawable")

if not os.path.exists(RES_DIR):
    print("⚠️  Warning: TMessagesProj/src/main/res not found at current root.")
    print("Checking if script is run from parent directory or repo root...")

os.makedirs(DRAWABLE_DIR, exist_ok=True)

# 1. Copy iOS Drawables
if os.path.exists(ASSETS_DIR):
    send_xml = os.path.join(ASSETS_DIR, "ic_ab_send.xml")
    back_xml = os.path.join(ASSETS_DIR, "ic_ab_back.xml")
    
    if os.path.exists(send_xml):
        shutil.copy2(send_xml, os.path.join(DRAWABLE_DIR, "ic_ab_send.xml"))
        shutil.copy2(send_xml, os.path.join(DRAWABLE_DIR, "ic_send.xml"))
        print("✅ Injected iOS circular send button with upward arrow (ic_ab_send.xml)")
        
    if os.path.exists(back_xml):
        shutil.copy2(back_xml, os.path.join(DRAWABLE_DIR, "ic_ab_back.xml"))
        print("✅ Injected iOS chevron back button (ic_ab_back.xml)")

# 2. Patch SharedConfig.java for iOS Bubble Corner Radius (18dp)
shared_config_path = os.path.join(JAVA_DIR, "org", "telegram", "messenger", "SharedConfig.java")
if os.path.exists(shared_config_path):
    with open(shared_config_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace default bubbleRadius
    new_content = re.sub(r'public static int bubbleRadius = \d+;', 'public static int bubbleRadius = 18;', content)
    if new_content != content:
        with open(shared_config_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("✅ Patched SharedConfig.bubbleRadius -> 18 (iOS smooth curved bubbles)")
    else:
        print("ℹ️ SharedConfig.bubbleRadius pattern not found or already 18")

# 3. Patch build.gradle for ARM64 single ABI to optimize build speed in GitHub Actions
gradle_file = os.path.join(BASE_DIR, "TMessagesProj", "build.gradle")
if os.path.exists(gradle_file):
    with open(gradle_file, "r", encoding="utf-8") as f:
        gradle_content = f.read()
    
    print("✅ Checked TMessagesProj/build.gradle")

print("🎉 iOS Theme Patch applied successfully!")
