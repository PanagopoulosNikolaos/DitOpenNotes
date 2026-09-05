# Makefile for DSA C++ Implementations
# Course: Data Structures and Algorithms (Course Code: 305)

CXX := g++
CXXFLAGS := -std=c++17 -Wall -Wextra -Wpedantic -O2 -DSKIP_STANDALONE_MAIN
DEBUG_FLAGS := -std=c++17 -Wall -Wextra -Wpedantic -g -DDEBUG -DSKIP_STANDALONE_MAIN

TARGET := main
SRC := main.cpp

.PHONY: all clean run debug help

all: $(TARGET)

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(SRC)

debug: $(SRC)
	$(CXX) $(DEBUG_FLAGS) -o $(TARGET)_debug $(SRC)

run: $(TARGET)
	./$(TARGET)

clean:
	rm -f $(TARGET) $(TARGET)_debug

help:
	@echo "Available targets:"
	@echo "  all    : Compiles the main demonstration executable (default)"
	@echo "  run    : Compiles and runs the main demonstration"
	@echo "  debug  : Compiles with debugging symbols and DEBUG macro defined"
	@echo "  clean  : Removes compiled binary executables"

