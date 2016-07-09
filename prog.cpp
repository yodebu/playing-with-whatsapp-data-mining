#include<iostream>
#include<fstream>

using namespace std;


string textchecker(string line)
{
    std::regex rgx(".*FILE_(\\w+)_EVENT\\.DAT.*");
    std::smatch match;


    if (std::regex_search(s.begin(), s.end(), match, rgx))
        std::cout << "match: " << match[1] << '\n';




}


int main()
{
    string line;
    ifstream myfile ("data.txt");
    ofstream outfile("output.csv");
    if (myfile.is_open())
    {
        while ( getline (myfile,line) )
        {
            // cout << line << '\n';
            outfile<<line<<endl;
        }
        myfile.close();
    }
    else
    cout<<"No File!"<<endl;


    cout<<"bye!";
}
