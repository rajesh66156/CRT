
'''n = int(input())
even = odd = 0
while n>0:
    if (n%2) == 0:
        eve += 1
    else:
        odd += 1
    n //= 10
print(even,odd)'''


n = int(input())
while n>9:
    n = sum(map(int,str(n)))
print(n)