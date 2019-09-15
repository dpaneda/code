#include <iostream>
#include <cstdio>
#include <string>
#include <sstream>
#include <vector>
#include <regex>
#include <algorithm>

using namespace std;

/*
vector<int> read_ints() {
	int i;
	string input;
	vector<int> vi;

	getline(cin, input);
	stringstream stream(input);

	while (myStream >> i) {
		vi.push_back(i);
	} 
	
	return vi;
}
*/

int main() {
	int L, D, N;
	scanf("%d %d %d\n", &L, &D, &N);
	
	string s;
	vector<string> words;
	vector<regex> cases;

	while (D--) {
		getline(cin, s);
		words.push_back(s);
	}

	while (N--) {
		getline(cin, s);
		replace(s.begin(), s.end(), '(', '[');
		replace(s.begin(), s.end(), ')', ']');
		cases.push_back(regex(s));
	}

	for (int i = 0; i < cases.size(); i++) {
		regex &r = cases[i];
		int n = 0;
		for(string &w : words) {
			if (regex_match(w, r)) {
				n++;
			}
		}
		cout <<"Case #" <<i + 1 <<": " <<n <<endl;
	}	
}
