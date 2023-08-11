#pragma once

#define IDI_ICON 101

namespace Resources {
	namespace Fonts {
		extern const int ubuntu_mono_r_size;
		extern const unsigned int ubuntu_mono_r_data[150392 / 4];
	}
	namespace Sounds {
		// Toca o som click_sound em sounds.cpp.
		void playClickSound(bool async = true);
		extern const unsigned int click_sound_data[26100 / 4];
	}
}