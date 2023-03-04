#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t){
        int n;
        cin >> n;
        vector<int> A(101, 0);
        vector<int> count(101, 0);

        for (int i = 0; i < n; i++){
            cin >> A[i];
            count[A[i]] += 1;
        }

        int val = -1;
        for (int i = 0; i <= 100; i++){
            if (count[i] == 1){
                val = i;
                break;
            }
        }

        for (int i = 0; i < n; i ++){
            if (val == A[i]){
                cout << i + 1 << '\n';
                break;
            }
        }

        t--;
    } 

}


