# Robotics

Useful Code for the several Robotics fields. It is divided into four major branches:
- Control.
- Intelligence.
- Motion.
- Sensing

There is an extra folder **Data** to store the files used for examples and tests.

The code in C is compiled using the Standard C99. For example with the GCC you can indicate this standard with:

```
gcc file.c -std=c99 -o output
```

Unix systems may not find the files defining the called functions (although included in the code), so you must tell the linker to search for the required library using the -lm flag at the end of the command.

```
gcc file.c -std=c99 -o output -lm
```

The code in C++ is compiled using the Standard C++11. For example with the GCC you can also indicate this standard as:

```
g++ file.cpp -std=c++11 -o output
```