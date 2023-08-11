#pragma once

#include <string>

namespace Anceu {
	extern std::string results;
	extern std::string details;

	bool downloadPdfs(int year, int call);
	void deletePdfs();
	bool convertPdfs();
	bool extractGrades(const char* course);
}