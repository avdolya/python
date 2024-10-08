def main():
    ...


n = int(input())
l_h = k = 0
arr = []
for i in range(n):
    a = int(input())
    arr.append(a)
for i in range(n):
    h_n = arr[i] % 256
    r_n = (arr[i] // 256) % 256
    m_n = arr[i] // (256 * 256)
    h = (37 * (m_n + r_n + l_h)) % 256
    if h != h_n or h >= 100:
        k = 1
        print(i)
        break
    else:
        l_h = h_n
if k == 0:
    print(-1)
if __name__ == "__main__":
    main()

