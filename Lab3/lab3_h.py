import sys



"""
we will create an array P.
1. use the sum function that we learned in order to enter line at which ith block ends
2. implement binary search
    check for line to be in the interval of two numbers in the list
    print the index
"""


def binary_search(P, goal):
    left = 0
    right = len(P) - 1
    while left <= right:
        mid = (left + right) // 2
        if P[mid] >= goal:
            right = mid - 1
        else:
            left = mid + 1
    return left + 1


# def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))


def main():
    N, M = map(int, sys.stdin.readline().split())
    lines = list(map(int, sys.stdin.readline().split()))
    # P = [sum(lines[:i+1]) for i in range(len(lines))]
    P = [0] * N
    P[0] = lines[0]
    for i in range(1, N):
        P[i] = P[i - 1] + lines[i]

    while M != 0:
        error_line = int(sys.stdin.readline().strip())
        sys.stdout.write(str(binary_search(P, error_line)) + '\n')
        M -= 1


if __name__ == '__main__':
    main()




"""
#include <iostream>
#include <vector>

int binary_search(const std::vector<int>& P, int goal) {
    int left = 0;
    int right = P.size() - 1;
    while (left <= right) {
        int mid = (left + right) / 2;
        if (P[mid] >= goal) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return left + 1;
}

int main() {
    int N, M;
    std::cin >> N >> M;

    std::vector<int> lines(N);
    for (int i = 0; i < N; ++i) {
        std::cin >> lines[i];
    }

    std::vector<int> P(N);
    P[0] = lines[0];
    for (int i = 1; i < N; ++i) {
        P[i] = P[i - 1] + lines[i];
    }

    while (M != 0) {
        int error_line;
        std::cin >> error_line;
        std::cout << binary_search(P, error_line) << '\n';
        M -= 1;
    }

    return 0;
}

"""