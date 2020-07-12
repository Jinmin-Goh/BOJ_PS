# Problem No.: 18323
# Solver:      Jinmin Goh
# Date:        20200710
# URL: https://www.acmicpc.net/problem/18323

import sys

def main():
    n = int(input())
    nums = list(map(int, sys.stdin.readline().split()))

    # b_i = a_i + a_(i + 1)
    # b is given, regenerate permutation a

    # backtracking
    ans = [None] * n
    numSet = set([_ + 1 for _ in range(n)])

    print(nums, numSet)

    def backtrack(_ans: [int]) -> bool:
        print(_ans)
        # found answer
        if not numSet:
            return True
        if len(numSet) == 1:
            temp = max(numSet)
            for i in range(n):
                if _ans[i] == None:
                    _ans[i] = temp
                return True

        temp = max(numSet)
        ansFlag = False
        for i in range(n - 1):
            if nums[i] > temp and temp * 2 != nums[i]:
                print("i:", i, "nums[i]:", nums[i], "temp:", temp)
                # both empty
                if not(_ans[i] or _ans[i + 1]):
                    print("check1")
                    numSet.remove(temp)
                    numSet.remove(nums[i] - temp)
                    _ans[i] = temp
                    _ans[i + 1] = nums[i] - temp
                    ansFlag = backtrack(_ans)
                    if ansFlag:
                        break
                    _ans[i], _ans[i + 1] = _ans[i + 1], _ans[i]
                    ansFlag = backtrack(_ans)
                    if ansFlag:
                        break
                    _ans[i], _ans[i + 1] = None, None
                    numSet.add(temp)
                    numSet.add(nums[i] - temp)
                # one occupied
                elif _ans[i + 1]:
                    print("check2")
                    print(i, temp, _ans)
                    if temp + _ans[i + 1] != nums[i]:
                        continue
                    if i > 0 and _ans[i - 1] and temp + _ans[i - 1] != nums[i - 1]:
                        continue
                    _ans[i] = temp
                    ansFlag = backtrack(_ans)
                    if ansFlag:
                        break

                elif _ans[i]:
                    print("check3")
                    if temp + _ans[i] != nums[i]:
                        continue
                    if i < n - 1 and _ans[i + 2] and temp + _ans[i + 2] != nums[i + 1]:
                        continue
                    _ans[i] = temp
                    ansFlag = backtrack(_ans)
                    if ansFlag:
                        break

        if not ansFlag:
            return False
        else:
            return True
    
    backtrack(ans)
    print("final",ans)

        
    

    return

if __name__ == "__main__":
    main()