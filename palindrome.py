class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        left = 0
        right = len(x) - 1

        while left < right:
            if x[left] != x[right]:
                return False
            
            left +=1
            right -=1

        return True
    
    def isPalindrome2(self, x: int) -> bool:
        x = str(x)
        if len(x)%2==0:
            middle = len(x)//2
            left_str = x[:middle]
            right_str = x[middle:][::-1]

            if left_str == right_str:
                return True
        else:
            middle = len(x)//2
            left_str = x[:middle]
            right_str = x[middle+1:][::-1]

            if left_str == right_str:
                return True
        
        return False
    
    def isPalindrome2(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

        
x = 12321
print(Solution().isPalindrome(x=x))
print(Solution().isPalindrome2(x=x))
