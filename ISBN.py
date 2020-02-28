isbn = input("Please input 12 digits: ")
even = 0
odd = 0

for i in range(0,12,2):
    even = even + int(isbn[i])

for i in range(1,12,2):
    odd = odd + int(isbn[i])*3

x13 = (10 - ((even+odd)%10))

print(isbn,"-",x13)