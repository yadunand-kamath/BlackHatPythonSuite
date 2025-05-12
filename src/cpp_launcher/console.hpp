#include <cstdlib>
#include <iostream>

#ifndef CONSOLE_HPP
#define CONSOLE_HPP
namespace console
{
    inline void clear()
    {
        #ifdef _WIN32
            system("cls");
        #elif defined(__linux__)
            system("clear");
        #else
            const int UNSUPPORTED_OS_ERROR = 10;
            std::cout << "Unsupported OS. Please make sure you have modified the source code before compiling for another OS.\n";
            exit(UNSUPPORTED_OS_ERROR);
        #endif
    }
}
#endif
