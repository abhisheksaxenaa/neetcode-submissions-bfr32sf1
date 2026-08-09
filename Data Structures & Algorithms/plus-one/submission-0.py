class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        if n == 0:
            return []
        carry = 0
        digit = digits[n - 1] + 1
        carry = digit // 10
        digit = digit % 10
        digits[n - 1] = digit

        i = n - 2
        while carry and i >= 0:
            digit = digits[i] + carry
            carry = digit // 10
            digit = digit % 10
            digits[i] = digit
            i -= 1
        if carry:
            digits.insert(0, carry)
        return digits
