


def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    if k == 0 or not s:
        return 0

    count = {}
    left = 0
    max_len = 0

    for right, ch in enumerate(s):
        count[ch] = count.get(ch, 0) + 1

        while len(count) > k:
            left_ch = s[left]
            count[left_ch] -= 1
            if count[left_ch] == 0:
                del count[left_ch]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len



def longest_single_char_substring(s: str) -> int:
    """
    Return the length of the longest substring
    that contains only one distinct character.
    """

    count = {}
    left = 0
    max_len = 0

    for right, ch in enumerate(s):
        count[ch] = count.get(ch, 0) + 1

        while len(count) > 1:
            left_ch = s[left]
            count[left_ch] -= 1
            if count[left_ch] == 0:
                # the line above means if the count (value) of the character
                # (key) left_ch in the dict is 0, then remove it in the line
                # below.
                del count[left_ch]

            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

