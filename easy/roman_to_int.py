"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:

Input: s = "III"
Output: 3
Example 2:

Input: s = "IV"
Output: 4
Example 3:

Input: s = "IX"
Output: 9
Example 4:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:
1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""

ROMAN = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

RULES = {
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900,
}


def roman_to_int(roman_numeral_str: str) -> int:
    """My first try"""

    res = 0
    symbols_count = len(roman_numeral_str)
    idx = 0
    while idx < symbols_count:
        letter = roman_numeral_str[idx]
        if letter == "I" and idx + 1 < symbols_count and roman_numeral_str[idx + 1] == "V":
            res += 4
        elif letter == "I" and idx + 1 < symbols_count and roman_numeral_str[idx + 1] == "X":
            res += 9
        elif letter == "X" and idx + 1 < symbols_count and roman_numeral_str[idx + 1] == "L":
            res += 40
        elif letter == "X" and idx + 1 < symbols_count and roman_numeral_str[idx + 1] == "C":
            res += 90
        elif letter == "C" and idx + 1 < symbols_count and roman_numeral_str[idx + 1] == "D":
            res += 400
        elif letter == "C" and idx + 1 < symbols_count and roman_numeral_str[idx + 1] == "M":
            res += 900
        else:
            res += ROMAN[letter]
            idx += 1
            continue
        idx += 2
    return res


def roman_to_int_v2(roman_numeral_str: str) -> int:
    """Refactored previous code"""

    res, idx = 0, 0
    while idx < len(roman_numeral_str):
        if idx + 1 < len(roman_numeral_str) and roman_numeral_str[idx] + roman_numeral_str[idx + 1] in RULES.keys():
            res += RULES[roman_numeral_str[idx] + roman_numeral_str[idx + 1]]
            idx += 2
        else:
            res += ROMAN[roman_numeral_str[idx]]
            idx += 1
    return res


print(roman_to_int_v2("LVIII"))
print(roman_to_int_v2("MCMXCIV"))
