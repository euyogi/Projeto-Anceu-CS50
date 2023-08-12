#include "ui.h"

#include <Windows.h>
#include <dwmapi.h> // Lembre de incluir respectivo diretório de biblioteca.

#include <span>
#include <future>
#include <format>
#include <cmath>

#include "anceu.h"
#include "colors.h"
#include "texts.h"
#include "resources.h"
#include "imgui.h"
#include "khlorz_combo_filter.h"

#define buttons_height (padding * 0.85f)

constexpr float FONT_SIZE = 18.0f;
float padding = 0.0f; bool dpi_changed = true;

struct SmallerTextBoxData {
    void setText(const char* text, ImVec4 color = { 0.92f, 0.92f, 0.92f, 0.92f }) {
        m_text = text;
        m_color = color;
    }
    
    const char* getText() { return m_text; }
    ImVec4 getColor() { return m_color; }
    
private:
    const char* m_text = Texts::SMALLER_TEXT_BOX_INITIAL;
    ImVec4 m_color = { 0.92f, 0.92f, 0.92f, 0.92f };
} smaller_text_box_data;

enum ChildFrameIDs {
    SmallerTextBoxID = 1, BiggerTextBoxID, ButtonsYearsID, LabelConverterID, ConversionTextBoxID
};

bool        selectableButton(const char*, int, int*);
bool        tipMarker(const char*, ImVec2 = { 0, 0 }, const char* = "?", bool = false);
float       calcItemsWidth(const char*, int = 1);
void        centerAlignNextItems(float, int = 1);
void        rightAlignNextItems(float, int = 1, float = 0.0f);
const char* itemGetter(std::span<const char* const>, int);

