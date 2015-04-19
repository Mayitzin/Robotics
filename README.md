# Robotics

Useful Code for the several Robotics fields. It is divided into four major branches:
- Control.
- Intelligence.
- Motion.
- Sensing

There is an extra folder **Data** to store the files used for examples and tests.

The code is created using the Standard C99. For example, to compile a C file with GCC you can indicate this standard with:

```
gcc file.c -o output -std=c99
```

Unix systems may not find the files defining the called functions (although included in the code), so you must tell the linker to search for the required library using the -lm flag at the end of the command.

```
gcc file.c -o output -std=c99 -lm
```