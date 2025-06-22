cmake_minimum_required(VERSION 3.10)

if(QUAKE_TARGET)
	set(SRC "${CMAKE_SOURCE_DIR}/src/${QUAKE_TARGET}")
else()
	set(SRC "${CMAKE_SOURCE_DIR}")

	if(EXISTS "${SRC}/Quakespasm-Spiked.txt")
		set(QUAKE_TARGET quakespasm-spiked)
	elseif(EXISTS "${SRC}/Quake/vkquake.pak")
		set(QUAKE_TARGET vkquake)
	elseif(EXISTS "${SRC}/Quake/ironwail.pak")
		set(QUAKE_TARGET ironwail)
	elseif(EXISTS "${SRC}/Quakespasm.txt")
		set(QUAKE_TARGET quakespasm)
	endif()

	if(NOT QUAKE_TARGET)
		set(SRC_DEFAULT "${SRC}/src/quakespasm")

		if(EXISTS "${SRC_DEFAULT}")
			set(QUAKE_TARGET quakespasm)
			set(SRC "${SRC_DEFAULT}")
		endif()
	endif()
endif()

if(QUAKE_TARGET STREQUAL quakespasm)
	set(PROJECT_QUAKESPASM TRUE)
elseif(QUAKE_TARGET STREQUAL quakespasm-spiked)
	set(PROJECT_SPIKED TRUE)
elseif(QUAKE_TARGET STREQUAL vkquake)
	set(PROJECT_VKQUAKE TRUE)
elseif(QUAKE_TARGET STREQUAL ironwail)
	set(PROJECT_IRONWAIL TRUE)
else()
	message(FATAL_ERROR "Unknown target ${QUAKE_TARGET}")
endif()

project(${QUAKE_TARGET} LANGUAGES C)
message("Quake target is set to '${QUAKE_TARGET}'")

