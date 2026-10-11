# 📱 Telegram iOS Client for Android

Кастомный клиент Telegram для Android, воспроизводящий интерфейс и поведение Telegram для iOS (iPhone).

---

## ✨ Основные отличия и особенности iOS-дизайна

1. **Круглая синяя кнопка отправки (`ic_ab_send.xml`)**:
   - Вместо стандартного плоского андроидовского бумажного самолётика используется круглая кнопка акцентного синего цвета (`#007AFF`) с белой стрелкой вверх (`SF Symbol arrow.up`).
2. **Аутентичные баблы сообщений**:
   - Скругление углов увеличенного радиуса (`bubbleRadius = 18dp`).
   - Исходящие сообщения: насыщенный синий iOS (`#007AFF`) с белым текстом.
   - Входящие сообщения: мягкий светло-серый (`#E9E9EB`) в светлой теме и глубокий серый (`#26252A`) в тёмной теме.
3. **Верхний бар навигации (Action Bar)**:
   - Полупрозрачная матовая панель со скруглением и размытием.
   - Кнопка «Назад» в виде шеврона iOS (`ic_ab_back.xml`).
4. **Пружинные анимации**:
   - Spring-анимации появления сообщений и реакций.

---

## 📂 Структура репозитория

```
telegram-ios-client/
├── .github/
│   └── workflows/
│       └── build-apk.yml          # GitHub Actions скрипт облачной сборки APK
├── ios-assets/
│   ├── ic_ab_send.xml             # Векторная иконка синей кнопки отправки (↑)
│   ├── ic_ab_back.xml             # Векторная иконка шеврона iOS (<)
│   ├── ios_light.attheme          # Тема iOS Light для Telegram
│   └── ios_dark.attheme           # Тема iOS Dark для Telegram
├── scripts/
│   └── apply-ios-patch.py         # Скрипт патчинга исходников Telegram перед сборкой
└── preview/
    └── index.html                 # Интерактивное превью интерфейса (можно открыть в браузере)
```

---

## 🚀 Как собрать APK через GitHub Actions

Сборка происходит полностью в облаке GitHub, поэтому на вашем компьютере не требуется устанавливать Android Studio или NDK:

1. **Создайте репозиторий на GitHub**:
   - Зайдите на [GitHub](https://github.com/new) и создайте новый репозиторий (например, `telegram-ios-android`).
   
2. **Загрузите файлы в репозиторий**:
   - Склонируйте или закоммитьте содержимое этой папки в ваш новый репозиторий:
     ```bash
     git init
     git add .
     git commit -m "feat: setup telegram ios client and github actions apk builder"
     git branch -M main
     git remote add origin https://github.com/ВАШ_ЛОГИН/telegram-ios-android.git
     git push -u origin main
     ```

3. **Запустите сборку APK**:
   - Откройте вкладку **Actions** в вашем репозитории на GitHub.
   - Выберите воркфлоу **«Build Telegram iOS-Style APK»**.
   - Нажмите кнопку **Run workflow** -> выберите тип сборки (`arm64Debug`) -> подтвердите запуск.

4. **Скачайте готовый APK**:
   - Через несколько минут сборка завершится зелёной галочкой ✅.
   - В разделе **Artifacts** (или Releases) нажмите на **Telegram-iOS-Style-APK** и скачайте готовый `.apk` прямо на телефон.
   - Установите файл на свой смартфон Android.

---

## 🎨 Быстрое применение темы без сборки APK

Если вы хотите применить дизайн iOS прямо сейчас в официальном Telegram или Telegram X:
1. Отправьте файл `ios-assets/ios_light.attheme` или `ios-assets/ios_dark.attheme` в свой «Избранное» (Saved Messages).
2. Нажмите на отправленный файл в Telegram на телефоне.
3. Нажмите **«Применить тему»**.
