# Write a Python program to read two numbers and display their sum, difference, product, and quotient.
# a = int(input("1st number = "))
# b = int(input("2nd number = "))
# print("sum =", a+b)
# print("difference =", a-b)
# print("product =", a*b)

2. # Write a Python program to check whether a given number is even or odd. 
# A = int(input("Enter the number = "))
# if (A%2 == 0):
#     print("Number is Even")
# else:
#     print("Number Odd")

# 3.Write a Python program to check whether a given number is positive, negative, or zero. 
# N = int(input("Enter the number = "))
# if (N > 0):
#     print("Number is positive")
# elif (N < 0):
#     print("Number is Negative")
# else:
#     print("Number is Zero")

# 4.Write a Python program to find the largest of three numbers.
# A = int(input("Enter the First number = "))
# B = int(input("Enter the second number = "))
# C = int(input("Enter the Thired number = "))
# if (A >= B and A >=C):
#     print("A is lagest number")
# elif (B >= A and B >=C):
#     print("B is largest number")
# else:
#     print("C is largest number") 

# 5.Write a Python program to check whether a given year is a leap year or not.
# Y = int(input("Enter the year = "))
# if (Y%4==0):
#     print("Year is leap year")
# else:
#     print("year is not leap year")

# 6.Write a Python program to print the first N natural numbers using a loop.
# N = int(input("Enter the number = "))
# sum = 0
# for i in range(1, N+1):
#     sum = sum+i
# print("Sum of first", N, "natural numbers is:", sum)

# 7.Write a Python program to find the factorial of a given number using a loop. 
# N = int(input("Enter the number = "))
# F = 1
# for i in range(N, 1, -1):
#     F = F*i
# print("factorial = ", F)

# 8.Write a Python program to generate the Fibonacci series up to N terms. 
# n = int(input("Enter number of terms: "))
# a = 0
# b = 1
# for i in range(n):
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c

# 9.Write a Python program to reverse a given number using a loop. 
# N = int(input("Enter the number: "))
# rev = 0
# while N > 0:
#     digit = N % 10
#     rev = rev * 10 + digit
#     N //= 10
# print("Reverse number:", rev)

# 10.Write a Python program to check whether a given number is a palindrome.
# N  = int(input("Enter the number: "))
# r = N
# rev = 0
# while N > 0:
#     digit = N % 10
#     rev = rev * 10 + digit
#     N //= 10
# if(rev == r):
#     print("Number is palindrome")
# else:
#     print("number is not palindrome")

# 11.Write a Python program to find the sum of all elements in a list. 
n = int(input("Enter number of elements: "))
lst = []
sum = 0

for i in range(n):
    x = int(input("Enter element: "))
    lst.append(x)
    sum = sum+x

print(lst)
print(sum)



    
    