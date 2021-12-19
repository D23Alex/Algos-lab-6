import time
import os

step = 1
now = 1
last = 0
startTime = time.time()
d = set()

while step != 23990:
    nowF = now + last
    last = now
    now = nowF
    step += 1
    d.add(last)


fopen = open('input.txt', 'r')
fout = open('output.txt', 'a')
data = [int(i) for i in fopen.read().split()]
del data[0]

for i in range(len(data)):
    if data[i] in d:
        fout.write('Yes\n')
    else:
        fout.write('No\n')

fout.close()
#print(f'Need time: {time.time() - startTime}s')
#print(f'Last element:\n=========\n{now}')