set(COMMON_SOURCES
	"${SRC}/Quake/anorms.h"
	"${SRC}/Quake/arch_def.h"
	"${SRC}/Quake/bgmusic.c"
	"${SRC}/Quake/bgmusic.h"
	"${SRC}/Quake/bspfile.h"
	"${SRC}/Quake/cd_null.c"
	"${SRC}/Quake/cdaudio.h"
	"${SRC}/Quake/cfgfile.c"
	"${SRC}/Quake/cfgfile.h"
	"${SRC}/Quake/chase.c"
	"${SRC}/Quake/cl_demo.c"
	"${SRC}/Quake/cl_input.c"
	"${SRC}/Quake/cl_main.c"
	"${SRC}/Quake/cl_parse.c"
	"${SRC}/Quake/cl_tent.c"
	"${SRC}/Quake/client.h"
	"${SRC}/Quake/cmd.c"
	"${SRC}/Quake/cmd.h"
	"${SRC}/Quake/common.c"
	"${SRC}/Quake/common.h"
	"${SRC}/Quake/console.c"
	"${SRC}/Quake/console.h"
	"${SRC}/Quake/crc.c"
	"${SRC}/Quake/crc.h"
	"${SRC}/Quake/cvar.c"
	"${SRC}/Quake/cvar.h"
	"${SRC}/Quake/draw.h"
	"${SRC}/Quake/filenames.h"
	"${SRC}/Quake/gl_draw.c"
	"${SRC}/Quake/gl_fog.c"
	"${SRC}/Quake/gl_mesh.c"
	"${SRC}/Quake/gl_model.c"
	"${SRC}/Quake/gl_model.h"
	"${SRC}/Quake/gl_refrag.c"
	"${SRC}/Quake/gl_rlight.c"
	"${SRC}/Quake/gl_rmain.c"
	"${SRC}/Quake/gl_rmisc.c"
	"${SRC}/Quake/gl_screen.c"
	"${SRC}/Quake/gl_sky.c"
	"${SRC}/Quake/gl_texmgr.c"
	"${SRC}/Quake/gl_texmgr.h"
	"${SRC}/Quake/gl_vidsdl.c"
	"${SRC}/Quake/gl_warp.c"
	"${SRC}/Quake/gl_warp_sin.h"
	"${SRC}/Quake/glquake.h"
	"${SRC}/Quake/host.c"
	"${SRC}/Quake/host_cmd.c"
	"${SRC}/Quake/image.c"
	"${SRC}/Quake/image.h"
	"${SRC}/Quake/in_sdl.c"
	"${SRC}/Quake/input.h"
	"${SRC}/Quake/keys.c"
	"${SRC}/Quake/keys.h"
	"${SRC}/Quake/lodepng.h"
	"${SRC}/Quake/main_sdl.c"
	"${SRC}/Quake/mathlib.c"
	"${SRC}/Quake/mathlib.h"
	"${SRC}/Quake/menu.c"
	"${SRC}/Quake/menu.h"
	"${SRC}/Quake/modelgen.h"
	"${SRC}/Quake/net.h"
	"${SRC}/Quake/net_defs.h"
	"${SRC}/Quake/net_dgrm.c"
	"${SRC}/Quake/net_dgrm.h"
	"${SRC}/Quake/net_loop.c"
	"${SRC}/Quake/net_loop.h"
	"${SRC}/Quake/net_main.c"
	"${SRC}/Quake/net_sys.h"
	"${SRC}/Quake/platform.h"
	"${SRC}/Quake/pr_cmds.c"
	"${SRC}/Quake/pr_comp.h"
	"${SRC}/Quake/pr_edict.c"
	"${SRC}/Quake/pr_exec.c"
	"${SRC}/Quake/progdefs.h"
	"${SRC}/Quake/progs.h"
	"${SRC}/Quake/protocol.h"
	"${SRC}/Quake/q_ctype.h"
	"${SRC}/Quake/q_sound.h"
	"${SRC}/Quake/q_stdinc.h"
	"${SRC}/Quake/qs_bmp.h"
	"${SRC}/Quake/quakedef.h"
	"${SRC}/Quake/r_alias.c"
	"${SRC}/Quake/r_brush.c"
	"${SRC}/Quake/r_part.c"
	"${SRC}/Quake/r_sprite.c"
	"${SRC}/Quake/r_world.c"
	"${SRC}/Quake/render.h"
	"${SRC}/Quake/resource.h"
	"${SRC}/Quake/sbar.c"
	"${SRC}/Quake/sbar.h"
	"${SRC}/Quake/screen.h"
	"${SRC}/Quake/server.h"
	"${SRC}/Quake/snd_codec.c"
	"${SRC}/Quake/snd_codec.h"
	"${SRC}/Quake/snd_codeci.h"
	"${SRC}/Quake/snd_dma.c"
	"${SRC}/Quake/snd_flac.c"
	"${SRC}/Quake/snd_flac.h"
	"${SRC}/Quake/snd_mem.c"
	"${SRC}/Quake/snd_mikmod.c"
	"${SRC}/Quake/snd_mikmod.h"
	"${SRC}/Quake/snd_modplug.c"
	"${SRC}/Quake/snd_modplug.h"
	"${SRC}/Quake/snd_mix.c"
	"${SRC}/Quake/snd_mp3.h"
	"${SRC}/Quake/snd_mp3tag.c"
	"${SRC}/Quake/snd_opus.c"
	"${SRC}/Quake/snd_opus.h"
	"${SRC}/Quake/snd_sdl.c"
	"${SRC}/Quake/snd_umx.c"
	"${SRC}/Quake/snd_umx.h"
	"${SRC}/Quake/snd_vorbis.c"
	"${SRC}/Quake/snd_vorbis.h"
	"${SRC}/Quake/snd_wave.c"
	"${SRC}/Quake/snd_wave.h"
	"${SRC}/Quake/snd_xmp.c"
	"${SRC}/Quake/snd_xmp.h"
	"${SRC}/Quake/spritegn.h"
	"${SRC}/Quake/stb_image_write.h"
	"${SRC}/Quake/strl_fn.h"
	"${SRC}/Quake/strlcat.c"
	"${SRC}/Quake/strlcpy.c"
	"${SRC}/Quake/sv_main.c"
	"${SRC}/Quake/sv_move.c"
	"${SRC}/Quake/sv_phys.c"
	"${SRC}/Quake/sv_user.c"
	"${SRC}/Quake/sys.h"
	"${SRC}/Quake/vid.h"
	"${SRC}/Quake/view.c"
	"${SRC}/Quake/view.h"
	"${SRC}/Quake/wad.c"
	"${SRC}/Quake/wad.h"
	"${SRC}/Quake/world.c"
	"${SRC}/Quake/world.h"
	"${SRC}/Quake/wsaerror.h"
)

set(MINIZ_SOURCES
	"${SRC}/Quake/miniz.c"
	"${SRC}/Quake/miniz.h"
)

set(NON_VKQUAKE_SOURCES
	"${SRC}/Quake/anorm_dots.h"
	"${SRC}/Quake/default_cfg.h"
	"${SRC}/Quake/zone.c"
	"${SRC}/Quake/zone.h"
)

set(SPIKED_SOURCES
	"${SRC}/Quake/mdfour.c"
	"${SRC}/Quake/pr_ext.c"
	"${SRC}/Quake/r_part_fte.c"
)

