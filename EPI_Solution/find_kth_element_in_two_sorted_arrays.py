import sys
import random


# @include
def find_kth_in_two_sorted_arrays(A, B, k):
    # Lower bound of elements we will choose in A.
    b = max(0, k - len(B))
    # Upper bound of elements we will choose in A.
    t = min(len(A), k)

    while b < t:
        x = b + (t - b) // 2
        A_x_1 = float('-inf') if x <= 0 else A[x - 1]
        A_x = float('inf') if x >= len(A) else A[x]
        B_k_x_1 = float('-inf') if k - x <= 0 else B[k - x - 1]
        B_k_x = float('inf') if k - x >= len(B) else B[k - x]

        if A_x < B_k_x_1:
            b = x + 1
        elif A_x_1 > B_k_x:
            t = x - 1
        else:
            # B[k - x - 1] <= A[x] and A[x - 1] < B[k - x].
            return max(A_x_1, B_k_x_1)

    A_b_1 = float('-inf') if b <= 0 else A[b - 1]
    B_k_b_1 = float('-inf') if k - b - 1 < 0 else B[k - b - 1]
    return max(A_b_1, B_k_b_1)
# @exclude


def check_answer(A, B, k):
    i = j = count = 0
    while (i < len(A) or j < len(B)) and count < k:
        if i < len(A) and j < len(B):
            if A[i] < B[j]:
                ret = A[i]
                i += 1
            else:
                ret = B[j]
                j += 1
        elif i < len(A):
            ret = A[i]
            i += 1
        else:
            ret = B[j]
            j += 1
        count += 1
    return ret


def small_test():
    # AA: handwritten test
    A0 = [0, 1, 2, 3]
    B0 = [0, 1, 2, 3]
    assert 0 == find_kth_in_two_sorted_arrays(A0, B0, 1)
    assert 0 == find_kth_in_two_sorted_arrays(A0, B0, 2)
    assert 1 == find_kth_in_two_sorted_arrays(A0, B0, 3)
    assert 1 == find_kth_in_two_sorted_arrays(A0, B0, 4)
    assert 2 == find_kth_in_two_sorted_arrays(A0, B0, 5)


def main():
    small_test()
    # Random test 10000 times.
    for _ in range(10000):
        if len(sys.argv) == 3:
            n = int(sys.argv[1])
            m = int(sys.argv[2])
            k = random.randint(1, n + m)
        elif len(sys.argv) == 4:
            n = int(sys.argv[1])
            m = int(sys.argv[2])
            k = int(sys.argv[3])
        else:
            n = random.randint(1, 10000)
            m = random.randint(1, 10000)
            k = random.randint(1, n + m)

        A = sorted(random.randrange(100000) for _ in range(n))
        B = sorted(random.randrange(100000) for _ in range(m))
        ans = find_kth_in_two_sorted_arrays(A, B, k)
        print(k, 'th = ', ans, sep='')
        assert ans == check_answer(A, B, k)


if __name__ == '__main__':
    main()
