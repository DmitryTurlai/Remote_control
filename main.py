s = input().split()
n = int(s[0])
m = int(s[1])
mas = [[0] * m for _ in range(n)]
for j in range(m):
      mas[0][j] = j + 1
for i in range(1, n):
      if i <= m:
            mas[i] = mas[0][i:] + mas[0][:i]
      elif i > m:
            mas[i] = mas[0][i - m:] + mas[0][:i - m]
for i in range(n):
    for j in range(m):
          print(mas[i][j], end=' ')
    print()