if(PROJECT_SPIKED)
	set(COMMON_SOURCES
		${COMMON_SOURCES}
		${SPIKED_SOURCES}
		${NON_VKQUAKE_SOURCES}
		"${SRC}/Quake/ice/ice_gnutls.c"
		"${SRC}/Quake/ice/ice_main.c"
		"${SRC}/Quake/ice/ice_mdns.c"
		"${SRC}/Quake/ice/ice_quake.c"
		"${SRC}/Quake/ice/ice_sctp.c"
		"${SRC}/Quake/ice/ice_socket.c"
		"${SRC}/Quake/ice/ice_stream.c"
		"${SRC}/Quake/ice/json.c"
		"${SRC}/Quake/ice/md5.c"
		"${SRC}/Quake/ice/sha1.c"
		"${SRC}/Quake/ice/sha2.c"
		"${SRC}/Quake/ice/ice_private.h"
		"${SRC}/Quake/ice/ice_quake.h"
		"${SRC}/Quake/fs_zip.c"
		"${SRC}/Quake/pmove.c"
		"${SRC}/Quake/pmove.h"
		"${SRC}/Quake/pmovetst.c"
		"${SRC}/Quake/snd_voip.c"
		"${SRC}/Quake/snd_voip.h"
	)
elseif(PROJECT_IRONWAIL)
	set(COMMON_SOURCES
		${COMMON_SOURCES}
		${MINIZ_SOURCES}
		${NON_VKQUAKE_SOURCES}
		"${SRC}/Quake/gl_shaders.c"
		"${SRC}/Quake/gl_shaders.h"
		"${SRC}/Quake/json.c"
		"${SRC}/Quake/jsmn.h"
		"${SRC}/Quake/json.h"
		"${SRC}/Quake/stb_image.h"
		"${SRC}/Quake/steam.c"
		"${SRC}/Quake/steam.h"
		"${SRC}/Quake/unicode_translit.h"
	)
elseif(PROJECT_VKQUAKE)
	set(COMMON_SOURCES
		${COMMON_SOURCES}
		${SPIKED_SOURCES}
		${MINIZ_SOURCES}
		"${SRC}/Quake/atomics.h"
		"${SRC}/Quake/embedded_pak.c"
		"${SRC}/Quake/gl_heap.c"
		"${SRC}/Quake/gl_heap.h"
		"${SRC}/Quake/hash_map.c"
		"${SRC}/Quake/hash_map.h"
		"${SRC}/Quake/mem.c"
		"${SRC}/Quake/mem.h"
		"${SRC}/Quake/palette.c"
		"${SRC}/Quake/palette.h"
		"${SRC}/Quake/sys_sdl.c"
		"${SRC}/Quake/tasks.c"
		"${SRC}/Quake/tasks.h"
		"${SRC}/Quake/quakever.h"
	)
else()
	set(COMMON_SOURCES
		${COMMON_SOURCES}
		${MINIZ_SOURCES}
		${NON_VKQUAKE_SOURCES}
	)
endif()

set(POSIX_SOURCES
	"${SRC}/Quake/net_bsd.c"
	"${SRC}/Quake/net_udp.c"
	"${SRC}/Quake/net_udp.h"
	"${SRC}/Quake/sys_sdl_unix.c"
)

set(LINUX_SOURCES
	"${SRC}/Quake/pl_linux.c"
)

set(MACOS_SOURCES
	"${SRC}/Quake/pl_osx.m"
)

if(PROJECT_QUAKESPASM OR PROJECT_SPIKED)
	set(MACOS_BUNDLE_SOURCES
		"${SRC}/MacOSX/AppController.h"
		"${SRC}/MacOSX/AppController.m"
		"${SRC}/MacOSX/QuakeArgument.h"
		"${SRC}/MacOSX/QuakeArgument.m"
		"${SRC}/MacOSX/QuakeArguments.h"
		"${SRC}/MacOSX/QuakeArguments.m"
		"${SRC}/MacOSX/ScreenInfo.h"
		"${SRC}/MacOSX/ScreenInfo.m"
		"${SRC}/MacOSX/SDLApplication.h"
		"${SRC}/MacOSX/SDLApplication.m"
		"${SRC}/MacOSX/SDLMain.h"
		"${SRC}/MacOSX/SDLMain.m"
	)

	set(MACOS_RESOURCES
		"${SRC}/MacOSX/English.lproj/InfoPlist.strings"
		"${SRC}/MacOSX/English.lproj/Launcher.nib"
		"${SRC}/MacOSX/Launcher-Info.plist"
		"${SRC}/MacOSX/QuakeSpasm.icns"
	)
