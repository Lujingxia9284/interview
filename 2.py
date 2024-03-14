n, m = map(int, input().split(' '))
s =''
for i in range(m):
    s += input()3 

meituan = list('meituan')

flag = True

for item in meituan:
    if item not in s:
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')