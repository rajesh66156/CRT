# Collatz Sequence

def collatz_sequence(n):
    sequence = []

    # Continue until n becomes 1
    while True:
        sequence.append(n)

        if n == 1:
            break

        if n % 2 == 0:
            n = n // 2   # Even case
        else:
            n = 3 * n + 1   # Odd case

    return sequence


if __name__ == "__main__":
    # Taking input
    num = int(input("Enter a positive integer: "))

    # Print sequence
    print(collatz_sequence(num))