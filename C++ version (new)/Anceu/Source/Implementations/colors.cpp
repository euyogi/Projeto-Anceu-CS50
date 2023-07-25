#include "colors.h"

Colors::Color::Color(int r, int g, int b) {
    m_r = r; m_g = g; m_b = b;
}

COLORREF Colors::Color::colorRef() {
    return RGB(m_r, m_g, m_b);
}

HBRUSH Colors::Color::hBrush() {
    return CreateSolidBrush(Colors::Color::colorRef());
}

ImVec4 Colors::Color::imVec4(int opacity) {
    return { m_r / 255.0f, m_g / 255.0f, m_b / 255.0f, opacity / 255.0f };
}

inline Colors::Color Colors::BLACK = { 0, 0, 0 };
Colors::Color Colors::LIGHTEST_WINE = { 125, 68, 64 };
Colors::Color Colors::LIGHT_WINE = { 100, 54, 51 };
Colors::Color Colors::WINE = { 80, 43, 41 };
Colors::Color Colors::DARK_WINE = { 44, 27, 26 };
Colors::Color Colors::DARKER_WINE = { 18, 11, 10 };
Colors::Color Colors::DARK_GRAY_WINE = { 44, 33, 33 };
Colors::Color Colors::LIGHTEST_GRAY = { 237, 237, 237 };
Colors::Color Colors::LIGHT2_GRAY = { 114, 114, 114 };
Colors::Color Colors::LIGHT1_GRAY = { 94, 94, 94 };
Colors::Color Colors::GRAY = { 74, 70, 70 };
Colors::Color Colors::DARK_GRAY = { 67, 61, 61 };
Colors::Color Colors::DARKEST_GRAY = { 57, 51, 51 };
Colors::Color Colors::LIGHT_RED = { 255, 77, 77 };
Colors::Color Colors::RED = { 165, 54, 31 };
Colors::Color Colors::DARK_RED = { 132, 44, 36 };
Colors::Color Colors::DARKEST_RED = { 106, 35, 21 };
Colors::Color Colors::LIGHT_GREEN = { 68, 237, 68 };
