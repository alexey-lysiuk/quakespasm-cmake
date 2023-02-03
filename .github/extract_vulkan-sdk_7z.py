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

VULKAN_SDK_VERSION=1.3.239.0
GLSLANG_VERSION=12.0.0

# === Linux ===
curl -JOL https://sdk.lunarg.com/sdk/download/1.3.239.0/linux/vulkansdk-linux-x86_64-$VULKAN_SDK_VERSION.tar.gz
EXE_DIR=$VULKAN_SDK_VERSION/x86_64/bin
tar --strip-components=3 -xf vulkansdk-linux-x86_64-$VULKAN_SDK_VERSION.tar.gz $EXE_DIR/glslangValidator $EXE_DIR/spirv-opt $EXE_DIR/spirv-remap
tar -cJf glslang-12.0.0-Linux.tar.xz glslangValidator spirv-opt spirv-remap
rm glslangValidator spirv-opt spirv-remap

# === macOS ===
curl -JOL https://sdk.lunarg.com/sdk/download/1.3.239.0/mac/vulkansdk-macos-$VULKAN_SDK_VERSION.dmg
hdiutil attach vulkansdk-macos-$VULKAN_SDK_VERSION.dmg
./extract_vulkan-sdk_7z.py /Volumes/vulkansdk-macos-$VULKAN_SDK_VERSION/InstallVulkan.app/Contents/Resources/installer.dat
./7za e vulkan-sdk.7z macOS/bin/glslangValidator macOS/bin/spirv-opt macOS/bin/spirv-remap
for exe in glslangValidator spirv-opt spirv-remap; do lipo $exe -thin x86_64 -output $exe; done
tar -cJf glslang-12.0.0-macOS.tar.xz glslangValidator spirv-opt spirv-remap
rm vulkan-sdk.7z glslangValidator spirv-opt spirv-remap

# === Windows ===
curl -JOL https://sdk.lunarg.com/sdk/download/1.3.239.0/windows/VulkanSDK-$VULKAN_SDK_VERSION-Installer.exe
./extract_vulkan-sdk_7z.py VulkanSDK-1.3.239.0-Installer.exe
./7za e vulkan-sdk.7z Bin/glslangValidator.exe Bin/spirv-opt.exe Bin/spirv-remap.exe
tar -cJf glslang-12.0.0-Windows.tar.xz glslangValidator.exe spirv-opt.exe spirv-remap.exe
rm vulkan-sdk.7z glslangValidator.exe spirv-opt.exe spirv-remap.exe

'''
