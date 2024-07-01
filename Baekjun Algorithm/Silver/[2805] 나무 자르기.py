import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N: 나무의 수, M: 가져가야하는 나무의 길이
trees = list(map(int, input().split()))

def binary_search(N, M, trees):
    min_tree, max_tree = 1, max(trees)

    while min_tree <= max_tree:
        target = (min_tree + max_tree) // 2 
        sum_ = 0

        for i in trees:
            if i > target:
                sum_ += i - target

        if sum_ >= M:
            min_tree = target + 1
        else:
            max_tree = target - 1

    return max_tree

print(binary_search(N, M, trees))