// SET-5
#include <iostream>
using namespace std;

int main() {
    string s;
    cin >> s;

    if (s.find("aaa") != string::npos)
        cout << "Accepted\n";
    else
        cout << "Rejected\n";
}
