find_path(MAD_INCLUDE_DIR mad.h)
find_library(MAD_LIBRARY mad)
mark_as_advanced(MAD_INCLUDE_DIR MAD_LIBRARY)

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(Mad DEFAULT_MSG MAD_LIBRARY MAD_INCLUDE_DIR)