endif()

set(WINDOWS_SOURCES
	"${SRC}/Quake/net_win.c"
	"${SRC}/Quake/net_wins.c"
	"${SRC}/Quake/net_wins.h"
	"${SRC}/Quake/net_wipx.c"
	"${SRC}/Quake/net_wipx.h"
	"${SRC}/Quake/pl_win.c"
	"${SRC}/Quake/sys_sdl_win.c"
)

set(OTHER_FILES
	"${SRC}/Quake/lodepng.c"
)

if(NOT PROJECT_IRONWAIL)
	set(OTHER_FILES
		${OTHER_FILES}
		"${SRC}/Quake/cd_sdl.c"
	)
endif()

if(PROJECT_VKQUAKE)
	set(WINDOWS_SOURCES
		${WINDOWS_SOURCES}
		"${SRC}/Windows/vkQuake.ico"
		"${SRC}/Windows/vkQuake.rc"
	)

	set(OTHER_FILES
		${OTHER_FILES}
		"${SRC}/Quake/mimalloc/prim/emscripten/prim.c"
		"${SRC}/Quake/mimalloc/prim/osx/alloc-override-zone.c"
		"${SRC}/Quake/mimalloc/prim/osx/prim.c"
		"${SRC}/Quake/mimalloc/prim/unix/prim.c"
		"${SRC}/Quake/mimalloc/prim/wasi/prim.c"
		"${SRC}/Quake/mimalloc/prim/windows/prim.c"
		"${SRC}/Quake/mimalloc/prim/windows/etw.h"
		"${SRC}/Quake/mimalloc/mimalloc/atomic.h"
		"${SRC}/Quake/mimalloc/mimalloc/internal.h"
		"${SRC}/Quake/mimalloc/mimalloc/prim.h"
		"${SRC}/Quake/mimalloc/mimalloc/track.h"
		"${SRC}/Quake/mimalloc/mimalloc/types.h"
		"${SRC}/Quake/mimalloc/prim/prim.c"
		"${SRC}/Quake/mimalloc/alloc-aligned.c"
		"${SRC}/Quake/mimalloc/alloc-override.c"
		"${SRC}/Quake/mimalloc/alloc-posix.c"
		"${SRC}/Quake/mimalloc/alloc.c"
		"${SRC}/Quake/mimalloc/arena.c"
		"${SRC}/Quake/mimalloc/bitmap.c"
		"${SRC}/Quake/mimalloc/free.c"
		"${SRC}/Quake/mimalloc/heap.c"
		"${SRC}/Quake/mimalloc/init.c"
		"${SRC}/Quake/mimalloc/libc.c"
		"${SRC}/Quake/mimalloc/options.c"
		"${SRC}/Quake/mimalloc/os.c"
		"${SRC}/Quake/mimalloc/page-queue.c"
		"${SRC}/Quake/mimalloc/page.c"
		"${SRC}/Quake/mimalloc/random.c"
		"${SRC}/Quake/mimalloc/segment-map.c"
		"${SRC}/Quake/mimalloc/segment.c"
		"${SRC}/Quake/mimalloc/static.c"
		"${SRC}/Quake/mimalloc/stats.c"
		"${SRC}/Quake/mimalloc/bitmap.h"
		"${SRC}/Quake/mimalloc/mimalloc-new-delete.h"
		"${SRC}/Quake/mimalloc/mimalloc-override.h"
		"${SRC}/Quake/mimalloc/mimalloc.h"
		"${SRC}/Windows/.clang-format"
		"${SRC}/.clang-format"
	)
else()
	set(WINDOWS_SOURCES
		${WINDOWS_SOURCES}
		"${SRC}/Windows/QuakeSpasm.ico"
		"${SRC}/Windows/QuakeSpasm.rc"
	)

	if(PROJECT_IRONWAIL AND MSVC)
		set(OTHER_FILES
			${OTHER_FILES}
			"${SRC}/Windows/VisualStudio/ironwail.natvis"
		)
	endif()
endif()

if(NOT CMAKE_BUILD_TYPE)
	set(CMAKE_BUILD_TYPE Release CACHE STRING "Choose the type of build, options are: Debug Release RelWithDebInfo MinSizeRel." FORCE)
endif()

if(APPLE AND (PROJECT_QUAKESPASM OR PROJECT_SPIKED))
	option(QUAKE_MACOS_BUNDLE "Create macOS application bundle" ON)
endif()

if(QUAKE_MACOS_BUNDLE)
	add_executable(${PROJECT_NAME} WIN32 MACOSX_BUNDLE)
