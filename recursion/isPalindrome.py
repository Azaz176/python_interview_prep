class Solution:
    def isPalindrome(self, s: str) -> bool:
        def helper(s, i, j):
            # Base case: if pointers have crossed, it means it's a palindrome
            if i >= j:
                return True
            # If characters at i and j do not match, it is not a palindrome
            if s[i] != s[j]:
                return False
            # Recursive call to check the remaining substring
            return helper(s, i + 1, j - 1)
        
        # Initial call with full string range
        return helper(self.s, 0, len(s) - 1)
