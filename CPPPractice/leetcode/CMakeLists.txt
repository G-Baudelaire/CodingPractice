# Header-only solutions: every .h in this directory is part of the library.
file(GLOB LEETCODE_HEADERS CONFIGURE_DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/*.h")

add_library(leetcode INTERFACE)
target_sources(leetcode INTERFACE ${LEETCODE_HEADERS})
target_include_directories(leetcode INTERFACE ${CMAKE_CURRENT_SOURCE_DIR})
