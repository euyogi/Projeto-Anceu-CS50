#include "utils.h"

Utils::Timer::Timer(const char* timer_name) : m_timer_name(timer_name) {
    m_start = std::chrono::system_clock::now();
}

Utils::Timer::~Timer() {
    std::chrono::system_clock::time_point end = std::chrono::system_clock::now();

    std::chrono::duration<double> duration = end - m_start;

    std::clog << m_timer_name << " -> " << duration.count() * 1000 << "ms" << std::endl;
}