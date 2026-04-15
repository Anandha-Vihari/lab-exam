// SET-3
#include <iostream>
using namespace std;

string input;
int i = 0;

void E(); void Eprime(); void T(); void Tprime(); void F();

void E() { T(); Eprime(); }

void Eprime() {
    if (input[i] == '+') {
        i++; T(); Eprime();
    }
}

void T() { F(); Tprime(); }

void Tprime() {
    if (input[i] == '*') {
        i++; F(); Tprime();
    }
}

void F() {
    if (input[i] == '(') {
        i++; E();
        if (input[i] == ')') i++;
        else cout << "Error\n";
    }
    else if (input[i] == 'i' && input[i+1] == 'd') i += 2;
    else cout << "Error\n";
}

int main() {
    cin >> input;
    E();

    if (input[i] == '\0') cout << "Accepted\n";
    else cout << "Rejected\n";

    string s; cin >> s;
    if (s.length() >= 3 && s[s.length()-3] == 'a')
        cout << "Accepted\n";
    else cout << "Rejected\n";
}
