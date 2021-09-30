class Solution(object):
    def breakPalindrome(self,palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        #if length is 1, return ""
        if (len(palindrome) == 1):
            return ""
        #change the first letter to an a if it is not an a
        for x, letter in enumerate(palindrome):
            if(letter != 'a'):
                if(x != len(palindrome)/2):
                    output = palindrome[:x] + 'a' + palindrome[1+x:]
                    return output
        output = palindrome[:len(palindrome)-1] + 'b'
        return output
        # if first letter is an a, change to b

