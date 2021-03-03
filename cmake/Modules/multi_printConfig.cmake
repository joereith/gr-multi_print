INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_MULTI_PRINT multi_print)

FIND_PATH(
    MULTI_PRINT_INCLUDE_DIRS
    NAMES multi_print/api.h
    HINTS $ENV{MULTI_PRINT_DIR}/include
        ${PC_MULTI_PRINT_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    MULTI_PRINT_LIBRARIES
    NAMES gnuradio-multi_print
    HINTS $ENV{MULTI_PRINT_DIR}/lib
        ${PC_MULTI_PRINT_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(MULTI_PRINT DEFAULT_MSG MULTI_PRINT_LIBRARIES MULTI_PRINT_INCLUDE_DIRS)
MARK_AS_ADVANCED(MULTI_PRINT_LIBRARIES MULTI_PRINT_INCLUDE_DIRS)

