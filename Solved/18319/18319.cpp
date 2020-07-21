// Problem No.: 18319
// Solver:      Jinmin Goh
// Date:        20200720
// URL: https://www.acmicpc.net/problem/18319

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

// solution: http://www.usaco.org/current/data/sol_berries_silver_jan20.html

int mod;

bool cmp(int a, int b) {
	return (a % mod) > (b % mod);
}

int main() {
    int n, k, maxVal = 0, ans = 0;
    vector<int> nums;
    scanf("%d %d", &n, &k);
    for(int i = 0; i < n; i++) {
        int temp;
        scanf("%d", &temp);
        nums.push_back(temp);
        maxVal = max(maxVal, temp);
    }

    sort(nums.begin(), nums.end());
    
    // all removed berries are same or more than b berries

    for(int b = 1; b <= maxVal; b++) {
		int bucketCnt = 0;   // number of buckets filled
        // count buckets filled with 'b' berries
		for(int i = 0; i < n; i++) {
			bucketCnt += nums[i] / b;
        }

		// found answer
        if(bucketCnt < k / 2) {
			break;
        }
        // buckets more than k
		if(bucketCnt >= k)
		{
			ans = max(ans, b * (k / 2));
			continue;
		}
        
        // buckets less than k, same or more than k / 2
		mod = b;
		sort(nums.begin(), nums.end(), cmp);
		
        int cur = b * (bucketCnt - k / 2);
		for(int i = 0; i < n && i + bucketCnt < k; i++)
			cur += nums[i] % b;
		ans = max(ans, cur);
	}

    printf("%d", ans);

    return 0;
}