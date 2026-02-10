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
# n = int(input("Enter number of elements: "))
# lst = []
# sum = 0

# for i in range(n):
#     x = int(input("Enter element: "))
#     lst.append(x)
#     sum = sum+x

# print(lst)
# print(sum) 

 # 12.Write a Python program to find the largest and smallest elements in a list.
 
 # What is the probability the team wins given the player is absent?
# o Probability of winning with star player: 60%
# o	Probability of winning without star player: 30%
# o	Probability of star player being absent: 40%

# A = int(input("Enter the number with star player: "))/100
# B = int(input("Enter the number with without star player: "))/100
# C = int(input("Enter the number player being absent: "))/100

# D = (A*B)/C 
# print(D)


# o	Probability of object being a pedestrian: 5%
# o	Sensor accuracy for pedestrians: 90%
# o	Probability of false detection: 10%
# •	Question: What is the probability the detected object is truly a pedestrian?
# A = int(input("Enter  being a pedestrian: "))/100
# B = int(input("Enter accuracy for pedestrians: "))/100
# C = int(input("Enter false detection: "))/100

# D = ((A*B)/C)*100
# print(D)
import pandas as pd

# Set the path to the file you'd like to load
file_path = r"C:\Users\LENOVO LOQ\Desktop\Titanic-Dataset.csv"

# Load the dataset using pandas
df = pd.read_csv(file_path)

# Display first 5 records
# print("First 5 records:")
# print(df.head())

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
print("All entities in the dataset:")
print(df)

# Check for missing values in each column
missing_values = df.isnull().sum()
missing_percentage = (df.isnull().sum() / len(df)) * 100

# Create a summary DataFrame for missing values
missing_summary = pd.DataFrame({
    "Missing Count": missing_values,
    "Missing Percentage": missing_percentage
})
print("\nMissing values summary:")
print(missing_summary)

# Removing Duplicates value

# Export both the dataset and missing-value summary to Excel
with pd.ExcelWriter("Titanic_MissingData_Analysis.xlsx") as writer:
    df.to_excel(writer, sheet_name="Titanic Dataset", index=False)
    missing_summary.to_excel(writer, sheet_name="Missing Values Summary")



     



    
    