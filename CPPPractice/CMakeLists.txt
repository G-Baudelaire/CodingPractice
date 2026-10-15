cmake_minimum_required(VERSION 3.30)
project(CppPractice LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 26)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_subdirectory(leetcode)
add_subdirectory(neetcode)

add_executable(cpp_practice main.cpp)
target_link_libraries(cpp_practice PRIVATE leetcode neetcode)
