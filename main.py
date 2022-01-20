"""
Given a 4 digit number n as input, find the sum of its digits. Note that n%10 gives its last digit, whereas n/10 removes the last digit. So if n=2456, n%10 is 6 and n/10 is 245. So, run a for loop from 1 to 4 and in the loop do 2 things – calculate the last digit and then remove the last digit.
Input-> n=2456
Output-> 17
"""

n = 2456
ln = len(str(n))
total = 0
dig = 0
for i in range(1,ln+1):
  dig = n%10
  total = total + dig
  n = n/10
print(total)
