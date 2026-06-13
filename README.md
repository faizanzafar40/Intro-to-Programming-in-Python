# Intro to Programming in Python

Learning to write code was never this easy!

This is the beginner's Python course I put together for anyone who wants to learn
programming from scratch. I believe in learning by doing, so instead of long
chapters of theory it is built around lots of small, self-contained scripts —
each one demonstrates a single concept and is short enough to read, run, and
tweak in a couple of minutes. The lecture slides cover the ideas; the scripts
let you see them work.

## Built with

- **Python 3** (the practice scripts use only the standard library)
- **NumPy**, **pandas**, and **matplotlib** for the data-analysis section
- **Black** for consistent formatting across every script

## What's inside

The material is organised in the order I teach it:

| Folder | What it covers |
| --- | --- |
| `docs/slides/` | The lecture slide decks — start here for each topic |
| `practice_programs/` | ~30 bite-sized scripts: variables, I/O, operators, conditionals, loops, lists, functions, files, exceptions, and a first look at classes |
| `oop_concepts/` | Object-oriented programming: composition, inheritance, polymorphism, operator overloading, and public vs. private members |
| `data_analysis/` | Hands-on tours of NumPy and pandas |
| `full_exercises/` | Larger end-to-end exercises, including a memory game and a console "Amazon" shopping app |

The scripts in `practice_programs/` are numbered so you can work through them top
to bottom, which roughly follows the outline below.

### Introduction
- Introduction to Programming
- Introduction to Python
- Applications and syntax
- Setting up the environment

### Basics of programming
- Constants and variables, data types
- `input()` / `print()`
- Arithmetic and logical operators
- Conditional statements
- Data structures (list, tuple, dictionary, ...)
- Loops (`for`, `while`), `range()`, `break` / `continue`
- Functions and built-in functions

### Intermediate topics
- File handling (reading, writing, and the `with` statement)
- Modules and the `import` statement
- The `math` module
- Exceptions and `try` / `except`
- The basics of classes and objects

### Python for data analysis
- NumPy
- pandas
- matplotlib

## Getting started

You need Python 3 installed. Clone the repository and you can run any of the
standard-library scripts straight away — no setup required:

```bash
python practice_programs/01_hello_world.py
```

Many scripts are interactive and will prompt you for input, for example:

```bash
python practice_programs/03_age_exercise.py
python practice_programs/21_palindrome.py
python full_exercises/memory_game.py
```

A script can be run from anywhere — its own folder is added to the import path,
so the calculator example finds its helper module automatically:

```bash
python practice_programs/20_calculator_main.py
```

### Running the data-analysis scripts

Only the `data_analysis/` scripts need extra packages. Install them first
(ideally in a virtual environment):

```bash
pip install -r requirements.txt
python data_analysis/numpy_basics.py
python data_analysis/pandas_basics.py
```

`numpy_basics.py` opens a matplotlib window to plot a sine curve, so run it on a
machine with a display.

## Formatting

Every script is formatted with [Black](https://black.readthedocs.io/) using the
configuration in `pyproject.toml`. To re-format after editing:

```bash
pip install black
black .
```

## Project structure

```
.
├── docs/slides/         # Lecture slide decks (.pptx)
├── practice_programs/   # Numbered beginner scripts, one concept each
├── oop_concepts/        # Object-oriented programming examples
├── data_analysis/       # NumPy and pandas walkthroughs
├── full_exercises/      # Larger exercises and mini-projects
├── requirements.txt     # Dependencies for the data-analysis scripts
└── pyproject.toml       # Black / Ruff configuration
```

## What I learned building this

I started this as my own notes while learning Python and turned it into a course
I could teach from. Writing a tiny program for every concept forced me to make
sure I actually understood each one well enough to explain it simply — which, it
turns out, is the best way to learn it yourself.

## Contributing

Feel free to open an issue or a pull request if you spot something to improve or
have an idea for another example. And star the repository if you had fun with
Python!

## License

This project is released under the [MIT License](LICENSE).
