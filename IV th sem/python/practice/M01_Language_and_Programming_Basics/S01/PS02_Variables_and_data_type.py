pass1 = 1234
for i in range(3):
    password = int(input())
    if password==pass1:
        print("login successful")
        break
    else:
        print(i,"attmpt over")
