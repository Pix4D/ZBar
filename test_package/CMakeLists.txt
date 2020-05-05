cmake_minimum_required(VERSION 3.10)
project(ZBarQRCodeTest)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_set_find_paths()

if (APPLE)
    set(CMAKE_INSTALL_RPATH "@executable_path/../lib")
elseif(UNIX)
    set(CMAKE_INSTALL_RPATH "$ORIGIN/../lib")
endif()

find_package(zbar)

add_executable(testApp main.cpp)
target_link_libraries(testApp
    PRIVATE
       zbar::zbar
)

install(TARGETS testApp)
# Install imported libraries
install(DIRECTORY ${CMAKE_BINARY_DIR}/conanLibs/
        DESTINATION lib
        FILES_MATCHING
        PATTERN "*.so*"
        PATTERN "*.dylib*")
install(DIRECTORY ${CMAKE_BINARY_DIR}/conanLibs/
        DESTINATION bin
        FILES_MATCHING PATTERN "*.dll")
