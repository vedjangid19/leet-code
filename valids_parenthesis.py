# # Intuition
# <!-- Describe your first thoughts on how to solve this problem. -->

# # Approach
# <!-- Describe your approach to solving the problem. -->

# # Complexity
# - Time complexity:
# <!-- Add your time complexity here, e.g. $$O(n)$$ -->

# - Space complexity:
# <!-- Add your space complexity here, e.g. $$O(n)$$ -->

# # Code

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        mapping = {')':'(', ']':'[', '}': '{'}

        for char in s:
            if char not in mapping:
                stack.append(char)
                continue
            elif not stack or mapping[char] != stack.pop():
                return False
            
        return not stack
