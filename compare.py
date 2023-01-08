import sys

def normalize(str):
    new_str = ""
    is_commented = False
    for ch in str:
        if ch == '#':
            is_commented = True
        elif ch == '\n':
            is_commented = False
        elif not is_commented and ch != ' ':
            new_str += ch
    return new_str

def get_dist(str1, str2):
    str1 = normalize(str1)
    str2 = normalize(str2)
    n = len(str1)
    m = len(str2)
    if m > n:
        n, m = m, n
        str1, str2 = str2, str1
    dist = [[0] * (m + 1) for i in range(2)]
    pos_calced = 0
    for i in range(n):
        for j in range(m):
            dist[pos_calced ^ 1][j + 1] = max(dist[pos_calced][j + 1], dist[pos_calced][j] + int(str1[i] == str2[j]))
        pos_calced ^= 1
    return dist[pos_calced][m] / n

f_input = open(sys.argv[1], "r")
f_output = open(sys.argv[2], "w")

for line in f_input.readlines():
    files = line.split()
    with open(files[0]) as f:
        str1 = f.read()
    with open(files[1]) as f:
        str2 = f.read()
    f_output.write(str(get_dist(str1, str2)) + '\n')

f_input.close()
f_output.close()
