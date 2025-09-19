#!/bin/bash
# Настраиваем Buildozer чтобы использовал существующие SDK/NDK

# Создаем симлинки для Buildozer
mkdir -p /root/.buildozer/android/platform/android-sdk
ln -sf /opt/android-sdk /root/.buildozer/android/platform/android-sdk/android-sdk-25.2.9519653

# Создаем необходимые папки
mkdir -p /root/.buildozer/android/platform/android-ndk
ln -sf /opt/android-sdk/ndk/25.2.9519653 /root/.buildozer/android/platform/android-ndk/android-ndk-r25b

# Копируем настройки
cp -r /opt/android-sdk /root/.buildozer/android/platform/

echo "Настройка завершена"
