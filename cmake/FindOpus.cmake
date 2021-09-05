find_path(OPUS_INCLUDE_DIR NAMES opusfile.h PATH_SUFFIXES opus)
mark_as_advanced(OPUS_INCLUDE_DIR)

find_library(OPUS_LIBRARY NAMES opus)
mark_as_advanced(OPUS_LIBRARY)

find_library(OPUSFILE_LIBRARY NAMES opusfile)
mark_as_advanced(OPUSFILE_LIBRARY)

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(Opus DEFAULT_MSG OPUSFILE_LIBRARY OPUS_LIBRARY OPUS_INCLUDE_DIR)
