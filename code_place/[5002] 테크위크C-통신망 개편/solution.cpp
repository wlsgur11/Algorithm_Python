#include <bits/stdc++.h>
#define all(x) x.begin(), x.end()
using ll = long long;
using namespace std;
struct edge{
    int u, v; ll w;
    edge(): u(0), v(0), w(0LL) {}
    edge(int u, int v, ll w): u(u), v(v), w(w) {}
};
int parent[100001];
int find(int x){
    if (x == parent[x]) return x;
    return parent[x] = find(parent[x]);
}
bool merge(int a, int b){
    a = find(a), b = find(b);
    if (a == b) return false;
    if (a > b) swap(a, b);
    parent[b] = a;
    return true;
}
ll kruskal(vector<edge>& vec){
    ll sum = 0;
    for (auto& [u, v, w]: vec){
        if (merge(u, v))    sum += w;
    }
    return sum;
}
int main() {
    cin.tie(0); ios_base::sync_with_stdio(false);
    ll n, m, k; cin >> n >> m >> k;
    ll answer = 0;
    iota(parent, parent + n + 1, 0);
    vector<edge> conedge(m);
    vector<edge> canedge(k);
    for (auto& [u, v, w]: conedge) cin >> u >> v >> w, answer += w;
    for (auto& [u, v, w]: canedge) cin >> u >> v >> w;
    sort(all(conedge), [](edge x, edge y){
        return x.w > y.w;
    });
    sort(all(canedge), [](edge x, edge y){
        return x.w < y.w;
    });
    cout << answer - kruskal(conedge) + kruskal(canedge);
    return 0;
}
​