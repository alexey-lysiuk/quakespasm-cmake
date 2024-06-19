#!/usr/bin/env python3

import sys

f = open(sys.argv[1], 'rb')
content = f.read()

header = b'7z\xbc\xaf\x27\x1c'
pos7z = content.find(header, content.find(header) + 1)
assert pos7z != 0

f = open('vulkan-sdk.7z', 'wb')
f.write(content[pos7z:])

'''

VULKAN_SDK_VERSION=1.3.283.0
GLSLANG_VERSION=14.2.0

# === Linux ===
curl -JOL https://sdk.lunarg.com/sdk/download/$VULKAN_SDK_VERSION/linux/vulkansdk-linux-x86_64-$VULKAN_SDK_VERSION.tar.xz
EXE_DIR=$VULKAN_SDK_VERSION/x86_64/bin
tar --strip-components=3 -xf vulkansdk-linux-x86_64-$VULKAN_SDK_VERSION.tar.xz $EXE_DIR/glslang $EXE_DIR/glslangValidator $EXE_DIR/spirv-opt $EXE_DIR/spirv-remap
tar -cJf glslang-$GLSLANG_VERSION-Linux.tar.xz glslang glslangValidator spirv-opt spirv-remap
rm vulkansdk-linux-x86_64-$VULKAN_SDK_VERSION.tar.xz glslang glslangValidator spirv-opt spirv-remap

# === macOS ===
curl -JOL https://sdk.lunarg.com/sdk/download/$VULKAN_SDK_VERSION/mac/vulkansdk-macos-$VULKAN_SDK_VERSION.dmg
hdiutil attach vulkansdk-macos-$VULKAN_SDK_VERSION.dmg
./extract_vulkan-sdk_7z.py /Volumes/vulkansdk-macos-$VULKAN_SDK_VERSION/InstallVulkan.app/Contents/Resources/installer.dat
hdiutil detach /Volumes/vulkansdk-macos-$VULKAN_SDK_VERSION
./7zz e vulkan-sdk.7z macOS/bin/glslang macOS/bin/glslangValidator macOS/bin/spirv-opt macOS/bin/spirv-remap
tar -cJf glslang-$GLSLANG_VERSION-macOS.tar.xz glslang glslangValidator spirv-opt spirv-remap
rm vulkansdk-macos-$VULKAN_SDK_VERSION.dmg vulkan-sdk.7z glslang glslangValidator spirv-opt spirv-remap

# === Windows ===
curl -JOL https://sdk.lunarg.com/sdk/download/$VULKAN_SDK_VERSION/windows/VulkanSDK-$VULKAN_SDK_VERSION-Installer.exe
./extract_vulkan-sdk_7z.py VulkanSDK-$VULKAN_SDK_VERSION-Installer.exe
./7zz e vulkan-sdk.7z Bin/glslangValidator.exe Bin/spirv-opt.exe Bin/spirv-remap.exe
tar -cJf glslang-$GLSLANG_VERSION-Windows.tar.xz glslangValidator.exe spirv-opt.exe spirv-remap.exe
rm VulkanSDK-$VULKAN_SDK_VERSION-Installer.exe vulkan-sdk.7z glslangValidator.exe spirv-opt.exe spirv-remap.exe

'''
