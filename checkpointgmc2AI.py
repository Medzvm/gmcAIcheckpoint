import numpy as np
#question1
result_list = []
for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        result_list.append(num)
print(result_list)

#question2

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(5)
print(result)
#question3
n = 8
result_dict = {}
for i in range(1, n+1):
    result_dict[i] = i*i
print(result_dict)
#question 4
def missing_char(word, n):
    return word[:n] + word[n+1:]

result = missing_char('kitten', 1)
print(result)
#question 5

original_array = np.array([[0, 1], [2, 3], [4, 5]])
converted_list = original_array.tolist()
print("Original array elements:", original_array)
print("Array to list:", converted_list)

#question6


array1 = np.array([0, 1, 2])
array2 = np.array([2, 1, 0])

covariance_matrix = np.cov(array1, array2)
print("Covariance matrix of the said arrays:", covariance_matrix)

# question 7
import math

C = 50
H = 30
input_sequence = input("Enter comma-separated values for D: ")
D_values = [int(value) for value in input_sequence.split(',')]

result_values = [int(math.sqrt((2 * C * D) / H)) for D in D_values]
print(','.join(map(str, result_values)))

