# FindVulkan module requires CMake 3.7 otherwise 3.0 should be enough
cmake_minimum_required(VERSION 3.7)

# TODO: add support for target detection if CMake files are in target's directory
if(NOT QUAKE_TARGET)
	message(FATAL_ERROR "QUAKE_TARGET variable is not set")
endif()

if(QUAKE_TARGET STREQUAL quakespasm)
	set(PROJECT_QUAKESPASM TRUE)
	set(SRC "${CMAKE_SOURCE_DIR}/src/${QUAKE_TARGET}")
elseif(QUAKE_TARGET STREQUAL quakespasm-spiked)
	set(PROJECT_SPIKED TRUE)
	set(SRC "${CMAKE_SOURCE_DIR}/src/${QUAKE_TARGET}/quakespasm")
elseif(QUAKE_TARGET STREQUAL vkquake)
	set(PROJECT_VKQUAKE TRUE)
	set(SRC "${CMAKE_SOURCE_DIR}/src/${QUAKE_TARGET}")
else()
	message(FATAL_ERROR "Unknown target ${QUAKE_TARGET}")
endif()

project(${QUAKE_TARGET} LANGUAGES C)

list(APPEND CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake")

set(COMMON_SOURCES
	"${SRC}/Quake/anorm_dots.h"
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
	"${SRC}/Quake/zone.c"
	"${SRC}/Quake/zone.h"
)

set(QUAKESPASM_SOURCES
	"${SRC}/Quake/default_cfg.h"
	"${SRC}/Quake/miniz.c"
	"${SRC}/Quake/miniz.h"
)

if(PROJECT_SPIKED)
	set(COMMON_SOURCES
		${COMMON_SOURCES}
		"${SRC}/Quake/fs_zip.c"
		"${SRC}/Quake/mdfour.c"
		"${SRC}/Quake/pr_ext.c"
		"${SRC}/Quake/r_part_fte.c"
		"${SRC}/Quake/snd_voip.c"
		"${SRC}/Quake/snd_voip.h"
	)
elseif(PROJECT_VKQUAKE)
	set(COMMON_SOURCES
		${COMMON_SOURCES}
		${QUAKESPASM_SOURCES}
		"${SRC}/Quake/gl_heap.c"
		"${SRC}/Quake/gl_heap.h"
		"${SRC}/Quake/mdfour.c"
		"${SRC}/Quake/pr_ext.c"
		"${SRC}/Shaders/Compiled/alias_alphatest_frag.c"
		"${SRC}/Shaders/Compiled/alias_frag.c"
		"${SRC}/Shaders/Compiled/alias_vert.c"
		"${SRC}/Shaders/Compiled/basic_alphatest_frag.c"
		"${SRC}/Shaders/Compiled/basic_frag.c"
		"${SRC}/Shaders/Compiled/basic_notex_frag.c"
		"${SRC}/Shaders/Compiled/basic_vert.c"
		"${SRC}/Shaders/Compiled/cs_tex_warp_comp.c"
		"${SRC}/Shaders/Compiled/postprocess_frag.c"
		"${SRC}/Shaders/Compiled/postprocess_vert.c"
		"${SRC}/Shaders/Compiled/screen_effects_10bit_comp.c"
		"${SRC}/Shaders/Compiled/screen_effects_10bit_scale_comp.c"
		"${SRC}/Shaders/Compiled/screen_effects_10bit_scale_sops_comp.c"
		"${SRC}/Shaders/Compiled/screen_effects_8bit_comp.c"
		"${SRC}/Shaders/Compiled/screen_effects_8bit_scale_comp.c"
		"${SRC}/Shaders/Compiled/screen_effects_8bit_scale_sops_comp.c"
		"${SRC}/Shaders/Compiled/showtris_frag.c"
		"${SRC}/Shaders/Compiled/showtris_vert.c"
		"${SRC}/Shaders/Compiled/sky_box_frag.c"
		"${SRC}/Shaders/Compiled/sky_layer_frag.c"
		"${SRC}/Shaders/Compiled/sky_layer_vert.c"
		"${SRC}/Shaders/Compiled/world_frag.c"
		"${SRC}/Shaders/Compiled/world_vert.c"
	)
else()
	set(COMMON_SOURCES ${COMMON_SOURCES} ${QUAKESPASM_SOURCES})
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

set(WINDOWS_SOURCES
	"${SRC}/Quake/net_win.c"
	"${SRC}/Quake/net_wins.c"
	"${SRC}/Quake/net_wins.h"
	"${SRC}/Quake/net_wipx.c"
	"${SRC}/Quake/net_wipx.h"
	"${SRC}/Quake/pl_win.c"
	"${SRC}/Quake/sys_sdl_win.c"
)

if(PROJECT_VKQUAKE)
	set(WINDOWS_SOURCES
		${WINDOWS_SOURCES}
		"${SRC}/Windows/vkQuake.ico"
		"${SRC}/Windows/vkQuake.rc"
	)
else()
	set(WINDOWS_SOURCES
		${WINDOWS_SOURCES}
		"${SRC}/Windows/QuakeSpasm.ico"
		"${SRC}/Windows/QuakeSpasm.rc"
	)
endif()

set(OTHER_FILES
	"${SRC}/Quake/cd_sdl.c"
	"${SRC}/Quake/lodepng.c"
)

if(PROJECT_VKQUAKE)
	add_executable(${PROJECT_NAME} WIN32)
else()
	add_executable(${PROJECT_NAME} WIN32 MACOSX_BUNDLE)
endif()

target_compile_definitions(${PROJECT_NAME} PRIVATE
	USE_CODEC_UMX
	USE_CODEC_WAVE
)

if(MSVC)
	target_compile_definitions(${PROJECT_NAME} PRIVATE _CRT_SECURE_NO_WARNINGS)
	set(CMAKE_C_FLAGS "/MP ${CMAKE_C_FLAGS}")
endif()

target_include_directories(${PROJECT_NAME} PRIVATE Quake)

if(APPLE)
	if(PROJECT_VKQUAKE)
		set(PLATFORM_SOURCE "${SRC}/Quake/pl_osx.m" ${POSIX_SOURCES})
	else()
		set(PLATFORM_SOURCE "${SRC}/Quake/pl_osx.m" ${MACOS_SOURCES} ${MACOS_RESOURCES} ${POSIX_SOURCES})

		target_include_directories(${PROJECT_NAME} PRIVATE MacOSX)
		target_link_libraries(${PROJECT_NAME} PRIVATE "-framework AppKit -framework IOKit")

		set_target_properties(${PROJECT_NAME} PROPERTIES
			MACOSX_BUNDLE_INFO_PLIST "${SRC}/MacOSX/Info.plist"
		)
		set_source_files_properties(${MACOS_RESOURCES} PROPERTIES 
			MACOSX_PACKAGE_LOCATION Resources
		)
	endif()

	set(OTHER_FILES ${LINUX_SOURCES} ${WINDOWS_SOURCES} ${OTHER_FILES})
elseif(WIN32)
	target_link_libraries(${PROJECT_NAME} PRIVATE Winmm Ws2_32)

	set(PLATFORM_SOURCE ${WINDOWS_SOURCES})
	set(OTHER_FILES ${LINUX_SOURCES} ${MACOS_SOURCES} ${MACOS_RESOURCES} ${POSIX_SOURCES} ${OTHER_FILES})
else()
	target_link_libraries(${PROJECT_NAME} PRIVATE m)

	set(PLATFORM_SOURCE ${LINUX_SOURCES} ${POSIX_SOURCES})
	set(OTHER_FILES ${MACOS_SOURCES} ${MACOS_RESOURCES} ${WINDOWS_SOURCES} ${OTHER_FILES})
endif()

target_sources(${PROJECT_NAME} PRIVATE
	${COMMON_SOURCES}
	${PLATFORM_SOURCE}
	${OTHER_FILES}
)

set_source_files_properties(${OTHER_FILES} PROPERTIES HEADER_FILE_ONLY TRUE)

if(NOT PROJECT_VKQUAKE)
	set(OpenGL_GL_PREFERENCE GLVND)
	find_package(OpenGL REQUIRED)
	target_include_directories(${PROJECT_NAME} PRIVATE "${OPENGL_INCLUDE_DIR}")
	target_link_libraries(${PROJECT_NAME} PRIVATE "${OPENGL_LIBRARY}")
endif()

find_package(FLAC)
if(FLAC_FOUND)
	target_compile_definitions(${PROJECT_NAME} PRIVATE USE_CODEC_FLAC)
	target_include_directories(${PROJECT_NAME} PRIVATE "${FLAC_INCLUDE_DIR}")
	target_link_libraries(${PROJECT_NAME} PRIVATE "${FLAC_LIBRARY}")
endif()

find_package(MikMod)
if(MIKMOD_FOUND)
	target_compile_definitions(${PROJECT_NAME} PRIVATE USE_CODEC_MIKMOD)
	target_include_directories(${PROJECT_NAME} PRIVATE "${MIKMOD_INCLUDE_DIR}")
	target_link_libraries(${PROJECT_NAME} PRIVATE "${MIKMOD_LIBRARY}")
endif()

find_package(MPG123)
if(MPG123_FOUND)
	target_compile_definitions(${PROJECT_NAME} PRIVATE USE_CODEC_MP3)
	target_sources(${PROJECT_NAME} PRIVATE "${SRC}/Quake/snd_mpg123.c")
	target_include_directories(${PROJECT_NAME} PRIVATE "${MPG123_INCLUDE_DIR}")
	target_link_libraries(${PROJECT_NAME} PRIVATE "${MPG123_LIBRARY}")
else()
	find_package(Mad)
	if(MAD_FOUND)
		target_compile_definitions(${PROJECT_NAME} PRIVATE USE_CODEC_MP3)
		target_sources(${PROJECT_NAME} PRIVATE "${SRC}/Quake/snd_mp3.c")
		target_include_directories(${PROJECT_NAME} PRIVATE "${MAD_INCLUDE_DIR}")
		target_link_libraries(${PROJECT_NAME} PRIVATE "${MAD_LIBRARY}")
	endif()
endif()

find_package(Opus)
if(OPUS_FOUND)
	target_compile_definitions(${PROJECT_NAME} PRIVATE USE_CODEC_OPUS)
	target_include_directories(${PROJECT_NAME} PRIVATE "${OPUS_INCLUDE_DIR}")
	target_link_libraries(${PROJECT_NAME} PRIVATE "${OPUS_LIBRARY}" "${OPUSFILE_LIBRARY}")
endif()

# TODO: add option to use SDL1

find_package(SDL2)
if(NOT SDL2_FOUND AND WIN32)
	set(SDL2_FOUND TRUE)
	set(SDL2_DIR "${SRC}/Windows/SDL2")
	set(SDL2_INCLUDE_DIR "${SDL2_DIR}/include")
	set(SDL2_LIBRARY SDL2 SDL2main)

	# TODO: detect ARM target
	if(CMAKE_SIZEOF_VOID_P EQUAL 8)
		target_link_directories(${PROJECT_NAME} PRIVATE ${SDL2_DIR}/lib64)
	else()
		target_link_directories(${PROJECT_NAME} PRIVATE ${SDL2_DIR}/lib)
	endif()
endif()

if(SDL2_FOUND)
	target_compile_definitions(${PROJECT_NAME} PRIVATE USE_SDL2)
	target_include_directories(${PROJECT_NAME} PRIVATE "${SDL2_INCLUDE_DIR}")
	target_link_libraries(${PROJECT_NAME} PRIVATE "${SDL2_LIBRARY}")
else()
	message(SEND_ERROR "Could NOT find SDL2")
endif()

find_package(Vorbis)
if(VORBIS_FOUND)
	target_compile_definitions(${PROJECT_NAME} PRIVATE USE_CODEC_VORBIS)
	target_include_directories(${PROJECT_NAME} PRIVATE "${VORBIS_INCLUDE_DIR}")
	target_link_libraries(${PROJECT_NAME} PRIVATE "${VORBIS_LIBRARY}" "${VORBISFILE_LIBRARY}")
endif()

if(PROJECT_VKQUAKE)
	find_package(Vulkan)
	if(Vulkan_FOUND)
		target_include_directories(${PROJECT_NAME} PRIVATE "${Vulkan_INCLUDE_DIR}")
		target_link_libraries(${PROJECT_NAME} PRIVATE "${Vulkan_LIBRARY}")
	endif()
endif()

find_package(XMP)
if(XMP_FOUND)
	target_compile_definitions(${PROJECT_NAME} PRIVATE USE_CODEC_XMP)
	target_include_directories(${PROJECT_NAME} PRIVATE "${XMP_INCLUDE_DIR}")
	target_link_libraries(${PROJECT_NAME} PRIVATE "${XMP_LIBRARY}")
endif()

if(PROJECT_SPIKED)
	find_package(ZLIB)
	if(ZLIB_FOUND)
		target_compile_definitions(${PROJECT_NAME} PRIVATE USE_ZLIB)
		target_include_directories(${PROJECT_NAME} PRIVATE "${ZLIB_INCLUDE_DIR}")
		target_link_libraries(${PROJECT_NAME} PRIVATE "${ZLIB_LIBRARY}")
	endif()
endif()

if(PROJECT_VKQUAKE)
	set(ENGINE_PAK_FILE vkquake.pak)
else()
	set(ENGINE_PAK_FILE quakespasm.pak)
endif()

add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD COMMAND
	${CMAKE_COMMAND} -E copy_if_different
	"${SRC}/Quake/${ENGINE_PAK_FILE}"
	"$<TARGET_PROPERTY:${PROJECT_NAME},BINARY_DIR>/$<CONFIG>/${ENGINE_PAK_FILE}"
)
