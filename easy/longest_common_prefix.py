"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""


def longest_common_prefix(strings_list: list) -> str:
    if not strings_list:
        return ""

    if len(strings_list) >= 1 and strings_list[0] == "":
        return ""

    strings_list.sort(key=len, reverse=True)
    if strings_list[0] and strings_list[-1] and strings_list[0][0] != strings_list[-1][0]:
        return ""

    prefix = strings_list[0]
    for word in strings_list[1:]:
        res = ""
        for i, letter in enumerate(prefix):
            if i < len(word) and letter == word[i]:
                res += word[i]
            else:
                break
        prefix = res
            
    return prefix

assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
assert longest_common_prefix(["dog", "racecar", "car"]) == ""
assert longest_common_prefix(["abab", "aba", ""]) == ""
assert longest_common_prefix(["abab", "aba", "abc"]) == "ab"
assert longest_common_prefix(["", "", ""]) == ""
assert longest_common_prefix(["", ""]) == ""
assert longest_common_prefix([""]) == ""
assert longest_common_prefix([]) == ""
