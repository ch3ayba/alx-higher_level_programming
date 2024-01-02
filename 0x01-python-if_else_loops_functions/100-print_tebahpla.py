#!/usr/bin/python3
for c in range(ord('z'), ord('a') - 1, -1):
    if c % 2 == 0:
        d = 0
    else:
        d = 32
    print('{}'.format(chr(c - d)), end='')
