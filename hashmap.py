# ==========================================
# PROBLEM 1: TWO SUM
# ==========================================
# Big-O Runtime: O(n)
# Big-O Space: O(n)
def two_sum(nums: list, target: int) -> list:
    """
    Hash Map Strategy:
    As we iterate through the list, we compute the required 'complement' (target - current_num).
    We check if this complement already exists in our dictionary. If it does, we immediately 
    return its index along with the current item's index. Otherwise, we store the current 
    number and its index in our map for future reference. This guarantees a single pass.
    """
    seen = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], index]
        seen[num] = index
    return []

# Test Cases
assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([3, 2, 4], 6) == [1, 2]
assert two_sum([3, 3], 6) == [0, 1]


# ==========================================
# PROBLEM 2: IS ANAGRAM
# ==========================================
# Big-O Runtime: O(n)
# Big-O Space: O(1) -> Bound to character map size constraints (max 26 keys for English alphabet)
def is_anagram(s: str, t: str) -> bool:
    """
    Hash Map Strategy:
    An anagram must have the exact same count of characters. We first check if length matches.
    Then, we loop through both strings simultaneously to increment counts for string 's' and
    decrement counts for string 't' inside a shared frequency dictionary. Finally, we verify 
    if all entries in our hash map have returned to 0.
    """
    if len(s) != len(t):
        return False
        
    counts = {}
    for i in range(len(s)):
        counts[s[i]] = counts.get(s[i], 0) + 1
        counts[t[i]] = counts.get(t[i], 0) - 1
        
    return all(val == 0 for val in counts.values())

# Test Cases
assert is_anagram("anagram", "nagaram") is True
assert is_anagram("rat", "car") is False
assert is_anagram("awesome", "asweome") is True

print("All Hash Map algorithm problems and testing validations passed!")