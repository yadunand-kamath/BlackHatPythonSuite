# CHANGELOG

## v.1.0.0 - 2025-05-12

### Added

- `src/cpp_launcher/console.hpp` (PR #2)
    - Created `console.hpp` to encapsulate console-related functionalities.
    - Implemented a `clear()` function to clear the console screen, with OS-specific implementations for Windows and Linux.
    - Added an error message and exit code for unsupported operating systems.
    
- `src/cpp_launcher/main.cpp` (PR #2)
    - Created `main.cpp` as the C++ CLI launcher.
    - Included necessary headers such as `<iostream>`, `<string>`, `<vector>`, and `<cstdlib>`.
    - Defined a PythonScript struct to store information about Python scripts (name, description, path).
    - Created a scripts vector containing details of available Python scripts.
    - Implemented a `menu()` function to display the list of available Python scripts to the user.
    - Implemented a `read()` function to read user input and handle script selection (currently only handles exit option and invalid options).
    - The `main()` function calls `console::clear`, `menu()`, and `read()` to present the menu and handle user input.

