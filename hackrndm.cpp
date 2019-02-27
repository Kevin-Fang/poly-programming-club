#include <iostream>
#include <unordered_set>
#include <iterator>

using namespace std;
int main() {
	int n, k;
	cin >> n >> k;

	//	cout << "n: " << n << ", k: " << k << endl;
	unordered_set<int> numbers;
	
	int number;
	for (size_t i = 0; i < n; i++) {
		cin >> number;
		numbers.insert(number);
	}
	unordered_set<int>::iterator it;
	int numPairs = 0;
	for (it = numbers.begin(); it != numbers.end(); ++it) {
		if (numbers.count(*it - k) != 0) {
			numPairs++;	
		}
		if (numbers.count(*it + k) != 0) {
			numPairs++;
		}
	}
	cout << numPairs / 2 << endl;
}
