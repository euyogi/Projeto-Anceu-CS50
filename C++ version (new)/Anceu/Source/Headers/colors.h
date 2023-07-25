#pragma once

#include <Windows.h>

#include "imgui.h"

namespace Colors {
    struct Color {
    public:
        Color(int r, int g, int b);

        // Muda o tipo da cor.
        COLORREF colorRef();
        // Muda o tipo da cor.
        HBRUSH hBrush();
        // Muda o tipo da cor.
        ImVec4 imVec4(int opacity = 255);

    private:
        int m_r, m_g, m_b;
    };

    extern Color BLACK;
    extern Color LIGHTEST_WINE;
    extern Color LIGHT_WINE;
    extern Color WINE;
    extern Color DARK_WINE;
    extern Color DARKER_WINE;
    extern Color DARK_GRAY_WINE;
    extern Color LIGHTEST_GRAY;
    extern Color LIGHT2_GRAY;
    extern Color LIGHT1_GRAY;
    extern Color GRAY;
    extern Color DARK_GRAY;
    extern Color DARKEST_GRAY;
    extern Color LIGHT_RED;
    extern Color RED;
    extern Color DARK_RED;
    extern Color DARKEST_RED;
    extern Color LIGHT_GREEN;
}