else()
	add_executable(${PROJECT_NAME} WIN32)
endif()

if(PROJECT_VKQUAKE)
	set_property(TARGET ${PROJECT_NAME} PROPERTY C_STANDARD 11)
else()
	set_property(TARGET ${PROJECT_NAME} PROPERTY C_STANDARD 90)
endif()

target_compile_definitions(${PROJECT_NAME} PRIVATE
	USE_CODEC_UMX
	USE_CODEC_WAVE
)

if(MSVC)
	target_compile_definitions(${PROJECT_NAME} PRIVATE _CRT_SECURE_NO_WARNINGS)
	target_compile_options(${PROJECT_NAME} PRIVATE /MP /wd4996)
else()
	option(QUAKE_SEARCH_USERDIRS "Search user directories for data" OFF)

	if(QUAKE_SEARCH_USERDIRS)
		target_compile_definitions(${PROJECT_NAME} PRIVATE DO_USERDIRS)
	endif()
endif()

if(APPLE)
	if(NOT PROJECT_VKQUAKE)
		target_compile_definitions(${PROJECT_NAME} PRIVATE GL_SILENCE_DEPRECATION)
	endif()

	target_link_libraries(${PROJECT_NAME} PRIVATE
		"-framework AppKit"
		"-framework IOKit"
	)

	if(${CMAKE_GENERATOR} STREQUAL Xcode)
		target_compile_options(${PROJECT_NAME} PRIVATE -Wno-shorten-64-to-32)
	endif()

	set(PLATFORM_SOURCE
		${MACOS_SOURCES}
		${POSIX_SOURCES}
	)
	set(OTHER_FILES
		${LINUX_SOURCES}
		${WINDOWS_SOURCES}
		${OTHER_FILES}
	)

	if(QUAKE_MACOS_BUNDLE)
		set(PLATFORM_SOURCE
			${PLATFORM_SOURCE}
			${MACOS_BUNDLE_SOURCES}
			${MACOS_RESOURCES}
		)

		target_include_directories(${PROJECT_NAME} PRIVATE MacOSX)

		set_target_properties(${PROJECT_NAME} PROPERTIES
			MACOSX_BUNDLE_INFO_PLIST "${SRC}/MacOSX/Info.plist"
			XCODE_ATTRIBUTE_PRODUCT_BUNDLE_IDENTIFIER "net.sf.quakespasm.QuakeSpasm"
		)
		set_source_files_properties(${MACOS_RESOURCES} PROPERTIES
			MACOSX_PACKAGE_LOCATION Resources
		)
	else()
		if(PROJECT_QUAKESPASM OR PROJECT_SPIKED)
			set(OTHER_FILES
				${OTHER_FILES}
				${MACOS_BUNDLE_SOURCES}
				${MACOS_RESOURCES}
			)
		endif()

		if(NOT PROJECT_VKQUAKE)
			# Workaround missing main function
			set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -Wl,-alias -Wl,_SDL_main -Wl,_main")
		endif()
	endif()
elseif(WIN32)
	target_link_libraries(${PROJECT_NAME} PRIVATE Winmm Ws2_32)

	set(PLATFORM_SOURCE
		${WINDOWS_SOURCES}
	)
	set(OTHER_FILES
		${LINUX_SOURCES}
		${MACOS_SOURCES}
		${POSIX_SOURCES}
		${OTHER_FILES}
	)
else()
	target_link_libraries(${PROJECT_NAME} PRIVATE m)

	set(PLATFORM_SOURCE
		${LINUX_SOURCES}
		${POSIX_SOURCES}
	)
	set(OTHER_FILES
		${MACOS_SOURCES}
		${WINDOWS_SOURCES}
		${OTHER_FILES}
	)
endif()

target_sources(${PROJECT_NAME} PRIVATE
	${COMMON_SOURCES}
	${PLATFORM_SOURCE}
	${OTHER_FILES}
)

set_source_files_properties(${OTHER_FILES} PROPERTIES HEADER_FILE_ONLY TRUE)

# Required dependencies

include(FindPackageHandleStandardArgs)

find_path(SDL2_INCLUDE_DIR SDL.h PATH_SUFFIXES SDL2)
find_library(SDL2_LIBRARY SDL2)
find_package_handle_standard_args(SDL2 DEFAULT_MSG SDL2_LIBRARY SDL2_INCLUDE_DIR)

