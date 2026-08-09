class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        if n == 0:
            return []
        carry = 1
        i = n - 1
        while carry and i >= 0:
            digit = digits[i] + carry
            carry = digit // 10
            digit = digit % 10
            digits[i] = digit
            i -= 1
        if carry:
            digits.insert(0, carry)
        return digits
