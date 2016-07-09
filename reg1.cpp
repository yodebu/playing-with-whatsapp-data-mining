#include <iostream>
#include <regex>
using namespace std;

int main()
{
    regex r1("S");
    printf("S works.\n");
    regex r2(".");
    printf(". works.\n");
    regex r3(".+");
    printf(".+ works.\n");
    regex r4("[0-9]");
    printf("[0-9] works.\n");
    return 0;
}