if(NOT SDL2_FOUND AND WIN32)
	message(STATUS "Using vendored SDL2 library")
	set(SDL2_FOUND TRUE)
	set(SDL2_DIR "${SRC}/Windows/SDL2")
	set(SDL2_INCLUDE_DIR "${SDL2_DIR}/include")
	set(SDL2_LIBRARY SDL2 SDL2main)

	if(CMAKE_SIZEOF_VOID_P EQUAL 8)
		target_link_directories(${PROJECT_NAME} PRIVATE "${SDL2_DIR}/lib64")
	else()
		target_link_directories(${PROJECT_NAME} PRIVATE "${SDL2_DIR}/lib")
	endif()
endif()

if(SDL2_FOUND)
	target_compile_definitions(${PROJECT_NAME} PRIVATE USE_SDL2)
	target_include_directories(${PROJECT_NAME} PRIVATE "${SDL2_INCLUDE_DIR}")
	target_link_libraries(${PROJECT_NAME} PRIVATE "${SDL2_LIBRARY}")
else()
	message(SEND_ERROR "Could NOT find SDL2")
endif()

if(PROJECT_VKQUAKE)
	find_package(Vulkan)

	if(NOT Vulkan_FOUND AND WIN32)
		message(STATUS "Using vendored Vulkan library")
		set(Vulkan_FOUND TRUE)
		set(VULKAN_DIR "${SRC}/Windows/misc")
		set(Vulkan_INCLUDE_DIR "${VULKAN_DIR}/include")
		set(Vulkan_LIBRARY vulkan-1)

		if(CMAKE_SIZEOF_VOID_P EQUAL 8)
			target_link_directories(${PROJECT_NAME} PRIVATE "${VULKAN_DIR}/x64")
		else()
			target_link_directories(${PROJECT_NAME} PRIVATE "${VULKAN_DIR}/x86")
		endif()
	endif()

	if(Vulkan_FOUND)
		target_include_directories(${PROJECT_NAME} PRIVATE "${Vulkan_INCLUDE_DIR}")
		target_link_libraries(${PROJECT_NAME} PRIVATE "${Vulkan_LIBRARY}")
	else()
		message(SEND_ERROR "Could NOT find Vulkan")
	endif()

	function(find_vulkan_tool TOOL_VARIABLE TOOL_EXECUTABLE)
		find_program(${TOOL_VARIABLE} ${TOOL_EXECUTABLE})
		if(NOT ${TOOL_VARIABLE})
			message(SEND_ERROR "Could NOT find ${TOOL_EXECUTABLE} executable")
		endif()
	endfunction()

	find_vulkan_tool(GLSLANG_VALIDATOR_EXECUTABLE "glslangValidator")
	find_vulkan_tool(SPIRV_OPT_EXECUTABLE "spirv-opt")
	find_vulkan_tool(SPIRV_REMAP_EXECUTABLE "spirv-remap")

	set(VKQUAKE_SHADERS_DIR "${SRC}/Shaders")
	set(VKQUAKE_SHADERS
		alias.frag
		alias.vert
		alias_alphatest.frag
		basic.frag
		basic.vert
		basic_alphatest.frag
		basic_notex.frag
		cs_tex_warp.comp
		indirect.comp
		indirect_clear.comp
		md5.vert
		postprocess.frag
		postprocess.vert
		screen_effects_10bit.comp
		screen_effects_10bit_scale.comp
		screen_effects_10bit_scale_sops.comp
		screen_effects_8bit.comp
		screen_effects_8bit_scale.comp
		screen_effects_8bit_scale_sops.comp
		showtris.frag
		showtris.vert
		sky_box.frag
		sky_cube.frag
		sky_cube.vert
		sky_layer.frag
		sky_layer.vert
		update_lightmap_10bit.comp
		update_lightmap_10bit_rt.comp
		update_lightmap_8bit.comp
		update_lightmap_8bit_rt.comp
		world.frag
		world.vert
		ray_debug.comp
	)

	foreach(SHADER ${VKQUAKE_SHADERS})
		if(SHADER MATCHES ".+sops.+")
			set(VULKAN_TARGET_ENV "--target-env" "vulkan1.1")
		else()
			set(VULKAN_TARGET_ENV "")
		endif()

		string(REPLACE . _ SHADER_NAME ${SHADER})
		set(SHADER_SPV ${SHADER_NAME}.spv)
		set(SHADER_DEP ${SHADER_NAME}.dep)
		set(SHADER_C ${SHADER_NAME}.c)

		# TODO: glslangValidator debug flags
		add_custom_command(OUTPUT ${SHADER_C}
			COMMAND "${GLSLANG_VALIDATOR_EXECUTABLE}" -V ${VULKAN_TARGET_ENV} -o ${SHADER_SPV} "${VKQUAKE_SHADERS_DIR}/${SHADER}" --depfile ${SHADER_DEP}
			COMMAND "${SPIRV_OPT_EXECUTABLE}" -Os ${SHADER_SPV} -o ${SHADER_SPV}
			COMMAND "${SPIRV_REMAP_EXECUTABLE}" -s -o . -i ${SHADER_SPV}
			COMMAND "${CMAKE_COMMAND}" -P "${CMAKE_SOURCE_DIR}/bin2c.cmake" -- ${SHADER_SPV} ${SHADER_NAME}_spv ${SHADER_C}
			MAIN_DEPENDENCY "${VKQUAKE_SHADERS_DIR}/${SHADER}"
			DEPFILE ${SHADER_DEP}
		)

		target_sources(${PROJECT_NAME} PRIVATE ${SHADER_C})
		set_source_files_properties(${SHADER_C} PROPERTIES GENERATED YES)
	endforeach()

	source_group("Shader Files" REGULAR_EXPRESSION "^${VKQUAKE_SHADERS_DIR}/.+")

	find_package(Threads REQUIRED)
	target_link_libraries(${PROJECT_NAME} PRIVATE Threads::Threads)
	target_include_directories(${PROJECT_NAME} PRIVATE "${SRC}/Quake/mimalloc")
