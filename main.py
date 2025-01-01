#Reverse a String:
#Write a function that takes a string as input and returns the string reversed.
word = input('insert a string')
reversed_word = word[::-1]
print(reversed_word)

#Example: Input: "hello", Output: "olleh"

#Find the Largest Element in an Array:
#Write a function that finds and returns the largest element in an array of integers.
#Example: Input: [10, 20, 30, 5], Output: 30

array = [5,10,30,60,100]
max_num = max(array)
print(max_num)

#Check for Palindrome:
#Write a function that checks whether a given string is a palindrome (reads the same forwards and backwards).

#Example: Input: "racecar", Output: true

words = input('enter a word to check a word for a palidrome')
reverse_words = words[::-1]
if words == reverse_words:
    print('true')
else:
    print('false')




#Factorial Calculation:
#Write a function to calculate the factorial of a given number n.
#Example: Input: n = 5, Output: 120 (since 5! = 5 * 4 * 3 * 2 * 1)

og_num = input('enter number')


#Sum of Array Elements:
#Write a function that takes an array of integers and returns the sum of all the elements.
#Example: Input: [1, 2, 3, 4], Output: 10

numbers = int(input('input different numbers to add together'))
print(sum(numbers))
