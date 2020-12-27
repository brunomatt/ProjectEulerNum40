# An irrational decimal fraction is created by concatenating the positive integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of the following expression.
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

digits = ''.join([str(n) for n in range(0,1000001)])

answer = int(digits[1]) * int(digits[10]) * int(digits[100]) * int(digits[1000]) * int(digits[10000]) * int(digits[100000]) * int(digits[1000000])

print(answer)