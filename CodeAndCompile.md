# Coding and Compiling Standards

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

For Windows users a statical linking problem might appear. To avoid this you can directly link statically with:

```
g++ file.cpp -std=c++11 -static-libgcc -static-libstdc++ -o output
```

This solution **does not apply to GNU-based system** (like Linux), as there it links with the static version of libgcc by default.

If possible, there will be a make file available for each application.