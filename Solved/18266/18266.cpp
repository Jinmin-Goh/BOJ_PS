// Problem No.: 18266
// Solver:      Jinmin Goh
// Date:        20200722
// URL: https://www.acmicpc.net/problem/18266

#include <iostream>
#include <cstdlib>
#include <list>
#include <array>
#include <atomic>
#include <algorithm>
#include <deque>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <valarray>
#include <vector>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
using namespace std;

int n, L;
vector<int> x, w, d; // 좌표 순으로 정렬
bool cmp(const int i, const int j){return x[i] < x[j];}

int determineT(){
	int weightSum = 0;
	vector<int> leftCows, rightCows;
	for(int i = 0; i < n; i++){
		if(d[i] == -1) leftCows.push_back(x[i]);
		else rightCows.push_back(x[i]);
	}
	vector<pair<int, int>> remainDistance;
	for(int i = 0; i < leftCows.size(); i++) {
        remainDistance.push_back({leftCows[i], w[i]});
    }
	for(int i = 0; i < rightCows.size(); i++) {
        remainDistance.push_back({L - rightCows[i], w[(int)leftCows.size() + i]});
    }
	sort(remainDistance.begin(), remainDistance.end());
	for(int i = 0; i < remainDistance.size(); i++) {
        weightSum += remainDistance[i].second;
    }
	for(int i = 0; i < remainDistance.size(); i++) {
		weightSum -= 2 * remainDistance[i].second;
		if(weightSum <= 0) {
            return remainDistance[i].first;
        }
	}
}

int main(){
    scanf("%d %d", &n, &L);
	x = vector<int>(n), w = vector<int>(n), d = vector<int>(n);
	for(int i = 0; i < n; i++) {
        scanf("%d %d %d", &w[i], &x[i], &d[i]);
    }
	vector<int> indrs;
	for(int i = 0; i < n; i++) {
        indrs.push_back(i); // iota(indrs.begin(), 0);
    }
	sort(indrs.begin(), indrs.end(), cmp);
	vector<int> X, W, D;
	for(auto tmp : indrs){
		X.push_back(x[tmp]);
		W.push_back(w[tmp]);
		D.push_back(d[tmp]);
	}
	swap(x, X); swap(w, W); swap(d, D);

	int t = determineT(), ans = 0;
	queue<int> rightCows;
	for(int i = 0; i < n; i++){
		if(d[i] == -1){
			while(!rightCows.empty() && rightCows.front() + 2 * t < x[i]) rightCows.pop();
			ans += (int) rightCows.size();
		}
		else rightCows.push(x[i]);
	}
	cout << ans << endl;
    return 0;
}