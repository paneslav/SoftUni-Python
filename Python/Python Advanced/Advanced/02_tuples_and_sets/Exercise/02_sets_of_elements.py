n, m = input().split()

n_set = set(int(input()) for _ in range(int(n)))
m_set = set(int(input()) for _ in range(int(m)))

[print(item) for item in (n_set & m_set)]