else()
	set(OpenGL_GL_PREFERENCE GLVND)
	find_package(OpenGL REQUIRED)
	target_include_directories(${PROJECT_NAME} PRIVATE "${OPENGL_INCLUDE_DIR}")
	target_link_libraries(${PROJECT_NAME} PRIVATE "${OPENGL_LIBRARY}")
endif()

# Optional dependencies

function(FIND_CODEC)
	cmake_parse_arguments(FIND_CODEC "" "NAME;HEADER;DEFINE" "PATH_SUFFIXES;LIBRARIES;SOURCES" ${ARGN})

	set(CODEC ${FIND_CODEC_NAME})
	find_path(${CODEC}_INCLUDE_DIR ${FIND_CODEC_HEADER} PATH_SUFFIXES ${FIND_CODEC_PATH_SUFFIXES})

	foreach(LIB IN LISTS FIND_CODEC_LIBRARIES)
		find_library(${LIB}_PATH ${LIB})
		list(APPEND ${CODEC}_LIBRARY "${${LIB}_PATH}")
	endforeach()

	include(FindPackageHandleStandardArgs)
	find_package_handle_standard_args(${CODEC} DEFAULT_MSG ${CODEC}_LIBRARY ${CODEC}_INCLUDE_DIR)

	if(NOT ${CODEC}_FOUND AND WIN32)
		message(STATUS "Using vendored ${CODEC} library")
		set(${CODEC}_FOUND TRUE)
		set(CODECS_DIR "${SRC}/Windows/codecs")
		set(${CODEC}_INCLUDE_DIR "${CODECS_DIR}/include")
		set(${CODEC}_LIBRARY "")

		foreach(LIB IN LISTS FIND_CODEC_LIBRARIES)
			list(APPEND ${CODEC}_LIBRARY "lib${LIB}")
		endforeach()

		if(CMAKE_SIZEOF_VOID_P EQUAL 8)
			target_link_directories(${PROJECT_NAME} PRIVATE "${CODECS_DIR}/x64")
		else()
			target_link_directories(${PROJECT_NAME} PRIVATE "${CODECS_DIR}/x86")
		endif()
	endif()

	if(${CODEC}_FOUND)
		set(${CODEC}_FOUND TRUE PARENT_SCOPE)
		target_sources(${PROJECT_NAME} PRIVATE "${FIND_CODEC_SOURCES}")
		target_compile_definitions(${PROJECT_NAME} PRIVATE ${FIND_CODEC_DEFINE})
		target_include_directories(${PROJECT_NAME} PRIVATE "${${CODEC}_INCLUDE_DIR}")
		target_link_libraries(${PROJECT_NAME} PRIVATE "${${CODEC}_LIBRARY}")
	endif()
endfunction()

find_codec(NAME FLAC
	HEADER FLAC/stream_decoder.h
	LIBRARIES FLAC
	DEFINE USE_CODEC_FLAC
)

find_codec(NAME MPG123
	HEADER mpg123.h
	LIBRARIES mpg123
	DEFINE USE_CODEC_MP3
	SOURCES "${SRC}/Quake/snd_mpg123.c"
)

if(NOT MPG123_FOUND)
	find_codec(NAME MAD
		HEADER mad.h
		LIBRARIES mad
		DEFINE USE_CODEC_MP3
		SOURCES "${SRC}/Quake/snd_mp3.c"
	)
endif()

