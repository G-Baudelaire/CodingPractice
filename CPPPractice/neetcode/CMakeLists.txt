# Header-only solutions: every .h in this directory is part of the library.
file(GLOB NEETCODE_HEADERS CONFIGURE_DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/*.h")

add_library(neetcode INTERFACE)
target_sources(neetcode INTERFACE ${NEETCODE_HEADERS})
target_include_directories(neetcode INTERFACE ${CMAKE_CURRENT_SOURCE_DIR})

