project(fhn)
set(project_SOURCES fhn.cpp)
set(CMAKE_CXX_FLAGS "-Ofast -Wall -Wextra")
add_executable(fhn ${project_SOURCES})
target_link_libraries(fhn armadillo glut GL GLU)