void UI::showAnceuWnd(bool* p_loop_boolean) {
    static const ImGuiStyle&    style = ImGui::GetStyle();
    static const ImGuiViewport* viewport = ImGui::GetMainViewport();
    static ImGuiWindowFlags     window_flags = ImGuiWindowFlags_NoDecoration | ImGuiWindowFlags_NoMove | ImGuiWindowFlags_NoSavedSettings | ImGuiWindowFlags_NoBackground | ImGuiWindowFlags_NoNavFocus;

    ImGui::PushStyleVar(ImGuiStyleVar_WindowPadding, { padding, padding });

    ImGui::SetNextWindowPos(viewport->Pos);
    ImGui::SetNextWindowSize(viewport->Size);
    if (ImGui::Begin("Window", nullptr, window_flags)) {
        ImGui::PopStyleVar();

        static ImGuiWindowFlags child_flags =  ImGuiWindowFlags_NoSavedSettings | ImGuiWindowFlags_AlwaysUseWindowPadding | ImGuiWindowFlags_NoNavFocus | ImGuiWindowFlags_NavFlattened;

        ImGui::SetCursorPosY(0); // Ignora o padding superior.
        if (ImGui::BeginChild("Inner Left Frame", { -9 * buttons_height, 0 }, false, child_flags)) {
            static const char* bigger_text_box_text = Texts::BIGGER_TEXT_BOX_INITIAL;
            static const char* nw_tip_marker_text = Texts::NW_TIP_MARKER_INFO;

            if (tipMarker(nw_tip_marker_text, { 0, style.FramePadding.y / 2.0f }, "i", true)) {
                Resources::Sounds::playClickSound();
                if (nw_tip_marker_text == Texts::NW_TIP_MARKER_INFO) {
                    nw_tip_marker_text = Texts::NW_TIP_MARKER_INITIAL;
                    smaller_text_box_data.setText(Texts::SMALLER_TEXT_BOX_INFO);
                    bigger_text_box_text = Texts::BIGGER_TEXT_BOX_INFO;
                }
                else {
                    nw_tip_marker_text = Texts::NW_TIP_MARKER_INFO;
                    smaller_text_box_data.setText(Texts::SMALLER_TEXT_BOX_INITIAL);
                    bigger_text_box_text = Texts::BIGGER_TEXT_BOX_INITIAL;
                }
            }

            static bool combo_courses_focused = false;
            if (not combo_courses_focused) {
                ImGui::SetKeyboardFocusHere(); // Foca o combo dos cursos.
                combo_courses_focused = true;
            }

            static int combo_courses_selected_idx = -1; static float search_width = 0.0f;
            
            if (dpi_changed) search_width = calcItemsWidth(Texts::BUTTON_SEARCH);

            ImGui::SetCursorPosX(ImGui::GetCursorPosX() + buttons_height);
            ImGui::SetNextItemWidth(-(search_width + style.ItemSpacing.x + buttons_height));
            if (ImGui::ComboFilter("##Courses", combo_courses_selected_idx, Texts::COURSES, itemGetter)) {
                Resources::Sounds::playClickSound();
                ImGui::SetKeyboardFocusHere(); // Foca o botão pesquisar.
            }

            // Pesquisar depende/altera as variáveis dos outros widgets, por isso as declarações aqui.
            static const char*  se_button_text = Texts::SE_BUTTON_DETAILS;
            static bool         se_button_disabled = true, are_pdfs_downloaded = false, start_progress = false;
            static float        progress = 1.0f; // Cheio.
            static int          year = 2023, call = 1;

            ImGui::SameLine();
            if (ImGui::Button(Texts::BUTTON_SEARCH)) {
                Resources::Sounds::playClickSound();

                start_progress = true;
                auto stop_progress = [] { start_progress = false; progress = 1.0f; };

                static std::future<void> task;
                task = std::async(std::launch::async, [stop_progress] { // Para não travar a UI.
                    if (combo_courses_selected_idx == -1) {
                        smaller_text_box_data.setText(Texts::SMALLER_TEXT_BOX_NO_COURSE_SELECTED, Colors::LIGHT_RED.imVec4());
                        stop_progress();
                        return;
                    }
                    if (not are_pdfs_downloaded) {
                        smaller_text_box_data.setText(Texts::SMALLER_TEXT_BOX_DOWNLOADING, Colors::LIGHT_GREEN.imVec4());
                        are_pdfs_downloaded = Anceu::downloadPdfs(year, call); // Retorna true se não falhar.
                        Anceu::convertPdfs();
                    }

                    if (not are_pdfs_downloaded) { // Tentamos baixar acima, mas falhou.
                        smaller_text_box_data.setText(Texts::SMALLER_TEXT_BOX_DOWNLOAD_FAILED, Colors::LIGHT_RED.imVec4());
                        stop_progress();
                        return;
                    }

                    if (ImGui::IsKeyDown(ImGuiKey_Comma)) { // Para testar os cursos.
                        for (auto & i : Texts::COURSES) {
                            if (Anceu::extractGrades(i)) {
                                smaller_text_box_data.setText(Texts::SMALLER_TEXT_BOX_RESULTS);
                                bigger_text_box_text = Anceu::results.c_str();
                                se_button_text = Texts::SE_BUTTON_DETAILS;
                                se_button_disabled = false;
                            }
                            else {
                                smaller_text_box_data.setText(Texts::SMALLER_TEXT_BOX_EXTRACT_FAILED, Colors::LIGHT_RED.imVec4());
                                break;
                            }
                        }
                    }
                    else if (Anceu::extractGrades(Texts::COURSES[combo_courses_selected_idx])) {
                        smaller_text_box_data.setText(Texts::SMALLER_TEXT_BOX_RESULTS);
                        bigger_text_box_text = Anceu::results.c_str();
                        se_button_text = Texts::SE_BUTTON_DETAILS;
                        se_button_disabled = false;
                    }
                    else
                        smaller_text_box_data.setText(Texts::SMALLER_TEXT_BOX_EXTRACT_FAILED, Colors::LIGHT_RED.imVec4());

                    stop_progress();
                });
            }
            
            ImGui::PushStyleColor(ImGuiCol_FrameBg, Colors::DARK_GRAY.imVec4());

            centerAlignNextItems(ImGui::GetWindowWidth() * 0.75f);
            if (ImGui::BeginChildFrame(SmallerTextBoxID, { ImGui::GetWindowWidth() * 0.75f, buttons_height}))
                ImGui::TextColored(smaller_text_box_data.getColor(), smaller_text_box_data.getText());
            ImGui::EndChildFrame();

            static float progress_dir = 2.5f; // Maior = mais rápido.
            if (start_progress) {
                progress += progress_dir * ImGui::GetIO().DeltaTime;
                if (progress >= +1.1f) { progress = +1.1f; progress_dir *= -1.0f; }
                if (progress <= -0.1f) { progress = -0.1f; progress_dir *= -1.0f; }
            }

            centerAlignNextItems(ImGui::GetWindowWidth() * 0.5f);
            ImGui::ProgressBar(progress, { ImGui::GetWindowWidth() * 0.5f, 10 }, "");

            if (ImGui::BeginChildFrame(BiggerTextBoxID, { 0, -(style.ItemSpacing.y + 2 * (3 + style.FramePadding.y) + ImGui::GetFontSize()) }))
                ImGui::TextWrapped("%s", bigger_text_box_text); // Com %s o texto aparentemente não tem limite de carácteres.
            ImGui::EndChildFrame();

            // Permite dar zoom apenas na janela BiggerTextBox.
            static ImGuiIO& io = ImGui::GetIO();
            if (ImGui::IsItemHovered())
                io.FontAllowUserScaling = true;
            else
                io.FontAllowUserScaling = false;
            
            ImGui::PushStyleVar(ImGuiStyleVar_WindowPadding, { 5, 5 });
            ImGui::PushStyleColor(ImGuiCol_Button, Colors::DARK_WINE.imVec4());

            // Ao clicar com o botão direito do mouse/touchpad.
            if (bigger_text_box_text == Anceu::results.c_str() or bigger_text_box_text == Anceu::details.c_str()) {
                ImGui::PushStyleColor(ImGuiCol_PopupBg, Colors::BLACK.imVec4(0));

                if (ImGui::BeginPopupContextItem("Copying Menu")) {
                    if (ImGui::Button(Texts::BUTTON_COPY)) {
                        Resources::Sounds::playClickSound();
                        ImGui::SetClipboardText(bigger_text_box_text);
                        smaller_text_box_data.setText(Texts::SMALLER_TEXT_BOX_COPIED, Colors::LIGHT_GREEN.imVec4());
                        ImGui::CloseCurrentPopup();
                    }
                    ImGui::EndPopup();
                }

                ImGui::PopStyleColor();

                if (ImGui::IsKeyDown(ImGuiKey_ModCtrl) and ImGui::IsKeyDown(ImGuiKey_C)) {
                    Resources::Sounds::playClickSound();
                    ImGui::SetClipboardText(bigger_text_box_text);
                    smaller_text_box_data.setText(Texts::SMALLER_TEXT_BOX_COPIED, Colors::LIGHT_GREEN.imVec4());
                }
            }
            else if (bigger_text_box_text == Texts::BIGGER_TEXT_BOX_INFO) {
                if (ImGui::BeginPopupContextItem("Links Menu")) {
                    auto selectedOption = [](const char* link) {
                        Resources::Sounds::playClickSound();
                        ShellExecuteA(nullptr, "open", link, nullptr, nullptr, SW_SHOWNORMAL);
                        ImGui::CloseCurrentPopup();
                    };

                    if (ImGui::Button(Texts::BUTTON_OPEN1))
                        selectedOption("https://www.cebraspe.org.br/");
                    else if (ImGui::Button(Texts::BUTTON_OPEN2))
                        selectedOption("https://github.com/euyogi/");
                    else if (ImGui::Button(Texts::BUTTON_OPEN3))
                        selectedOption("https://pll.harvard.edu/course/cs50-introduction-computer-science/");
                    else if (ImGui::Button(Texts::BUTTON_OPEN4))
                        selectedOption("https://github.com/euyogi/Projeto-CS50/issues/new/");
                 
                    ImGui::EndPopup();
                }
            }

            ImGui::PopStyleColor();
            ImGui::PopStyleVar();

            tipMarker(Texts::SW_TIP_MARKER, { 0, 3 + style.FramePadding.y / 2.0f });

            static int calls_qnt = 2; static float buttons_years_width = 0.0f;

            ImGui::PushStyleVar(ImGuiStyleVar_ItemSpacing, { 3, 0 });
            
            if (dpi_changed)
                buttons_years_width = calcItemsWidth("202320222021", 3);
            
            ImGui::PushStyleVar(ImGuiStyleVar_FramePadding, { 3, 3 });
            
            ImGui::SetCursorPosX(ImGui::GetCursorPosX() + buttons_height);
            if (ImGui::BeginChildFrame(ButtonsYearsID, { buttons_years_width + 6, buttons_height + 6 })) {
                ImGui::PopStyleVar();
                ImGui::PopStyleColor();

                auto selectedButton = [](int set_call, int set_calls_qnt) {
                    Resources::Sounds::playClickSound();
                    Anceu::deletePdfs();
                    are_pdfs_downloaded = false;
                    call = set_call;
                    calls_qnt = set_calls_qnt;
                };

                if (selectableButton("2023", 2023, &year))
                    selectedButton(1, 2);

                ImGui::SameLine();
                if (selectableButton("2022", 2022, &year))
                    selectedButton(1, 5);

                ImGui::SameLine();
                if (selectableButton("2021", 2021, &year))
                    selectedButton(1, 4);

            }
            ImGui::EndChildFrame();

            ImGui::PopStyleVar();

            static const char* calls[] = { "1ª", "2ª", "3ª", "4ª", "5ª" };
            const char*        combo_calls_preview = calls[call - 1];

            ImGui::SameLine();
            ImGui::SetCursorPosY(ImGui::GetCursorPosY() + 3);
            ImGui::SetNextItemWidth(ImGui::GetFontSize() * 4);
            if (ImGui::BeginCombo("##Calls", combo_calls_preview)) {
                for (int n = 0; n < calls_qnt; n++) {
                    const bool is_selected = (call - 1 == n);
                    if (ImGui::Selectable(calls[n], is_selected)) {
                        call = n + 1;
                        Resources::Sounds::playClickSound();
                        Anceu::deletePdfs();
                        are_pdfs_downloaded = false;
                    }

                    if (is_selected) {
                        ImGui::SetItemDefaultFocus();
                        if (ImGui::IsKeyReleased(ImGuiKey_Enter) or ImGui::IsKeyReleased(ImGuiKey_Space)) {
                            Resources::Sounds::playClickSound();
                            ImGui::FocusItem();
                        }
                    }
                }
                ImGui::EndCombo();
            }

            if (ImGui::IsItemHovered() and ImGui::IsMouseReleased(ImGuiMouseButton_Left))
                Resources::Sounds::playClickSound(); // Ao clicar no combo das chamadas.

            static float se_and_exit_buttons_width = 0.0f;
            if (dpi_changed)
                se_and_exit_buttons_width = calcItemsWidth(se_button_text) + calcItemsWidth(Texts::BUTTON_EXIT);

            ImGui::BeginDisabled(se_button_disabled);
            ImGui::SameLine();
            ImGui::SetCursorPosY(ImGui::GetCursorPosY() + 3);
            rightAlignNextItems(se_and_exit_buttons_width, 2, buttons_height);
            if (ImGui::Button(se_button_text)) {
                Resources::Sounds::playClickSound();
                if (se_button_text == Texts::SE_BUTTON_DETAILS) {
                    se_button_text = Texts::SE_BUTTON_RESULTS;
                    smaller_text_box_data.setText(Texts::SMALLER_TEXT_BOX_DETAILS);
                    bigger_text_box_text = Anceu::details.c_str();
                }
                else {
                    se_button_text = Texts::SE_BUTTON_DETAILS;
                    smaller_text_box_data.setText(Texts::SMALLER_TEXT_BOX_RESULTS);
                    bigger_text_box_text = Anceu::results.c_str();
                }
                se_and_exit_buttons_width = calcItemsWidth(se_button_text) + calcItemsWidth(Texts::BUTTON_EXIT);
            }
            ImGui::EndDisabled();

            ImGui::PushStyleColor(ImGuiCol_Button, Colors::RED.imVec4());
            ImGui::PushStyleColor(ImGuiCol_ButtonHovered, Colors::DARK_RED.imVec4());
            ImGui::PushStyleColor(ImGuiCol_ButtonActive, Colors::DARKEST_RED.imVec4());

            ImGui::SameLine();
            ImGui::SetCursorPosY(ImGui::GetCursorPosY() + 3);
            if (ImGui::Button(Texts::BUTTON_EXIT)) // Não precisa chamar o som, pois vai ser chamado ao terminar o aplicativo em main.cpp.
                *p_loop_boolean = true; // True = terminar aplicativo.

            ImGui::PopStyleColor(3);
        }
        ImGui::EndChild();

        ImGui::SameLine();
        if (ImGui::BeginChild("Inner Right Frame", { 0, 0 }, false, child_flags)) {
            static float label_converter_width = 0.0f;
            if (dpi_changed)
                label_converter_width = calcItemsWidth(Texts::LABEL_CONVERTER);

            ImGui::PushStyleColor(ImGuiCol_FrameBg, Colors::DARK_GRAY.imVec4());
            ImGui::PushStyleColor(ImGuiCol_FrameBgHovered, Colors::DARK_GRAY.imVec4());
            ImGui::PushStyleColor(ImGuiCol_FrameBgActive, Colors::DARK_GRAY.imVec4());

            centerAlignNextItems(label_converter_width);
            if (ImGui::BeginChildFrame(LabelConverterID, { label_converter_width, buttons_height }))
                ImGui::Text(Texts::LABEL_CONVERTER);
            ImGui::EndChildFrame();

            ImGui::PopStyleColor(3);

            float before = ImGui::GetCursorPosY();

            ImGui::SameLine();
            tipMarker(Texts::NE1_TIP_MARKER, { 0, style.FramePadding.y / 2.0f }, "?##1");

            static float label_group_width = 0.0f;
            if (dpi_changed)
                label_group_width = ImGui::CalcTextSize(Texts::LABEL_GROUP).x;

            float equal_items_spacing = (ImGui::GetWindowHeight() - (2 * ImGui::GetFontSize() + style.ItemSpacing.y + 10 * ImGui::GetFrameHeightWithSpacing() + 2 * style.WindowPadding.y)) / 3.0f;

            ImGui::SetCursorPosY(before + equal_items_spacing);
            centerAlignNextItems(label_group_width);
            ImGui::Text(Texts::LABEL_GROUP);

            before = ImGui::GetCursorPosY();
            
            ImGui::SameLine();
            tipMarker(Texts::NE2_TIP_MARKER, { 0, -style.FramePadding.y / 2.0f }, "?##2");

            static float radio1_width = 0.0f;
            if (dpi_changed)
                radio1_width = 2 * style.FramePadding.y + style.ItemInnerSpacing.x + ImGui::CalcTextSize(Texts::RADIO1).x;

            static int group = 1;

            ImGui::SetCursorPosY(before);
            centerAlignNextItems(radio1_width);
            if (ImGui::RadioButton(Texts::RADIO1, &group, 1))
                Resources::Sounds::playClickSound();
            centerAlignNextItems(radio1_width);
            if (ImGui::RadioButton(Texts::RADIO2, &group, 2))
                Resources::Sounds::playClickSound();

            static float label_grades_width = 0.0f;
            if (dpi_changed)
                label_grades_width = ImGui::CalcTextSize(Texts::LABEL_GRADES).x;

            ImGui::SetCursorPosY(ImGui::GetCursorPosY() + equal_items_spacing);
            centerAlignNextItems(label_grades_width);
            ImGui::Text(Texts::LABEL_GRADES);
            
            struct TextProc {
                static void handlePoint(ImGuiInputTextCallbackData* data) {
                    if (data->BufTextLen == 0) // Vazio = sem ponto.
                        return;

                    if (data->Buf[data->BufTextLen - 1] == '.') // O último caráctere é um ponto = sem ponto.
                        data->Buf[data->BufTextLen - 1] = '\0';

                    float num = std::stof(data->Buf);
                    
                    if (num >= 10000) // No caso de digitar 123.45 e tentar apagar o ponto.
                        num *= 0.01f;
                    if (num >= 1000) { // Momento do ponto.
                        num *= 0.1f;
                        ++data->CursorPos; // Adicionamos um caractére (o ponto) cursor avança uma posição.
                    }
                                        
                    std::string str = std::format("{:g}", num); // g põe ponto e ignora zeros após o ponto.
                    memcpy(data->Buf, str.c_str(), str.size() + 1);
                    data->BufTextLen = static_cast<int>(str.size());
                    data->BufDirty = true;
                }

                static int onlyNumbers(ImGuiInputTextCallbackData* data) {
                    if (data->EventChar >= '0' and data->EventChar <= '9')
                        return 0;

                    return 1; // 1 = Desconsiderar caráctere.
                }

                static int gradeProc(ImGuiInputTextCallbackData* data) {
                    if (data->EventFlag == ImGuiInputTextFlags_CallbackCharFilter)
                        return onlyNumbers(data);

                    if (data->EventFlag == ImGuiInputTextFlags_CallbackEdit)
                        handlePoint(data);

                    return 0;
                }
            };

            ImGui::PushStyleColor(ImGuiCol_FrameBg, Colors::DARK_GRAY.imVec4());
            ImGui::PushStyleColor(ImGuiCol_FrameBgHovered, Colors::DARK_GRAY.imVec4());
            ImGui::PushStyleColor(ImGuiCol_FrameBgActive, Colors::DARK_GRAY.imVec4());

            ImGuiInputTextFlags input_flags = ImGuiInputTextFlags_EnterReturnsTrue | ImGuiInputTextFlags_CallbackCharFilter | ImGuiInputTextFlags_CallbackEdit;
            static char  buf1[7] = "", buf2[7] = "", buf3[7] = "", buf4[7] = "", buf5[7] = "";
            static float input_width = 0.0f;
            static float label_literature_width = ImGui::CalcTextSize(Texts::LABEL_LITERATURE).x;
            
            if (dpi_changed) {
                input_width = calcItemsWidth("000.00");
                label_literature_width = ImGui::CalcTextSize(Texts::LABEL_LITERATURE).x;
            }

            centerAlignNextItems(label_literature_width + style.ItemSpacing.x + input_width);
            ImGui::AlignTextToFramePadding(); ImGui::Text(Texts::LABEL_LITERATURE); ImGui::SameLine();
            static float align_pos_x = 0.0f; if (dpi_changed) align_pos_x = ImGui::GetCursorPosX();
            ImGui::SetNextItemWidth(input_width);
            if (ImGui::InputTextWithHint("##Literature", "000.00", buf1, 7, input_flags, TextProc::gradeProc))
                ImGui::SetKeyboardFocusHere();

            centerAlignNextItems(label_literature_width + style.ItemSpacing.x + input_width);
            ImGui::AlignTextToFramePadding(); ImGui::Text(Texts::LABEL_HUMANITIES); ImGui::SameLine(); ImGui::SetCursorPosX(align_pos_x);
            ImGui::SetNextItemWidth(input_width);
            if (ImGui::InputTextWithHint("##Humanities", "000.00", buf2, 7, input_flags, TextProc::gradeProc))
                ImGui::SetKeyboardFocusHere();

            centerAlignNextItems(label_literature_width + style.ItemSpacing.x + input_width);
            ImGui::AlignTextToFramePadding(); ImGui::Text(Texts::LABEL_NATURE); ImGui::SameLine(); ImGui::SetCursorPosX(align_pos_x);
            ImGui::SetNextItemWidth(input_width); 
            if (ImGui::InputTextWithHint("##Nature", "000.00", buf3, 7, input_flags, TextProc::gradeProc))
                ImGui::SetKeyboardFocusHere();

            centerAlignNextItems(label_literature_width + style.ItemSpacing.x + input_width);
            ImGui::AlignTextToFramePadding(); ImGui::Text(Texts::LABEL_MATH); ImGui::SameLine(); ImGui::SetCursorPosX(align_pos_x);
            ImGui::SetNextItemWidth(input_width);
            if (ImGui::InputTextWithHint("##Math", "000.00", buf4, 7, input_flags, TextProc::gradeProc))
                ImGui::SetKeyboardFocusHere();

            centerAlignNextItems(label_literature_width + style.ItemSpacing.x + input_width);
            ImGui::AlignTextToFramePadding(); ImGui::Text(Texts::LABEL_ESSAY); ImGui::SameLine(); ImGui::SetCursorPosX(align_pos_x);
            ImGui::SetNextItemWidth(input_width);
            if (ImGui::InputTextWithHint("##Essay", "000.00", buf5, 7, input_flags, TextProc::gradeProc))
                ImGui::SetKeyboardFocusHere();

            static float button_convert_width = 0.0f, grade = 0.0f;
            if (dpi_changed)
                button_convert_width = calcItemsWidth(Texts::BUTTON_CONVERT);
            
            static bool button_convert_disabled = true;
            if (buf1[0] && buf2[0] && buf3[0] && buf4[0] && buf5[0])
                button_convert_disabled = false;
            else {
                button_convert_disabled = true;
                grade = 0.0f;
            }

            ImGui::BeginDisabled(button_convert_disabled);
            ImGui::SetCursorPosY(ImGui::GetCursorPosY() + equal_items_spacing);
            centerAlignNextItems(button_convert_width);
            if (ImGui::Button(Texts::BUTTON_CONVERT)) {
                Resources::Sounds::playClickSound();
                int weight1 = (group == 1 ? 4 : 2);
                int weight2 = (group == 1 ? 2 : 4);
                grade = (weight1 * (std::stof(buf1) + std::stof(buf2)) + weight2 * (std::stof(buf3) + std::stof(buf4)) + std::stof(buf5)) / 13.0f;
            }
            ImGui::EndDisabled();

            centerAlignNextItems(label_literature_width + style.ItemSpacing.x + input_width);
            ImGui::AlignTextToFramePadding(); ImGui::Text(Texts::LABEL_FINAL); ImGui::SameLine(); ImGui::SetCursorPosX(align_pos_x);
            if (ImGui::BeginChildFrame(ConversionTextBoxID, { input_width, buttons_height }))
                ImGui::TextColored(grade == 0.0f ? style.Colors[ImGuiCol_TextDisabled] : style.Colors[ImGuiCol_Text], std::format("{:06.2f}", grade).c_str());
            ImGui::EndChildFrame();

            ImGui::PopStyleColor(3);
        }
        ImGui::EndChild();
    }
    ImGui::End();

    if (dpi_changed)
        dpi_changed = false;

    //ImGui::ShowDemoWindow();
}

