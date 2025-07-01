import math


# Returns list of permutations for input string
# e.g. 'ab' -> ['ab', 'ba']; 'a' -> ['a']; '' -> []
def perm_gen_lex(str_in: str) -> list[str]:
    # base case(s)
    if len(str_in) == 0:
        return []

    elif len(str_in) == 1:
        return [str_in]

    else:
        result = []
        for i in range(len(str_in)):  # the original 'abc' is used in this range function the whole time the code is run
            # then other smaller permutations of it run the range while the other one is still stored.
            without_char = str_in[:i] + str_in[i + 1:]  # this excludes the charter that we need excluded
            perms = perm_gen_lex(without_char)  # this re-runs the function
            for perm in perms: # after the (elif len(str_in) is hit the function comes here to add the char to the perms
                result.append(str_in[i] + perm)
        return result  # once this is hit it doesn't mean the code is done yet, it needs to finish the original for loop
        # in the start of the else of the 'abc' so the first time this is hit it only completed i = 0, and now will move
        # onto i = 1 with the original input string of 'abc'


