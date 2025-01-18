# Running headless Android Emulator



1. Create an AVD

   ```bash
   echo no | $ANDROID_SDK_ROOT/cmdline-tools/latest/bin/avdmanager create avd --force -n test --abi 'google_apis_playstore/x86' --package 'system-images;android-28;google_apis_playstore;x86' --device 'Nexus 6'
   ```

2. Boot the Emulator

   ```bash
   $ANDROID_SDK_ROOT/emulator/emulator -avd test -no-window -gpu swiftshader_indirect -no-snapshot -noaudio -no-boot-anim
   ```
   You will see an output similar like this

   ```
   emulator: Android emulator version 30.7.5.0 (build_id 7491168) (CL:N/A)
   handleCpuAcceleration: feature check for hvf
   emulator: feeding guest with passive gps data, in headless mode
   cannot add library /Users/cs/Library/Android/sdk/emulator/qemu/darwin-x86_64/lib64/vulkan/libvulkan.dylib: failed
   added library /Users/cs/Library/Android/sdk/emulator/lib64/vulkan/libvulkan.dylib
   emulator: INFO: GrpcServices.cpp:315: Started GRPC server at 127.0.0.1:8554, security: Local
   emulator: INFO: EmulatorAdvertisement.cpp:93: Advertising in: /Users/cs/Library/Caches/TemporaryItems/avd/running/pid_60753.ini
   emulator: Cold boot: requested by the user
   Your emulator is out of date, please update by launching Android Studio:
    - Start Android Studio
    - Select menu "Tools > Android > SDK Manager"
    - Click "SDK Tools" tab
    - Check "Android Emulator" checkbox
    - Click "OK"

   emulator: INFO: boot completed
   emulator: INFO: boot time 26292 ms
   emulator: Increasing screen off timeout, logcat buffer size to 2M.
   emulator: Revoking microphone permissions for Google App.

   ```

   If you already have an AVD setup, use `-list-avds` flag to list available avds and provide that in argument to `-avd` above.
   ```
   $ANDROID_SDK_ROOT/emulator/emulator -list-avds
   ```

3. Verify emulator is successfully booted (required in case if you run the above command in background)

   ```bash
   $ANDROID_SDK_ROOT/platform-tools/adb shell getprop sys.boot_completed
   ```
   This will return `1` if emulator is running.


> Note: `ANDROID_SDK_ROOT` points to `/Users/user/Library/Android/sdk/`

## Runninng Emulator inside Github Actions

```yaml
name: Emulator Test
on:
  push:
  workflow_dispatch:

jobs:
  integration_test:
    runs-on: ubuntu-latest
    name: "Android"
    steps:
      - uses: actions/checkout@v2
      - name: "Check android emulator"
        run: |
          $ANDROID_SDK_ROOT/cmdline-tools/latest/bin/sdkmanager --install 'build-tools;31.0.0' platform-tools 'platforms;android-29' > /dev/null
          $ANDROID_SDK_ROOT/cmdline-tools/latest/bin/sdkmanager --install emulator --channel=0 > /dev/null
          $ANDROID_SDK_ROOT/cmdline-tools/latest/bin/sdkmanager --install 'system-images;android-29;default;x86_64' --channel=0 > /dev/null
          echo no | $ANDROID_SDK_ROOT/cmdline-tools/latest/bin/avdmanager create avd --force -n test --abi 'default/x86_64' --package 'system-images;android-29;default;x86_64' --device 'Nexus 6'
```

## Emulator CLI Tips

1. You can also record the session/screen using the `-record-session` flag. Specially useful when running emulator in headless mode
   ```bash
   $ANDROID_SDK_ROOT/emulator/emulator -avd Pixel_2_API_27 -no-window -gpu swiftshader_indirect -no-snapshot -record-session filename.webm,7s
   ```
