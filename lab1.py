# ex1 - find the gcd of two numbers read from the console

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def get_gcd_of_numbers():
    numbers = []

    while True:
        try:
            num = int(input("Enter a number (or 0 to calculate GCD): "))
            if num == 0:
                break
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    if len(numbers) < 2:
        print("At least two numbers are required to calculate GCD.")
    else:
        gcdVal = numbers[0]
        for i in range(1, len(numbers)):
            gcdVal = gcd(gcdVal, numbers[i])

        print(f"The GCD of {numbers} is {gcdVal}")


get_gcd_of_numbers()


# ex2 - calculate the number of vowels in a string
def countVowels(word):
    count = 0
    for i in range(len(word)):
        if word[i] in "aeiouAEIOU":
            count += 1
    return count


print("Number of vowels in 'Imi place sa mananc':", countVowels("Imi place sa mananc"))
print("Number of vowels in 'bcd':", countVowels("bcd"))


# ex3 - print the number of occurrences of the first string in the second

def countOccurrences(word, string):
    count = 0
    index = 0
    while True:
        index = string.find(word, index)  # find occurrence
        if index == -1:
            break
        count += 1
        index += len(word)  # start searching after the last occurrence
    return count


print("Number of occurrences of 'ana' in 'ana are mere si ana are pere':",
      countOccurrences("ana", "ana are mere si ana are pere"))


# ex 4 - write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.

def convertToUnderscores(string):
    result = ""
    for i in range(len(string)):
        if string[i].isupper() and i != 0:
            result += "_"
        result += string[i].lower()
    return result


print("Underscored version of 'UpperCamelCase':", convertToUnderscores("UpperCamelCase"))


# ex 5 - print the matrix obtained by going through spiral order

def printSpiral(matrix):
    if not matrix:
        return ""

    result = []
    rows, cols = len(matrix), len(matrix[0])
    top = 0
    bottom = rows - 1
    left = 0
    right = cols - 1

    while top <= bottom and left <= right:
        # traverse the top row
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # traverse the right column
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        # traverse the bottom row from right to left
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        # traverse the left column from bottom to top
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return "".join(result)


m = [
    ['f', 'i', 'r', 's'],
    ['n', '_', 'l', 't'],
    ['o', 'b', 'a', '_'],
    ['h', 't', 'y', 'p']
]

print("Spiral order of matrix:", printSpiral(m))


# ex 6 - write a function that validates if a number is a palindrome.
def isPalindrome(number):
    check = number
    if number < 0:
        return False
    if number < 10:
        return True

    inv = 0
    while number > 0:
        inv = inv * 10 + number % 10
        number //= 10

    return check == inv


print("Is 12321 a palindrome?", isPalindrome(12321))
print("Is 12345 a palindrome?", isPalindrome(12345))


# ex 7 - extract the first number from a text

def extractFirstNumber(text):
    result = ""
    found_number = False

    for c in text:
        if c.isdigit():
            result += c
            found_number = True
        elif found_number:
            break

    if result:
        return int(result)
    else:
        return None


print("First number in 'abc123def456':", extractFirstNumber("abc123def456"))
print("First number in 'An apple is 123 USD: ", extractFirstNumber("An apple is 123 USD"))


# ex 8 - write a function that counts how many bits with value 1 a number has

def countBits(value):
    binary_value = bin(value)[2:]  # transform to binary and remove the first two characters
    print("Binary value of given number: ", binary_value)
    return binary_value.count("1")


print("Number of bits with value 1 in 24:", countBits(24))


# ex 9 - write a function that determines the most common letter in a string

def mostCommonLetter(string):
    input_string = string.lower()  # transform to lowercase
    letter_count = {}

    for letter in input_string:
        if letter.isalpha():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1

    if letter_count:
        print("Max occurrences of a letter:", max(letter_count.values()))
        return max(letter_count, key=letter_count.get)
    else:
        return None, 0


print("Most common letter in 'an apple is not a tomato':", mostCommonLetter("an apple is not a tomato"))


# ex 10 - count spaces in a text

def count_words(input_text):
    words = input_text.split()

    return len(words)


print("Number of words in 'I have Python exam':", count_words("I have Python exam"))