void UI::setWndStyle(HWND hWnd) {
    COLORREF DARK_WINE = Colors::DARK_WINE.colorRef(); // Cor de fundo da barra superior da janela.
    constexpr int DWMWA_CAPTION_COLOR = 35; // dwmapi.h está desatualizado no mingw, e não contém dwmwa_caption_color.
    DwmSetWindowAttribute(hWnd, DWMWA_CAPTION_COLOR, &DARK_WINE, sizeof(DARK_WINE));

    ImGuiIO& io = ImGui::GetIO();
    io.IniFilename = nullptr; // Desativa o arquivo .ini.

    // Adiciona dois carácteres especiais que aparecem no programa.
    ImVector<ImWchar> ranges;
    ImFontGlyphRangesBuilder builder;
    builder.AddRanges(io.Fonts->GetGlyphRangesDefault());
    builder.AddText("–≤");
    builder.BuildRanges(&ranges);
    io.Fonts->AddFontFromMemoryCompressedTTF(Resources::Fonts::ubuntu_mono_r_data, Resources::Fonts::ubuntu_mono_r_size, FONT_SIZE, nullptr, ranges.Data);
    io.Fonts->Build();

    ImGuiStyle& style = ImGui::GetStyle();
    
    style.HoverFlagsForTooltipMouse = ImGuiHoveredFlags_DelayNone;
    style.HoverFlagsForTooltipNav = ImGuiHoveredFlags_DelayNone;
    style.PopupBorderSize = 0;

    style.WindowRounding = 5;
    style.FrameRounding = style.WindowRounding;
    style.PopupRounding = style.WindowRounding;
    style.ChildRounding = style.WindowRounding * 2;
    style.ItemSpacing = { 10, 15 };

    style.Colors[ImGuiCol_NavHighlight] = Colors::LIGHTEST_WINE.imVec4();
    style.Colors[ImGuiCol_Text] = Colors::LIGHTEST_GRAY.imVec4();
    style.Colors[ImGuiCol_ChildBg] = Colors::DARK_GRAY_WINE.imVec4();

    style.Colors[ImGuiCol_Button] = Colors::WINE.imVec4();
    style.Colors[ImGuiCol_ButtonHovered] = Colors::LIGHT_WINE.imVec4();
    style.Colors[ImGuiCol_ButtonActive] = Colors::LIGHTEST_WINE.imVec4();

    // Combo
    style.Colors[ImGuiCol_FrameBg] = Colors::WINE.imVec4();
    style.Colors[ImGuiCol_FrameBgHovered] = Colors::LIGHT_WINE.imVec4();
    style.Colors[ImGuiCol_FrameBgActive] = Colors::LIGHTEST_WINE.imVec4();

    // Combo items
    style.Colors[ImGuiCol_Header] = Colors::LIGHTEST_WINE.imVec4();
    style.Colors[ImGuiCol_HeaderHovered] = Colors::LIGHT_WINE.imVec4();
    style.Colors[ImGuiCol_HeaderActive] = Colors::LIGHTEST_WINE.imVec4();

    // Combo bg
    style.Colors[ImGuiCol_PopupBg] = Colors::DARK_WINE.imVec4();

    style.Colors[ImGuiCol_ScrollbarBg] = Colors::DARK_GRAY_WINE.imVec4();
    style.Colors[ImGuiCol_ScrollbarGrab] = Colors::GRAY.imVec4();
    style.Colors[ImGuiCol_ScrollbarGrabHovered] = Colors::LIGHT1_GRAY.imVec4();
    style.Colors[ImGuiCol_ScrollbarGrabActive] = Colors::LIGHT2_GRAY.imVec4();

    // Progresso.
    style.Colors[ImGuiCol_PlotHistogram] = Colors::LIGHTEST_WINE.imVec4();

    style.Colors[ImGuiCol_CheckMark] = Colors::DARK_GRAY_WINE.imVec4();
}

