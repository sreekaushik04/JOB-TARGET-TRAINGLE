def solve(A):
    A = A
    l = len(A)
    if l == 1:
        return A[0][0]
    down = A[l-1]
    up = [0]*l
    for i in range(l-2, -1, -1):
        for j in range(i+1):
            up[j] = A[i][j] + max(down[j], down[j+1])
        down = up
    return up[0]

def get_line_count(file_path):
    f = open(file_path,"r")
    line_count = 0
    for line in f:
        line_count += 1
    return line_count

file_path = "D:\\ASSIGNMENT JT\\ASSIGNMENT JT.txt"
line_count = get_line_count(file_path)
file1 = open(file_path,"r")
row = 0
inp = []
while True:
    line = file1.readline()
    if not line:
        break
    s = list(map(int, line.split()))
    s = s + [0 for _ in range(line_count-len(s))]
    inp.append(s)
print(solve(inp))