def get_even_num():
    result = []

    result.append(num for num in range(1, 51) if num%2 == 0)

    return result
