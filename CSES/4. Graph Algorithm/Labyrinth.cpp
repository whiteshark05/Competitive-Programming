#include <bits/stdc++.h>
using namespace std;

int n, m;

vector<string> a;

string bfs(int r, int c) {
    queue<tuple<int, int, string>> q;
    q.push(make_tuple(r, c, " "));
    a[r][c] = '#';

    while (!q.empty()) {
        tie(r, c, string_path) = q.front();
        q.pop();

        for (auto [dr, dc, direction] : vector<vector<int>>{{0, -1, 'L'}, {0, 1, 'R'}, {-1, 0, 'U'}, {1, 0, 'D'}}) {
            int row = r + dr;
            int col = c + dc;
            string new_path = string_path + direction;
            if (0 <= row && row < n && 0 <= col && col < m && a[row][col] != '#') {
                if (a[row][col] == 'B') {
                    return new_path;
                }
                else if (a[row][col] == '.') {
                    q.push(make_tuple(row, col, new_path));
                    a[row][col] = '#';
                }
            }
        }
    }

    return "";
}

void solve() {
    string path = "";
    for (int r = 0; r < n; r++) {
        for (int c = 0; c < m; c++) {
            if (a[r][c] == 'A') {
                path = bfs(r, c);
                break;
            }
        }
    }

    if (path.empty()) {
        cout << "NO\n";
    }
    else {
        cout << "YES\n" << path.size() << "\n" << path << "\n";
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        a.push_back(s);
    }

    solve();

    return 0;
}