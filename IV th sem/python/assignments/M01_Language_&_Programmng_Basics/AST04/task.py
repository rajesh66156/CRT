def Reverse_String(s: str) -> str:
    rev = ""
    for i in range(len(s) - 1,-1,-1):
        rev += s[i] 
    return rev


if __name__ == '_main_':
    s = input()
    print(Reverse_String(s))