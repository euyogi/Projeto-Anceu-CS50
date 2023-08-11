# Esse arquivo é utilizado para compilar com cmake, infelizmente o tamanho final do aplicativo
# parece ficar em 4Mb quando compilado com cmake enquanto que com Visual Studio fica 1Mb

cmake_minimum_required(VERSION 3.26)
project(Anceu)

set(CMAKE_CXX_STANDARD 20)

include_directories(Anceu/Source/Headers)
include_directories(ImGui/Source/Headers)
include_directories(Neyo/Source/Headers)
include_directories(Neyo/Externals/zlib)

add_executable(Anceu
        Anceu/Source/Headers/anceu.h
        Anceu/Source/Headers/colors.h
        Anceu/Source/Headers/khlorz_combo_filter.h
        Anceu/Source/Headers/resources.h
        Anceu/Source/Headers/texts.h
        Anceu/Source/Headers/ui.h
        Anceu/Source/Headers/utils.h
        Anceu/Source/Implementations/anceu.cpp
        Anceu/Source/Implementations/colors.cpp
        Anceu/Source/Implementations/khlorz_combo_filter.cpp
        Anceu/Source/Implementations/main.cpp
        Anceu/Source/Implementations/texts.cpp
        Anceu/Source/Implementations/ui.cpp
        Anceu/Source/Implementations/utils.cpp
        Anceu/Source/Resources/fonts.cpp
        Anceu/Source/Resources/icon.ico
        Anceu/Source/Resources/icon.psd
        Anceu/Source/Resources/resources.rc
        Anceu/Source/Resources/sounds.cpp
        ImGui/Source/Headers/imconfig.h
        ImGui/Source/Headers/imgui.h
        ImGui/Source/Headers/imgui_impl_dx11.h
        ImGui/Source/Headers/imgui_impl_win32.h
        ImGui/Source/Headers/imgui_internal.h
        ImGui/Source/Headers/imstb_rectpack.h
        ImGui/Source/Headers/imstb_textedit.h
        ImGui/Source/Headers/imstb_truetype.h
        ImGui/Source/Implementations/imgui.cpp
        ImGui/Source/Implementations/imgui_demo.cpp
        ImGui/Source/Implementations/imgui_draw.cpp
        ImGui/Source/Implementations/imgui_impl_dx11.cpp
        ImGui/Source/Implementations/imgui_impl_win32.cpp
        ImGui/Source/Implementations/imgui_tables.cpp
        ImGui/Source/Implementations/imgui_widgets.cpp
        Neyo/Externals/zlib/zconf.h
        Neyo/Externals/zlib/zlib.h
        Neyo/Externals/zlib/zlibstatic.lib
        Neyo/Source/Headers/neyo.h
        Neyo/Source/Implementations/neyo.cpp)

target_link_options(Anceu PRIVATE -static -mwindows) # Windows build (main = WinMain, no console)
target_link_directories(Anceu PRIVATE Neyo/Externals/zlib)

# Libraries:
target_link_libraries (Anceu PRIVATE urlmon d3d11 d3dcompiler dwmapi winmm)
target_link_libraries (Anceu PRIVATE -lz)
