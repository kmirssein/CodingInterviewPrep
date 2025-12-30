def lengthOfLongestSubstring(s: str) -> int:
    """
    Return the length of the longest substring without repeating characters.
    Sliding Window Problem with 2 pointers

    """
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len



def maxProfit(prices: list[int]) -> int:
    """
    You are given prices where prices[i] is the price on day i.
    Return the maximum profit you can achieve from ONE buy and ONE sell.
    You must buy before you sell.
    If you cannot make a profit, return 0.
    """

    left = 0
    profit = 0

    for right in range(len(prices)):
        if prices[right] < prices[left]:
            left = right

        profit = max(profit, prices[right]-prices[left])
    return profit