'''
Armstrong number:
input: 153
output: Armstrong number

input: 24
output: not an Armstrong number'''

n = int(input())
count = len(str(n))
s = 0
for digit in str(n):
    s += int(digit) ** count
print("Armstrong number" if s == n else "not an Armstrong number")



'''perfect number:'''


n = int(input())
s = 0
for i in range(1,n//2+1):
    if n%i == 0:
        s += i
print("perfect number" if s == n else "not an perfect number")





