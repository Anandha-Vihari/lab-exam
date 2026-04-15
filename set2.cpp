// SET-2
#include <iostream>
using namespace std;

string input;
int i = 0;

void S();
void L();

void S() {
    if (input[i] == 'a') i++;
    else if (input[i] == '(') {
        i++; L();
        if (input[i] == ')') i++;
        else cout << "Error\n";
    } else cout << "Error\n";
}

void L() {
    S();
    while (input[i] == ',') {
        i++; S();
    }
}

int main() {
    cin >> input;
    S();

    if (input[i] == '\0') cout << "Accepted\n";
    else cout << "Rejected\n";

    string s; cin >> s;
    if (s.back() == '0') cout << "Even\n";
    else cout << "Odd\n";
}