// Calcula e atualiza os Paddings.
void UI::updateWndPaddings(HWND hWnd) {
    POINT top_left_coord = { 0, 0 };
    ClientToScreen(hWnd, &top_left_coord);
    RECT wnd_coords;
    GetWindowRect(hWnd, &wnd_coords);
    padding = static_cast<float>(top_left_coord.y - wnd_coords.top);

    ImGuiIO& io = ImGui::GetIO();
    float dpi_scale = getDpiScale();
    io.FontGlobalScale = dpi_scale;

    ImGuiStyle& style = ImGui::GetStyle();
    float window_padding = ceilf(padding * 0.75f);
    style.WindowPadding = { window_padding, window_padding };
    style.FramePadding = { 15 * dpi_scale, (buttons_height - FONT_SIZE * dpi_scale) / 2.0f};
    style.ScrollbarSize = 15 * dpi_scale;
    
    dpi_changed = true;
}

// Widgets que se comportam como botões radiais, mas tem o design padrão de um botão e retornam true ao serem clicados.
bool selectableButton(const char* label, int id, int* selected_id) {
    bool selected = false;
    if (*selected_id == id)
        selected = true;

    if (not selected)
        ImGui::PushStyleColor(ImGuiCol_Button, Colors::GRAY.imVec4());
    bool clicked = ImGui::Button(label);
    if (not selected) {
        if (clicked)
            *selected_id = id;

        ImGui::PopStyleColor();
    }

    return clicked;
}

