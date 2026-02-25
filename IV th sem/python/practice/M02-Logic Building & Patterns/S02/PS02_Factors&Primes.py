'''n = int(input("Enter a number:"))
for i in range(1,n//2+1):
    if n % i = 0:
        print(i,end=" ")'''
    



'''n=int(input())
counter = 0
for i in range(2,n//2+1):
    if n % i == 0:
        counter += 1
print("prime" if counter == 0 else "not prime")'''



''''start = int(input())
end = int(input())
if start == 1:
    start = 2
for n in range(start,end+1):
    counter = 0
    for i in range(2,n//2+1):
        if n % i ==0:
            counter += 1
    if counter == 0:
        print(n,end=" ")'''



''''a = int(input())
b = int(input())
while b:
    a, b = b, a % b
print(a)


import math
print(math.gcd(a,b))'''


n = int(input())