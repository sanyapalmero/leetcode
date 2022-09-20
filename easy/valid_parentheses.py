"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
 

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

def is_valid_v1(input_str: str) -> bool:
    """My first try to solve this problem"""
    if not input_str or len(input_str) == 1 or len(input_str) % 2 != 0:
        return False

    round_brackets = ("(", ")")
    square_brackets = ("[", "]")
    curly_brackets = ("{", "}")

    left_part = input_str[:len(input_str) // 2]
    right_part = input_str[len(input_str) // 2:]

    if (left_part[-1], right_part[0]) not in [round_brackets, square_brackets, curly_brackets]:
        return False 

    def _get_another_bracket(brackets_tuple: tuple, bracket: str) -> str:
        return brackets_tuple[1] if brackets_tuple.index(s) == 0 else brackets_tuple[0]

    mirrored_right_part = ""
    for s in right_part[::-1]:
        if s in round_brackets:
            mirrored_right_part += _get_another_bracket(round_brackets, s)
        elif s in square_brackets:
            mirrored_right_part += _get_another_bracket(square_brackets, s)
        elif s in curly_brackets:
            mirrored_right_part += _get_another_bracket(curly_brackets, s)

    if left_part == mirrored_right_part:
        return True

    for i in range(0, len(input_str), 2):
        if i + 1 >= len(input_str):
            break

        bracket = input_str[i]

        if bracket in round_brackets and (bracket, input_str[i + 1]) != round_brackets:
            return False
        elif bracket in square_brackets and (bracket, input_str[i + 1]) != square_brackets:
            return False
        elif bracket in curly_brackets and (bracket, input_str[i + 1]) != curly_brackets:
            return False

    return True


def is_valid(input_str: str) -> bool:
    close_to_open = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    stack = []
    for s in input_str:
        if s in close_to_open:
            if stack and stack[-1] == close_to_open[s]:
                stack.pop()
            else:
                return False
        else:
            stack.append(s)

    return True if not stack else False


assert is_valid("(([]){})")
assert is_valid("{[]}")
assert is_valid("()")
assert is_valid("()[]{}")
assert not is_valid("(}{)")
assert not is_valid("(]")
assert not is_valid("[")
assert not is_valid("[])")
