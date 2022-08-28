def main(m, n, k):
    for i, j in zip(range(1, m), range(1, n)):
        if i * n == k or j * m == k:
            return True

    return False


if __name__ == '__main__':

    m = int(input())
    n = int(input())
    k = int(input())
    for i, j in zip(range(1, m + 2), range(1, n + 2)):

        if i * n == k or j * m == k:
            print("Yes")
            break
    else:
        print("No")
