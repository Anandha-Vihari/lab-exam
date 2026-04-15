// SET-1
#include <iostream>
#include <vector>
#include <cctype>
using namespace std;

vector<string> prod;
vector<char> result;

void findFirst(char c) {
    if (!isupper(c)) {
        result.push_back(c);
        return;
    }
    for (auto p : prod) {
        if (p[0] == c) {
            if (p[2] == '#') result.push_back('#');
            else findFirst(p[2]);
        }
    }
}

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        string s; cin >> s;
        prod.push_back(s);
    }
    char symbol; cin >> symbol;
    findFirst(symbol);

    cout << "FIRST(" << symbol << ") = { ";
    for (char c : result) cout << c << " ";
    cout << "}\n";

    string s; cin >> s;
    if (s.back() == '0') cout << "Even\n";
    else cout << "Odd\n";
}
