#pragma once

#include <Windows.h>

namespace UI {
	// Chamar fora do window loop.
	void setWndStyle(HWND);
	// Chamar após mudança de DPI.
	void updateWndPaddings(HWND);
	// Chamar dentro do window loop.
	void showAnceuWnd(bool* loop_boolean);

	float getDpiScale();
}