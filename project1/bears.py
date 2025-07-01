# Given integer n, returns True or False based on reachabilty of goal
def bears(n: int, attempted: list = None) -> bool:
    if attempted is None:
        attempted = []

    if n in attempted:
        return False
    else:
        attempted.append(n)

    if n == 42:
        return True
    elif n < 42:
        return False
    else:
        last_number = int(str(n)[-1])
        second_to_last_number = int(str(n)[-2])
        product = last_number * second_to_last_number

        if (n % 5 == 0) and bears(n - 42, attempted):
            return True
        elif (n % 2 == 0) and bears(n // 2, attempted):
            return True
        elif (n % 4 == 0 or n % 3 == 0) and bears(n - product, attempted):
            return True
        else:
            return False
