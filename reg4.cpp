#include <regex>
#include <iostream>

int main()
{
    const std::string s = "/home/toto/FILE_mysymbol_EVENT.DAT";
    std::regex rgx(".*FILE_(\\w+)_EVENT\\.DAT.*");
    std::smatch match;

    if (std::regex_search(s.begin(), s.end(), match, rgx))
        std::cout << "match: " << match[1] << '\n';
}
