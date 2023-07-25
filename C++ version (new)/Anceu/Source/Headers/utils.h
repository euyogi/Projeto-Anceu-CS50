#pragma once

#include <chrono>
#include <iostream>

#ifdef DFUNCS
    #define DERR(x, y) if (x) std::cerr << y << std::endl;
    #define DTIMER(x) Utils::Timer t(x);
    #define DLOG(x) std::clog << x << std::endl;
#else
    #define DERR(x, y)
    #define DTIMER(x)
    #define DLOG(x)
#endif

namespace Utils {
    struct Timer {
    public:
        // Inicia o timer (ele para no fim do scope no qual foi declarado).
        Timer(const char* timer_name);

        ~Timer();

    private:
        const char* m_timer_name;
        std::chrono::system_clock::time_point m_start;
    };
}