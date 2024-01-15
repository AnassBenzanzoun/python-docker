# anna otto osso
class Palindrome:
    def isPalindrome(self, x):
        return "".join(reversed(str(x))) == str(x)


palindrome = Palindrome()
print(f" anna: {palindrome.isPalindrome('anna')}")

palindrome = Palindrome()
print(f" osso: {palindrome.isPalindrome('osso')}")

palindrome = Palindrome()
print(f" otto: {palindrome.isPalindrome('otto')}")

palindrome = Palindrome()
print(f" itopinonavevanonipoti: {palindrome.isPalindrome('itopinonavevanonipoti')}")
