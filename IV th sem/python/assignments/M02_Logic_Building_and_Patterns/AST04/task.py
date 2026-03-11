def right_triangle(n: int) -> str:
    result = []
    
    for i in range(1, n + 1):
        result.append("*" * i)
    
    return "\n".join(result)


if __name__ == "_main_":
    n = int(input())
    print(right_triangle(n))