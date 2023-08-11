#pragma once

#include <Windows.h>

#include "imgui.h"

namespace Colors {
    struct Color {
    public:
        Color(int r, int g, int b);

        // Muda o tipo da cor.
        COLORREF colorRef() const;
        // Muda o tipo da cor.
        ImVec4 imVec4(int opacity = 255) const;

    private:
        int m_r, m_g, m_b;
    };

    const extern Color BLACK;
    const extern Color LIGHTEST_WINE;
    const extern Color LIGHT_WINE;
    const extern Color WINE;
    const extern Color DARK_WINE;
    const extern Color DARK_GRAY_WINE;
    const extern Color LIGHTEST_GRAY;
    const extern Color LIGHT2_GRAY;
    const extern Color LIGHT1_GRAY;
    const extern Color GRAY;
    const extern Color DARK_GRAY;
    const extern Color LIGHT_RED;
    const extern Color RED;
    const extern Color DARK_RED;
    const extern Color DARKEST_RED;
    const extern Color LIGHT_GREEN;
}