find_codec(NAME OPUS
	HEADER opusfile.h
	PATH_SUFFIXES opus
	LIBRARIES opus opusfile
	DEFINE USE_CODEC_OPUS
)

find_codec(NAME VORBIS
	HEADER vorbis/vorbisfile.h
	LIBRARIES vorbis vorbisfile
	DEFINE USE_CODEC_VORBIS
)

find_codec(NAME XMP
	HEADER xmp.h
	LIBRARIES xmp
	DEFINE USE_CODEC_XMP
)

if(NOT XMP_FOUND)
	find_codec(NAME MIKMOD
		HEADER mikmod.h
		LIBRARIES mikmod
		DEFINE USE_CODEC_MIKMOD
	)

	if(NOT MIKMOD_FOUND)
		find_codec(NAME MODPLUG
			HEADER libmodplug/modplug.h
			LIBRARIES modplug
			DEFINE USE_CODEC_MODPLUG
		)
	endif()
endif()

if(PROJECT_SPIKED)
	find_package(ZLIB)
	if(ZLIB_FOUND)
		target_compile_definitions(${PROJECT_NAME} PRIVATE USE_ZLIB)
		target_include_directories(${PROJECT_NAME} PRIVATE "${ZLIB_INCLUDE_DIR}")
		target_link_libraries(${PROJECT_NAME} PRIVATE "${ZLIB_LIBRARY}")
	endif()

	find_package(GnuTLS)
	if(GNUTLS_FOUND)
		target_compile_definitions(${PROJECT_NAME} PRIVATE USE_GNUTLS)
		target_include_directories(${PROJECT_NAME} PRIVATE "${GNUTLS_INCLUDE_DIR}")
		target_link_libraries(${PROJECT_NAME} PRIVATE "${GNUTLS_LIBRARY}")

		if(APPLE)
			# macOS does not have this flag defined
			target_compile_definitions(${PROJECT_NAME} PRIVATE SOCK_CLOEXEC=0)
		endif()
	endif()

	target_link_libraries(${PROJECT_NAME} PRIVATE ${CMAKE_DL_LIBS})
elseif(PROJECT_VKQUAKE)
	include(CheckSymbolExists)
	set(CMAKE_REQUIRED_DEFINITIONS_PREV ${CMAKE_REQUIRED_DEFINITIONS})
	set(CMAKE_REQUIRED_DEFINITIONS ${CMAKE_REQUIRED_DEFINITIONS} -D_GNU_SOURCE)
	check_symbol_exists(CPU_ZERO "sched.h" HAVE_CPU_ZERO)
	set(CMAKE_REQUIRED_DEFINITIONS ${CMAKE_REQUIRED_DEFINITIONS_PREV})

	if (HAVE_CPU_ZERO)
		target_compile_definitions(${PROJECT_NAME} PRIVATE _GNU_SOURCE)
	else()
		message(WARNING "sched.h not found, disabling task affinity support")
		target_compile_definitions(${PROJECT_NAME} PRIVATE TASK_AFFINITY_NOT_AVAILABLE)
	endif()
elseif(PROJECT_IRONWAIL)
	find_package(CURL)

	if(NOT CURL_FOUND AND WIN32)
		set(CURL_FOUND TRUE)
		set(CURL_DIR "${SRC}/Windows/curl")
		set(CURL_INCLUDE_DIRS "${CURL_DIR}/include")
		set(CURL_LIB_DIRS "${CURL_DIR}/lib")
		set(CURL_LIBRARIES libcurl)

		if(CMAKE_SIZEOF_VOID_P EQUAL 8)
			target_link_directories(${PROJECT_NAME} PRIVATE "${CURL_LIB_DIRS}/x64")
		else()
			target_link_directories(${PROJECT_NAME} PRIVATE "${CURL_LIB_DIRS}/x86")
		endif()
	endif()

	if(CURL_FOUND)
		target_include_directories(${PROJECT_NAME} PRIVATE "${CURL_INCLUDE_DIRS}")
		target_link_libraries(${PROJECT_NAME} PRIVATE "${CURL_LIBRARIES}")
	else()
		target_compile_definitions(${PROJECT_NAME} PRIVATE WITHOUT_CURL)
	endif()
endif()

if(NOT PROJECT_VKQUAKE)
	if(PROJECT_IRONWAIL)
		set(ENGINE_PAK_FILE ironwail.pak)
	else()
		set(ENGINE_PAK_FILE quakespasm.pak)
	endif()

	add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD COMMAND
		${CMAKE_COMMAND} -E copy_if_different
		"${SRC}/Quake/${ENGINE_PAK_FILE}"
		"$<TARGET_FILE_DIR:${PROJECT_NAME}>"
	)
endif()
