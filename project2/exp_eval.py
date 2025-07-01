from stack_array import Stack
import math


# You do not need to change this class
class PostfixFormatException(Exception):
    pass


def postfix_eval(input_str: str) -> float:
    '''Evaluates a postfix expression
    
    Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** >> << or numbers.
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed
    DO NOT USE PYTHON'S EVAL FUNCTION!!!'''

    if len(input_str) == 0:
        raise PostfixFormatException("Empty input")

    expression_list = input_str.split()
    my_stack = Stack(30)
    operations_list = ["+", "-", "*", "/", "**", ">>", "<<"]

    for token in expression_list:
        if token not in operations_list:
            try:
                int(token)
                my_stack.push(int(token))
            except ValueError:

                try:
                    float(token)
                    my_stack.push(float(token))
                except ValueError:
                    raise PostfixFormatException("Invalid token")
        elif token in operations_list:
            if my_stack.size() < 2:
                raise PostfixFormatException("Insufficient operands")

            else:
                x = my_stack.pop()
                y = my_stack.pop()
                if token == ">>":
                    try:
                        push_value = y >> x
                        my_stack.push(push_value)
                    except TypeError:
                        raise PostfixFormatException("Illegal bit shift operand")

                elif token == "<<":
                    try:
                        push_value2 = y << x
                        my_stack.push(push_value2)
                    except TypeError:
                        raise PostfixFormatException("Illegal bit shift operand")

                elif token == "+":
                    my_stack.push(y + x)
                elif token == "-":
                    my_stack.push(y - x)
                elif token == "*":
                    my_stack.push(y * x)
                elif token == "/":
                    if x == 0:
                        raise ValueError
                    my_stack.push(y / x)
                elif token == "**":
                    my_stack.push(y ** x)

    if my_stack.num_items != 1:
        raise PostfixFormatException("Too many operands")

    return my_stack.pop()


def infix_to_postfix(input_str: str) -> str:
    '''Converts an infix expression to an equivalent postfix expression

    Input argument:  a string containing an infix expression where tokens are
    space separated.  Tokens are either operators + - * / ** >> << parentheses ( ) or numbers
    Returns a String containing a postfix expression '''
    precedence = {
        '>>': 4, '<<': 4,
        '**': 3,
        '*': 2, '/': 2,
        '+': 1, '-': 1,
    }

    output = []
    operator_stack = Stack(30)
    tokens = input_str.split()
    for token in tokens:
        if token not in precedence and token != "(" and token != ")":
            output.append(token)
        elif token == "(":
            operator_stack.push(token)
        elif token == ")":
            while not operator_stack.is_empty() and operator_stack.peek() != "(":
                output.append(operator_stack.pop())
            operator_stack.pop()  # Discard the '('
        else:
            while (not operator_stack.is_empty() and operator_stack.peek() != "("
                   and precedence.get(operator_stack.peek(), 0) >= precedence.get(token, 0)
                   and precedence.get(operator_stack.peek(), 0) != 3):  # Exclude exponentiation operator
                output.append(operator_stack.pop())
            operator_stack.push(token)

    while not operator_stack.is_empty():
        output.append(operator_stack.pop())

    return " ".join(output)


def prefix_to_postfix(input_str: str) -> str:
    '''Converts a prefix expression to an equivalent postfix expression
    Input argument:  a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** >> << or numbers
    Returns a String containing a postfix expression (tokens are space separated)'''
    reverse_input = []
    operations_list = ["+", "-", "*", "/", "**", ">>", "<<"]
    list_str = input_str.split()
    for i in range(len(list_str) - 1, -1, -1):
        if list_str[i] != " ":
            reverse_input.append(list_str[i])

    my_stack = Stack(30)

    for token in reverse_input:
        if token not in operations_list:
            my_stack.push(token)
        else:
            pop1 = my_stack.pop()
            pop2 = my_stack.pop()
            x = pop1 + " " + pop2 + " " + token
            my_stack.push(x)

    return my_stack.pop()
