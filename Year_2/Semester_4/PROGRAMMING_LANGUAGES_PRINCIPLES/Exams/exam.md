### Topic 1 - A (0.5)

**A.** Answer with True or False the following statements. In case of an error, justify your answer to receive full credit:
1. Python belongs to the family of functional programming languages
2. A lexeme is the lowest-level syntactic unit of the language
3. In Python, function definitions are executable
4. C provides exception handling mechanisms
5. The header of a subroutine defines the actions that the subroutine will execute
6. In PHP, variable declaration is done with `var`

***

**Solution:**

1. **False.** Python is a multi-paradigm programming language (mainly imperative and object-oriented) and not purely functional.
2. **True.** According to programming language theory, the lexeme is the lowest-level syntactic unit of the language (e.g., a specific variable name or an operator).
3. **True.** In Python, the `def` statement is an executable statement that runs at runtime to bind the function name to the corresponding function object.
4. **False.** The C language does not support a built-in exception handling mechanism (like `try/catch`). Error handling is done via function return values or libraries (e.g., `setjmp.h`).
5. **False.** The header defines only the interface of the subroutine (name, parameters, return type). The actions that the subroutine executes are defined in its body.
6. **False.** In PHP, variable declaration is done with the `$` prefix (e.g., `$x = 5`) and the keyword `var` is not used for local variables (it is used for class properties in older versions).

***

### Topic 1 - B (0.5)

**B.** Match each concept with its definition

| Concept | Definition |
| :--- | :--- |
| 1. Compiler | A. Compromise solution between compilers and pure interpreters |
| 2. Hybrid systems | B. Execution happens instruction by instruction |
| 3. JIT | C. Execution happens after translation into machine language |
| 4. Interpreter | D. Translates the program into an intermediate language and compiles it at execution time |

***

**Solution:**

* **1** -> **C** (Compiler: Execution happens after translation into machine language)
* **2** -> **A** (Hybrid systems: Compromise solution between compilers and pure interpreters)
* **3** -> **D** (JIT: Translates the program into an intermediate language and compiles it at execution time)
* **4** -> **B** (Interpreter: Execution happens instruction by instruction)

***

### Topic 1 - C (0.5)

**C.** Choose the correct answer. Justify your answer to receive full credit.

1. What do the `{}` mean in the regular expression `a{5}`?
   * A. 5 or fewer a's
   * B. Exactly 5 a's
   * C. 5 or more a's
   * D. None of the above

2. What will be the value of `x` at the end of the program
   ```python
   x=1
   def cg():
       global x
       x=x+1
   cg()
   print(x)
   ```
   * A. 2
   * B. 1
   * C. 0
   * D. None of the above

3. What will be the output of the following program
   ```python
   colors = {}
   def insert(items):
       if(items in colors):
           colors[items]+=1
       else:
           colors[items]=1
   insert('Red')
   insert('Green')
   insert('Red')
   print(len(colors))
   ```
   *(Note: The original text contained typographical errors, such as `if(items in colors:` without a closing parenthesis, and `color[items]=1` without the `s`. The corrected, executable form is presented here.)*
   * A. 3
   * B. 1
   * C. 2
   * D. None of the above

***

**Solution:**

1. **B. Exactly 5 a's.** In regular expressions, the `{n}` syntax indicates that the preceding symbol must appear exactly `n` times.
2. **A. 2.** The `global x` declaration inside `cg()` specifies that the variable `x` refers to the global variable `x` defined externally. Therefore, the statement `x=x+1` increases the value of the global variable from `1` to `2`.
3. **C. 2.** The dictionary `colors` contains unique keys for each color. After the three calls to `insert()`, the dictionary will be `{'Red': 2, 'Green': 1}`. The function `len(colors)` returns the number of keys in the dictionary, which is `2`.

***

### Topic 2 - A (1)

Consider the following Python subroutine:
```python
def calculate():
    num = 1
    def inner_func():
        nonlocal num
        num += 2
        return num
    return inner_func

odd = calculate()

print(odd())
print(odd())
print(odd())

odd2 = calculate()
print(odd2())
```

**A.** Describe what it does

***

**Solution:**

The code implements a **closure** mechanism in Python.

