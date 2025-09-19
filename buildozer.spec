[app]

# (str) Title of your application
title = My Kivy App

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#

#
# author = © Copyright Info

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for new android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
#presplash.color = #FFFFFF

# (list) Permissions
#android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
#android.api = 33

# (int) Minimum API your APK will support.
#android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25.2.9519653

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
#android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
android.ndk_path = /opt/android-sdk/ndk/25.2.9519653

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
android.sdk_path = /opt/android-sdk

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you do not want to wait for it.
android.skip_update = True

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be shown the license when first running
# buildozer.
#android.accept_sdk_license = False

# (str) Android build tools version to use
android.build_tools_version = 33.0.0

# (str) The main activitiy of your application
#android.entrypoint = org.test.myapp

# (list) Pattern to whitelist for the whole project
#android.whitelist =

# (str) Path to a custom whitelist file
#android.whitelist_src =

# (str) Path to a custom blacklist file
#android.blacklist_src =

# (list) List of Java .jar files to add to the libs so that gradle can compile them.
#android.add_jars = foo.jar,bar.jar

# (list) List of Java files to add to the android project (can be java or aapted resources)
#android.add_src =

# (list) Android AAR archives to add
#android.add_aars =

# (list) Gradle dependencies to add
#android.gradle_dependencies =

# (list) add java compile options
# this can for example be necessary when importing certain java libraries using the 'android.gradle_dependencies' option
# see https://developer.android.com/studio/write/java8-support for further information
# android.add_compile_options = -source 1.8 -target 1.8

# (list) Gradle repositories to add {can be necessary for some android.gradle_dependencies}
# please enclose in double quotes 
# e.g. android.add_gradle_repositories = "maven { url 'https://kotlin.bintray.com/ktor' }"
#android.add_gradle_repositories =

# (list) packaging options to add 
# see https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.PackagingOptions.html
# can be necessary to conflict between gradle dependencies
# options: exclude, merge, pickFirst
#android.add_packaging_options = 

# (list) Java classes to add as activities to the manifest.
#android.add_activities = com.example.ExampleActivity

# (str) OUYA Console category.
# see: https://devs.ouya.tv/docs/ouya-consoles-categories
#android.ouya.category = GAME

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
#android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file to include as an intent filters in the main activity
#android.manifest.intent_filters = 

# (str) launchMode to set for the main activity
#android.manifest.launch_mode = 

# (list) Android additional libraries to copy into libs/armeabi
#android.add_libs_armeabi = libs/android/*.so
#android.add_libs_armeabi_v7a = libs/android-v7/*.so
#android.add_libs_arm64_v8a = libs/android-v8/*.so
#android.add_libs_x86 = libs/android-x86/*.so
#android.add_libs_x86_64 = libs/android-x64/*.so

# (bool) Indicate whether the screen should stay on
# Don't forget to add the WAKE_LOCK permission if you set this to True
#android.wakelock = False

# (list) Android application meta-data to set (key=value format)
#android.meta_data =

# (list) Android library project to add (will be added in the project.properties automatically.)
#android.library_references =

# (list) Android shared libraries which will be added to AndroidManifest.xml as <uses-library> items
#android.uses_library =

# (str) Android logcat filters to use
#android.logcat_filters = *:S

# (bool) Android logcat only display log for activity's PID
# android.logcat_pid_only = False

# (str) Android additional adb arguments
#android.adb_args = -H host.docker.internal

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.arch = arm64-v8a, armeabi-v7a

# (int) overrides automatic versionCode computation (used in build.gradle)
# this is not the same as app version and should only be edited if you know what you're doing
# android.numeric_version = 1

# (str) XAuthorize: authorization type (password, none)
# xauthorize.type = password

# (str) XAuthorize: username
# xauthorize.username =

# (str) XAuthorize: password
# xauthorize.password =

# (bool) XAuthorize: allow root user access
# xauthorize.root = False

# (bool) XAuthorize: allow non-root user access
# xauthorize.non_root = False

# (bool) XAuthorize: allow non-network local connections (no-ssh)
# xauthorize.local = False

# (bool) XAuthorize: screen saver gets launched at app start
# xauthorize.screensaver = False

# (bool) XAuthorize: allow other users (not the one running the X server) to access the display
# xauthorize.other_users = False

# (bool) XAuthorize: disable access control temporarily (enables all connections) 
# xauthorize.disable_access_control = False

# (bool) XAuthorize: enable TCP connections (no-ssh)
# xauthorize.tcp = False

# (bool) XAuthorize: allow connections from any host (no-ssh)
# xauthorize.any_host = False

# (bool) XAuthorize: enable XDMCP (X Display Manager Control Protocol) 
# xauthorize.xdmcp = False

# (bool) XAuthorize: X server to listen to TCP (no-ssh)
# xauthorize.listen_tcp = False

# (bool) XAuthorize: X server to listen to UNIX domain socket (no-ssh)
# xauthorize.listen_unix = False

# (bool) Skip the version check of the Kivy iOS requirements
# ios.skip_kivy_requirements = False

# (bool) Skip the version check of the buildozer requirements
# skip_buildozer_version_check = False

# (bool) Use the buildozer --verbose option
# buildozer_verbose = False

# (bool) Use the buildozer --color option
# buildozer_color = True

# (bool) Use the buildozer --profiling option
# buildozer_profiling = False
