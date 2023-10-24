#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<float> people_queue(n);
    for (int i = 0; i < n; i++) {
        cin >> people_queue[i];
    }

    vector<int> closest_age(n, -1);
    stack<int> s;

    for (int i = n - 1; i >= 0; i--) {
        while (!s.empty() && people_queue[i] < people_queue[s.top()]) {
            closest_age[s.top()] = static_cast<int>(people_queue[i]);
            s.pop();
        }
        s.push(i);
    }

    for (int age : closest_age) {
        cout << age << " ";
    }
    cout << endl;

    return 0;
}

