class Solution {
public:
    vector<vector<int>> Graph;
    vector<int> parArray;
    vector<i64> price;

    void build_parArray(int u, int par) {
        for (int v : Graph[u]) if (v != par) {
            parArray[v] = u;
            build_parArray(v, u);
        }
    }

    vector<i64> dpUpArr;
    vector<vector<pair<i64,int>>> dpUpHelper;

    i64 dpUp(int u) {
        if (u == 0) return price[0];
        if (dpUpArr[u] != -1) return dpUpArr[u];

        i64 res1 = 0;

        if (dpUpHelper[parArray[u]][0].second != u) {
            res1 = dpUpHelper[parArray[u]][0].first;
        }
        else {
            if (len(dpUpHelper[parArray[u]]) >= 2) {
                res1 = dpUpHelper[parArray[u]][1].first;
            }
        }

        /*for (int v : Graph[parArray[u]]) if (v != parArray[parArray[u]]) {
            bool goDownAgain = v == u;
            if (!goDownAgain)
                res1 = max(res1, price[parArray[v]] + dpDown(v));
        }*/

        res1 += price[u];

        i64 res2 = 0;
        res2 = price[u] + dpUp(parArray[u]);

        return dpUpArr[u] = max(res1, res2);
    }
    
    vector<i64> dpDownArr;
    i64 dpDown(int u) {
        if (dpDownArr[u] != -1) return dpDownArr[u];

        i64 res = 0;
        for (int v : Graph[u]) if (v != parArray[u]) {
            res = max(res, dpDown(v));
        }

        return dpDownArr[u] = price[u] + res;
    }

    i64 maxOutput(int N, vector<vector<int>>& edges, vector<int>& price) {
        Graph.resize(N);

        for (vector<int>& e : edges) {
            Graph[e[0]].push_back(e[1]);
            Graph[e[1]].push_back(e[0]);
        }

        parArray = vector<int>(N, -1);
        build_parArray(0, -1);

        this->price.resize(N);
        for (int i = 0; i < N; i++) {
            this->price[i] = price[i];
        }

        dpUpArr = dpDownArr = vector<i64>(N, -1);
        dpUpHelper.resize(N);

        for (int u = 0; u < N; u++) {
            for (int v : Graph[u]) if (v != parArray[u]) {
                dpUpHelper[u].push_back({price[parArray[v]] + dpDown(v), v});
            }

            sort(ALL(dpUpHelper[u]), greater<pair<i64,int>>());
        }

        i64 res = 0;
        for (int u = 0; u < N; u++) {
            i64 longestPath = max(dpUp(u), dpDown(u));
            i64 priceSum = longestPath - price[u];
            res = max(res, priceSum);
        }

        return res;
    }
};