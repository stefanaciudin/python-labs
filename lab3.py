# ex1: a function that receives as parameters two lists a and b and returns a list of sets containing: (an intersected
# with b, a reunited with b, a - b, b - a)
from typing import Any


def set_operations(a: list[Any], b: list[Any]) -> list[set[Any]]:
    intersection = set(a) & set(b)
    union = set(a) | set(b)
    difference_a_b = set(a) - set(b)
    difference_b_a = set(b) - set(a)

    result = [intersection, union, difference_a_b, difference_b_a]
    return result


list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]

result_sets = set_operations(list_a, list_b)
print("Intersection:", result_sets[0])
print("Union:", result_sets[1])
print("A - B:", result_sets[2])
print("B - A:", result_sets[3])


# ex2: a function that receives a string as a parameter and returns a dictionary in which the keys are the characters
# in the character string and the values are the number of occurrences of that character in the given text.

def count_occurrences(text: str) -> dict[str, int]:
    occurrences = {}
    for char in text:
        if char in occurrences:
            occurrences[char] += 1
        else:
            occurrences[char] = 1
    return occurrences


example = "Ana has apples"
print("Occurrences in example 'ana has apples':", count_occurrences(example))


# ex3:  compare two dictionaries without using the operator "==" returning True or False. (Attention, dictionaries
# must be recursively covered because they can contain other containers, such as dictionaries, lists, sets, etc.)

def compare_dicts(d1: dict[Any, Any], d2: dict[Any, Any]) -> bool:
    if len(d1) != len(d2):
        return False

    for key in d1:
        if key not in d2:
            return False
        if type(d1[key]) == dict and type(d2[key]) == dict:
            if not compare_dicts(d1[key], d2[key]):
                return False
        elif d1[key] != d2[key]:
            return False
    return True


d11 = {"a": {"d": [1, 2, 3], "e": 7}, "b": 2, "c": 3}
d12 = {"a": {"d": (1, 2, 3), "e": 7}, "b": 2, "c": 3}
d13 = {"a": {"d": [1, 2, 3], "e": 7}, "b": 2, "c": 3}
d14 = {"a": {"d": [1, 2, 3], "e": 7}, "b": 2, "c": 3, "f": 1344}
d15 = {"a": {"d": [1, 2, 3], "e": 7}, "b": 2, "c": [1, 2, 3]}
d16 = {"a": {"d": [1, 2, 3], "e": 7}, "b": 2, "c": [1, 2, 3]}
print("d1 == d2:", compare_dicts(d11, d12))
print("d1 == d3:", compare_dicts(d11, d13))
print("d11 == d14:", compare_dicts(d11, d14))
print("d15 == d16:", compare_dicts(d15, d16))


# ex4:The build_xml_element function receives the following parameters: tag, content, and key-value elements given as
# name-parameters. Build and return a string that represents the corresponding XML element. Example:
# build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ") returns
# the string = "<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"

def build_xml_element(tag: str, content: str, **attributes: str) -> str:
    attribute_string = " ".join([f'{key}="{value}"' for key, value in attributes.items()])
    xml_element = f"<{tag} {attribute_string}>{content}</{tag}>"
    return xml_element


res = build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
print(res)


# ex5:  The validate_dict function that receives as a parameter a set of tuples ( that represents validation rules
# for a dictionary that has strings as keys and values) and a dictionary. A rule is defined as follows: (key,
# "prefix", "middle", "suffix"). A value is considered valid if it starts with "prefix", "middle" is inside the value
# (not at the beginning or end) and ends with "suffix". The function will return True if the given dictionary matches
# all the rules, False otherwise.

def validate_dict(rules: set[tuple[str, str, str, str]], dictionary: dict[str, str]) -> bool:
    for rule in rules:
        key, prefix, middle, suffix = rule
        if key not in dictionary:
            return False
        if not dictionary[key].startswith(prefix):
            return False
        if not dictionary[key].endswith(suffix):
            return False
        if middle not in dictionary[key]:
            return False
    return True


r = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
dic = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
print("Dictionary is valid:", validate_dict(r, dic))


# ex6: Write a function that receives as a parameter a list and returns a tuple (a, b), representing the number of
# unique elements in the list, and b representing the number of duplicate elements in the list (use sets to achieve
# this objective).

def count_unique_and_duplicates(input_list):
    # create a set to store unique elements
    unique_set = set()

    # create a set to store duplicate elements
    duplicate_set = set()

    for item in input_list:
        if item in unique_set and item not in duplicate_set:
            duplicate_set.add(item)
        else:
            unique_set.add(item)

    # calculate unique items (appear only once)
    unique_items = [item for item in input_list if input_list.count(item) == 1]

    return unique_items, list(duplicate_set)


# Example usage:
my_list = [1, 2, 2, 3, 4, 4, 5, 5, 6, 8, 9, 9, 9, 9, 9, 9, 9]
result = count_unique_and_duplicates(my_list)
print("Unique items:", result[0])
print("Duplicate items:", result[1])


# ex7: Write a function that receives a variable number of sets and returns a dictionary with the following
# operations from all sets two by two: reunion, intersection, a-b, b-a. The key will have the following form: "an op
# b", where a and b are two sets, and op is the applied operator: |, &, -.

def set_operations(*sets: set[Any]) -> dict[str, set[Any]]:
    operations = {}
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            operations[f"{sets[i]} | {sets[j]}"] = sets[i] | sets[j]
            operations[f"{sets[i]} & {sets[j]}"] = sets[i] & sets[j]
            operations[f"{sets[i]} - {sets[j]}"] = sets[i] - sets[j]
            operations[f"{sets[j]} - {sets[i]}"] = sets[j] - sets[i]
    return operations


print("Dictionary with set operations: ", set_operations({1, 2}, {2, 3}))


# ex8:  Write a function that receives a single dict parameter named mapping. This dictionary always contains a
# string key "start". Starting with the value of this key you must obtain a list of objects by iterating over mapping
# in the following way: the value of the current key is the key for the next value, until you find a loop (a key that
# was visited before). The function must return the list of objects obtained as previously described.

def get_values(mapping: dict[str, str]) -> list[str]:
    values = []
    current_key = "start"
    while current_key not in values:
        if current_key != "start":
            values.append(current_key)
        current_key = mapping[current_key]
    return values


print("Returned list of objects: ",
      get_values({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))


# ex9: Write a function that receives a variable number of positional arguments and a variable number of keyword
# arguments and will return the number of positional arguments whose values can be found among keyword arguments values.

def count_positional_in_keyword(*args: Any, **kwargs: Any) -> int:
    count = 0
    for arg in args:
        if arg in kwargs.values():
            count += 1
    return count


print("Number of positional arguments that cam be found among keyword arguments values:",
      count_positional_in_keyword(1, 2, 3, 4, x=1, y=2, z=3, w=2134))
