// SET-4
#include <iostream>
using namespace std;

int main() {
    string s;
    cin >> s;

    int n = s.length();
    if (n >= 2 && s[n-1]=='0' && s[n-2]=='0')
        cout << "Accepted\n";
    else
        cout << "Rejected\n";

    if (s.back() == '1')
        cout << "Odd\n";
    else
        cout << "Even\n";
}
