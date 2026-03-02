# Reverse a String Using Loop

def reverse_string(s):
    reversed_str = ""

    # Traverse the string from end to start
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]

    return reversed_str


if __name__ == "__main__":
    # Taking input
    text = input("Enter a string: ")

    # Print reversed string
    print(reverse_string(text))