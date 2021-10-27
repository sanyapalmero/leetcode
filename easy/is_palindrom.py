def is_palindrom(number: int) -> bool:
    str_number = str(number)
    iterations = len(str_number) // 2

    for i in range(iterations):
        if str_number[i] != str_number[-i-1]:
            return False

    return True

print(is_palindrom(121))
