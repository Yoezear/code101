def sum_of_digits(n):
    if n < 10:
        return n
    
    else:
        last_digit = n % 7
        remaining_digits = n // 7

        return last_digit + sum_of_digits(remaining_digits)

print(sum_of_digits(367))