// Widgets para dicas/ajuda, podem, opcionalmente, se comportarem como botões.
bool tipMarker(const char* text, ImVec2 offset, const char* symbol, bool is_button) {
    ImVec2 before = ImGui::GetCursorPos();
    ImGui::SetCursorPos({ before.x + offset.x, before.y + offset.y });

    float tip_height = buttons_height * 0.80f;

    ImGui::PushStyleVar(ImGuiStyleVar_FrameBorderSize, 2);
    ImGui::PushStyleVar(ImGuiStyleVar_FramePadding, { 0, (tip_height - ImGui::GetFontSize()) / 2.0f});
    ImGui::PushStyleColor(ImGuiCol_Button, Colors::BLACK.imVec4(0));
    ImGui::PushStyleColor(ImGuiCol_Text, Colors::LIGHT2_GRAY.imVec4());

    bool clicked = false;

    if (is_button)
        clicked = ImGui::Button(symbol, { tip_height, tip_height });

    else {
        ImGui::PushStyleColor(ImGuiCol_ButtonActive, Colors::BLACK.imVec4(0));
        ImGui::PushStyleColor(ImGuiCol_ButtonHovered, Colors::BLACK.imVec4(0));
        ImGui::Button(symbol, { tip_height, tip_height });
    }

    ImGui::PopStyleColor(is_button ? 2 : 4);
    ImGui::PopStyleVar(2);

    ImGui::PushStyleVar(ImGuiStyleVar_WindowPadding, { 20, 10 });
    ImGui::PushStyleColor(ImGuiCol_PopupBg, Colors::LIGHT_WINE.imVec4());
    ImGui::SetItemTooltip(text);
    ImGui::PopStyleColor();
    ImGui::PopStyleVar();

    ImGui::SetCursorPos(before);

    return clicked;
}

