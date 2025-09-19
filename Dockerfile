FROM kivy-final-builder:latest

# Настраиваем Buildozer для использования существующих SDK/NDK
RUN mkdir -p /root/.buildozer/android/platform && \
    ln -sf /opt/android-sdk /root/.buildozer/android/platform/android-sdk && \
    ln -sf /opt/android-sdk/ndk/25.2.9519653 /root/.buildozer/android/platform/android-ndk

WORKDIR /app
