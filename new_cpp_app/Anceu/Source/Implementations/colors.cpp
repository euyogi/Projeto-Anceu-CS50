#include "colors.h"

Colors::Color::Color(int r, int g, int b) {
    m_r = r; m_g = g; m_b = b;
}

COLORREF Colors::Color::colorRef() const {
    return RGB(m_r, m_g, m_b);
}

ImVec4 Colors::Color::imVec4(int opacity) const {
    return { m_r / 255.0f, m_g / 255.0f, m_b / 255.0f, opacity / 255.0f };
}

const Colors::Color Colors::BLACK = { 0, 0, 0 };
const Colors::Color Colors::LIGHTEST_WINE = { 125, 68, 64 };
const Colors::Color Colors::LIGHT_WINE = { 100, 54, 51 };
const Colors::Color Colors::WINE = { 80, 43, 41 };
const Colors::Color Colors::DARK_WINE = { 44, 27, 26 };
const Colors::Color Colors::DARK_GRAY_WINE = { 44, 33, 33 };
const Colors::Color Colors::LIGHTEST_GRAY = { 237, 237, 237 };
const Colors::Color Colors::LIGHT2_GRAY = { 114, 114, 114 };
const Colors::Color Colors::LIGHT1_GRAY = { 94, 94, 94 };
const Colors::Color Colors::GRAY = { 74, 70, 70 };
const Colors::Color Colors::DARK_GRAY = { 67, 61, 61 };
const Colors::Color Colors::LIGHT_RED = { 255, 77, 77 };
const Colors::Color Colors::RED = { 165, 54, 31 };
const Colors::Color Colors::DARK_RED = { 132, 44, 36 };
const Colors::Color Colors::DARKEST_RED = { 106, 35, 21 };
const Colors::Color Colors::LIGHT_GREEN = { 68, 237, 68 };
