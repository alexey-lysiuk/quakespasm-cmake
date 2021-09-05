find_path(XMP_INCLUDE_DIR xmp.h)
find_library(XMP_LIBRARY xmp)
mark_as_advanced(XMP_INCLUDE_DIR XMP_LIBRARY)

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(XMP DEFAULT_MSG XMP_LIBRARY XMP_INCLUDE_DIR)