// Se for calcular mais de um item: labels = concatenação dos n labels.
float calcItemsWidth(const char* labels, int items_qnt) {
    ImGuiStyle& style = ImGui::GetStyle();
    return ImGui::CalcTextSize(labels).x + items_qnt * 2 * style.FramePadding.x + (items_qnt - 1) * style.ItemSpacing.x;
}

void centerAlignNextItems(float items_width, int items_qnt) {
    ImGuiStyle& style = ImGui::GetStyle();
    ImGui::SetCursorPosX((ImGui::GetWindowSize().x - items_width - (items_qnt - 1) * style.ItemSpacing.x) / 2.0f);
}

// Se for calcular mais de um item: items_width = soma dos comprimentos.
void rightAlignNextItems(float items_width, int items_qnt, float opt_padding) {
    ImGuiStyle& style = ImGui::GetStyle();
    ImGui::SetCursorPosX(ImGui::GetWindowSize().x - style.WindowPadding.x - items_width - (items_qnt - 1) * style.ItemSpacing.x - opt_padding);
}

// Para o combo filter.
const char* itemGetter(std::span<const char* const> items, int index) {
    if (index >= 0 && index < (int)items.size()) {
        return items[index];
    }
    return "";
}

float UI::getDpiScale() {
    return padding / 38.0f;
}
