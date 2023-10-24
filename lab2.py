from math import sqrt
from typing import Any, Set, Tuple


# ex1: return a list of the first n numbers in the Fibonacci string.
def generate_fibonacci(n: int) -> list[int]:
    if n <= 0:
        return []

    fibonacci_sequence = [0, 1]

    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence


value = 10
fibonacci_numbers = generate_fibonacci(value)
print(f"The first {value} Fibonacci numbers are: {fibonacci_numbers}")


# ex2: a function that receives a list of numbers and returns a list of the prime numbers found in it

def return_primes(list_of_numbers: list[int]) -> list[int]:
    new_list = []
    for item in list_of_numbers:
        if item > 1:
            for i in range(2, int(sqrt(item) + 1)):
                if (item % i) == 0:
                    break
            else:
                new_list.append(item)
    return new_list


print("The prime values in the list [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] are ",
      return_primes([0, 1, 1, 2, 3, 5, 8, 13, 21, 34]))


# ex3: a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited with
# b, a - b, b - a)
def list_operations(a, b: list[int] or list[str]) -> tuple[list, list, list, list]:
    # intersection of a with b
    intersection = list(set(a) & set(b))

    # a reunited with b
    union = list(set(a) | set(b))

    # a-b
    a_minus_b = list(set(a) - set(b))

    # b-a
    b_minus_a = list(set(b) - set(a))

    return intersection, union, a_minus_b, b_minus_a


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [2, 4, 6, 8, 10, 12, 14, 16, 18]

print("The intersection, union, a-b and b-a of lists ", list1, " and ", list2, " are ", list_operations(list1, list2))


# ex4:  a function that receives as a parameters a list of musical notes (strings), a list of moves (integers) and a
# start position (integer). The function will return the song composed by going through the musical notes beginning
# with the start position and following the moves given as parameter.

def compose(notes: list[str], moves: list[int], start_position: int) -> list[str]:
    song = []
    position = start_position
    song.append(notes[position])
    for move in moves:
        position += move
        while position < 0:
            position += len(notes)
        while position >= len(notes):
            position -= len(notes)
        song.append(notes[position])

    return song


notes_list = ["do", "re", "mi", "fa", "sol"]
moves_list = [1, -3, 4, 2]
start = 2

result = compose(notes_list, moves_list, start)
print("Composed song: ", result)


# ex5: a function that receives as parameter a matrix and will return the matrix obtained by replacing all the
# elements under the main diagonal with 0 (zero).

def replace_under_diagonal(matrix: list[list[int]]) -> list[list[int]]:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i > j:
                matrix[i][j] = 0
    return matrix


test_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Replacing under diagonal with 0: ", replace_under_diagonal(test_matrix))


# ex6: a function that receives as a parameter a variable number of lists and a whole number x. Return a list
# containing the items that appear exactly x times in the incoming lists.

def count_items(x: int, *lists: list[Any]) -> list[Any]:
    items_count = {}  # dictionary to store item counts

    for ls in lists:
        for item in ls:
            if item in items_count:
                items_count[item] += 1
            else:
                items_count[item] = 1

    # find items that appear x times
    res = [item for item in items_count if items_count[item] == x]
    return res


list1 = [1, 2, 3]
list2 = [2, 3, 4]
list3 = [4, 5, 6]
list4 = [4, 1, "test"]
x1 = 2
result = count_items(x1, list1, list2, list3, list4)
print(f"Items that appear {x1} times in the list of lists: ", result)


# ex7: a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements.
# The first element of the tuple will be the number of palindrome numbers found in the list and the second element
# will be the greatest palindrome number.

def is_palindrome(number: int) -> bool:
    num_str = str(number)
    return num_str == num_str[::-1]


def palindromes_from_list(numbers: list[int]) -> list[int]:
    palindromes = []
    for number in numbers:
        if is_palindrome(number):
            palindromes.append(number)
    return palindromes


def count_and_greatest_palindrome(numbers: list[int]) -> tuple[int, int]:
    palindromes = palindromes_from_list(numbers)
    return len(palindromes), max(palindromes)


nums = [121, 123, 1331, 55, 12121, 45654, 12345]
print("Number of palindromes and the greatest palindrome from the list: ", count_and_greatest_palindrome(nums))


# ex8: a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set to
# True. For each string, generate a list containing the characters that have the ASCII code divisible by x if the
# flag is set to True, otherwise it should contain characters that have the ASCII code not divisible by x.

def generate_lists_by_ascii_divisibility(x: int = 1, strings: list[str] = None, flag: bool = True) -> list[list[str]]:
    if strings is None:
        strings = []

    result_lists = []

    for string in strings:
        char_list = []

        for char in string:
            ascii_code = ord(char)
            if (ascii_code % x == 0 and flag) or (ascii_code % x != 0 and not flag):
                char_list.append(char)

        result_lists.append(char_list)

    return result_lists


strings_input = ["test", "hello", "lab002"]
flag_input = False
print("Lists generated by ASCII divisibility: ", generate_lists_by_ascii_divisibility(2, strings_input, flag_input))


# ex9: a function that receives as parameter a matrix which represents the heights of the spectators in a stadium and
# will return a list of tuples (line, column) each one representing a seat of a spectator which can't see the game. A
# spectator can't see the game if there is at least one taller spectator standing in front of him. All the seats are
# occupied. All the seats are at the same level. Row and column indexing starts from 0, beginning with the closest
# row from the field.

def seats_with_blocked_view(matrix: list[list[int]]) -> set[tuple[int, int]]:
    obstructed_seats = set()
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            current_height = matrix[i][j]
            for k in range(i + 1, rows):
                if matrix[k][j] <= current_height:
                    obstructed_seats.add((k, j))
    return obstructed_seats


stadium = [
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]
]

print("Seats with blocked view: ", seats_with_blocked_view(stadium))


# ex10: a function that receives a variable number of lists and returns a list of tuples as follows: the first tuple
# contains the first items in the lists, the second element contains the items on the position 2 in the lists,
# etc. Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(1, 5, "a ") ,(2, 6, "b"), (3,7, "c")].

def combine_lists(*lists: list[Any]) -> list[tuple[Any, ...]]:
    max_length = max(len(lst) for lst in lists)

    combined_tuples = []

    for i in range(max_length):
        combined_tuple = tuple(lst[i] if i < len(lst) else None for lst in lists)
        combined_tuples.append(combined_tuple)

    return combined_tuples


l1 = [1, 2, 3]
l2 = [5, 6, 7]
l3 = ["a", "b", "c"]
print("Combined lists: ", combine_lists(l1, l2, l3))


# ex11: a function that will order a list of string tuples based on the 3rd character of the 2nd element in
# the tuple.

def order_list_of_tuples(list_of_tuples: list[tuple[str, str]]) -> list[tuple[str, str]]:
    return sorted(list_of_tuples, key=lambda new_key: new_key[1][2])


tuples_list = [('abc', 'bcd'), ('abc', 'zza')]
print("Ordered list of tuples: ", order_list_of_tuples(tuples_list))


# ex12: a function that will receive a list of words  as parameter and will return a list of lists of words,
# grouped by rhyme. Two words rhyme if both of them end with the same 2 letters.

def group_by_rhyme(words: list[str]) -> list[list[str]]:
    rhymes = {}
    for word in words:
        rhyme = word[-2:]
        if rhyme in rhymes:
            rhymes[rhyme].append(word)
        else:
            rhymes[rhyme] = [word]
    return list(rhymes.values())


print("Words grouped by rhyme: ", group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))
