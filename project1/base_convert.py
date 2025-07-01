# Given integer num and base b, converts num to a string representation in base b
def convert(num: int, b: int) -> str:
    if b < 1:
        raise ValueError

    alpha = ["A", "B", "C", "D", "E", "F"]
    str_remainder = ""
    remainder = (num % b)
    quotient = num // b
    if remainder > 9:
        str_remainder += alpha[remainder - 10]
    else:
        str_remainder += str(remainder)

    if quotient == 0:
        return str_remainder

    else:
        return convert(quotient, b) + str_remainder
