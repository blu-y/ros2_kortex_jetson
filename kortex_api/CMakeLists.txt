cmake_minimum_required(VERSION 3.14)
include(FetchContent)
#include(ExternalProject)
FetchContent_Declare(
  kinova_binary_api
  URL https://artifactory.kinovaapps.com:443/artifactory/generic-public/kortex/API/2.5.0/linux_armv7_jetson_gcc.zip 
  URL_HASH MD5=a6c96adc053d7b2095676f009fde1a44
)

FetchContent_MakeAvailable(kinova_binary_api)

project(kortex_api)

#Future:
# convert API_URL components from CMAKE_SYSTEM variables.
# The kinova artifactory server artifacts have slightly different expectations and they need some transformations
# Could build something like: (URL_OS)_(URL_PROCESSOR)_(?)_(URL_COMPILER).zip
# string(REPLACE "_" "-" URL_PROCESSOR ${CMAKE_SYSTEM_PROCESSOR}) # x86_64 -> x86-64
# string(TOLOWER ${CMAKE_SYSTEM_NAME} URL_OS) # Linux -> linux

set(API_URL https://artifactory.kinovaapps.com:443/artifactory/generic-public/kortex/API/2.5.0/linux_armv7_jetson_gcc.zip )

#ExternalProject_Add(kinova_binary_api
#  URL ${API_URL}
#  CONFIGURE_COMMAND ""
#  BUILD_COMMAND ""
#  INSTALL_COMMAND ""
#)

find_package(ament_cmake REQUIRED)

ament_export_include_directories(include/kortex_api)

install(DIRECTORY ${kinova_binary_api_SOURCE_DIR}/include/client/ DESTINATION include/kortex_api)
install(DIRECTORY ${kinova_binary_api_SOURCE_DIR}/include/common/ DESTINATION include/kortex_api)
install(DIRECTORY ${kinova_binary_api_SOURCE_DIR}/include/messages/ DESTINATION include/kortex_api)
install(DIRECTORY ${kinova_binary_api_SOURCE_DIR}/include/client_stubs/ DESTINATION include/kortex_api)
install(DIRECTORY ${kinova_binary_api_SOURCE_DIR}/include/google/protobuf DESTINATION include/kortex_api/google)

ament_package()