1. The outer function `calculate` defines a local variable `num = 1` and an inner function `inner_func`.
2. `inner_func` uses the `nonlocal num` keyword to declare that `num` is not local to itself but belongs to the scope of the immediately enclosing function (`calculate`). Thus, it can read and modify its value.
3. `calculate` returns the function object `inner_func` (without calling it).
4. The returned `odd` object "remembers" the environment in which it was created and the specific `num` variable. Each time `odd()` is called, it increases `num` by `2` and returns it, producing successive odd numbers.
5. Each new call to `calculate()` (e.g., `odd2 = calculate()`) creates a new, independent scope with its own separate `num` variable initialized to `1`.

***

### Topic 2 - B (1)

Consider the following Python subroutine:
```python
def calculate():
    num = 1
    def inner_func():
        nonlocal num
        num += 2
        return num
    return inner_func

odd = calculate()

print(odd())
print(odd())
print(odd())

odd2 = calculate()
print(odd2())
```

**B.** What will it print when executed?

***

**Solution:**

When executed, the program will print:
```
3
5
7
3
```

**Analysis:**
- `odd = calculate()`: The first closure is created with `num = 1`.
- `print(odd())`: `inner_func` increases `num` by `2` (`1 + 2 = 3`) and prints `3`.
- `print(odd())`: `inner_func` increases the already existing `num` by `2` (`3 + 2 = 5`) and prints `5`.
- `print(odd())`: `inner_func` increases `num` by `2` (`5 + 2 = 7`) and prints `7`.
- `odd2 = calculate()`: A new, independent closure is created with a new `num = 1`.
- `print(odd2())`: `inner_func` increases the new `num` by `2` (`1 + 2 = 3`) and prints `3`.

***

### Topic 3 (3.5)

Write a Python function that checks whether a phrase is a pangram.
Note: A pangram is a word that contains all 24 letters of the Greek alphabet.

***

**Solution:**

The `isPangram` function in Python is given below, which checks whether a phrase contains all 24 letters of the Greek alphabet. For correct operation, the function converts characters to lowercase, removes accents and diacritics, and maps the final sigma «ς» to the normal sigma «σ».

```python
def isPangram(phrase: str) -> bool:
    """Checks if the given Greek phrase is a pangram.

    A pangram is a sentence containing all 24 letters of the Greek alphabet.

    Args:
        phrase (str): The input phrase to check.

    Returns:
        bool: True if the phrase contains all Greek letters, False otherwise.
    """
    greek_letters = set("αβγδεζηθικλμνξοπρστυφχψω")
    
    # Normalize input to lowercase
    normalized_phrase = phrase.lower()
    
    # Map accented greek characters to their unaccented equivalents
    replacements = {
        'ά': 'α', 'έ': 'ε', 'ή': 'η', 'ί': 'ι', 'ΐ': 'ι', 'ϊ': 'ι',
        'ό': 'ο', 'ύ': 'υ', 'ΰ': 'υ', 'ϋ': 'υ', 'ώ': 'ω', 'ς': 'σ'
    }
    
    # Clean the input phrase by replacing accented characters and final sigma
    for accented_char, plain_char in replacements.items():
        normalized_phrase = normalized_phrase.replace(accented_char, plain_char)
        
    # Keep only the valid Greek alphabet characters from the phrase
    found_letters = set(char for char in normalized_phrase if char in greek_letters)
    
    # Verify if all 24 letters are present
    return len(found_letters) == 24
```

***

### Topic 4 - A (3)

**A.** Create the EBNF grammar for recognizing a postal address of the form:
```
Name Surname
Street number
City
Country
Postal code
```

***

**Solution:**

The EBNF grammar definition for recognizing the postal address is presented below:

```ebnf
address         = name_line newline street_line newline city_line newline country_line newline zip_line
name_line       = first_name space last_name
street_line     = street_number space street_name
city_line       = city_name
country_line    = country_name
zip_line        = zip_code

first_name      = letter { letter }
last_name       = letter { letter }
street_name     = letter { letter }
city_name       = letter { letter }
country_name    = letter { letter }

street_number   = digit { digit }
zip_code        = digit { digit }

letter          = "a" | ... | "z" | "A" | ... | "Z" | "α" | ... | "ω" | "Α" | ... | "Ω"
digit           = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
space           = " "
newline         = "\n"
```
