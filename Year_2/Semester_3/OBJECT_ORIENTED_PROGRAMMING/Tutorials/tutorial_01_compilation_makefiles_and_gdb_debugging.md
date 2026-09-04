# Tutorial 01: Modern C++ Compilation, Makefiles, and GDB Debugging

This tutorial covers the multi-file compilation model in C++, structuring clean modular build systems via GNU Make, and inspecting program state with the GNU Debugger (GDB).

---

## 1. The Multi-File Compilation Model

In C++, codebases are split into header files (`.hpp` / `.h`) containing declarations and source files (`.cpp`) containing definitions.

```
Source Files (.cpp)  ---> Compiler (g++ -c) ---> Object Files (.o)  ---> Linker (g++) ---> Executable Binary
Header Files (.hpp)  /
```

### Compilation Flags:
```bash
g++ -std=c++17 -Wall -Wextra -Wpedantic -g -O0 -c main.cpp -o main.o
```
- `-Wall -Wextra -Wpedantic`: Enables strict compiler warnings for potential defects.
- `-g`: Generates DWARF debugging symbols required by GDB.
- `-O0`: Disables optimizations to maintain 1-to-1 line mapping during debugging.

---

## 2. Professional GNU Makefile

```makefile
CXX := g++
CXXFLAGS := -std=c++17 -Wall -Wextra -Wpedantic -g -O0
LDFLAGS := 

SRC_DIR := src
OBJ_DIR := obj
BIN_DIR := bin

TARGET := $(BIN_DIR)/app

SRCS := $(wildcard $(SRC_DIR)/*.cpp)
OBJS := $(patsubst $(SRC_DIR)/%.cpp,$(OBJ_DIR)/%.o,$(SRCS))

all: $(TARGET)

$(TARGET): $(OBJS) | $(BIN_DIR)
	$(CXX) $(OBJS) -o $@ $(LDFLAGS)

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp | $(OBJ_DIR)
	$(CXX) $(CXXFLAGS) -Iinclude -c $< -o $@

$(BIN_DIR) $(OBJ_DIR):
	mkdir -p $@

clean:
	rm -rf $(OBJ_DIR) $(BIN_DIR)

.PHONY: all clean
```

---

## 3. Debugging with GDB

Launch executable under GDB:
```bash
gdb ./bin/app
```

### Essential GDB Commands:
| Command | Shorthand | Description |
|---|---|---|
| `run [args]` | `r` | Start program execution with optional command-line arguments |
| `break [func/line]` | `b` | Set breakpoint at function name or source line number (`b main.cpp:42`) |
| `next` | `n` | Step over next line of code without entering functions |
| `step` | `s` | Step into function calls |
| `continue` | `c` | Resume execution until next breakpoint or termination |
| `print [expr]` | `p` | Evaluate and print variable or expression value (`p this->balance_`) |
| `backtrace` | `bt` | Print call stack frames after segmentation fault or crash |
| `quit` | `q` | Exit debugger |

