def capitalize_and_ascii_sum(word: str):
    """
    This method capitalizes the word and finds out the sum of ASCII value of
    all characters of a word
    
    """
    return sum(ord(x) for x in word.capitalize())


animals = ['cat', 'dog', 'cow']
#using map
animal_output = list(map(capitalize_and_ascii_sum, animals))
print(animal_output)

## normal way
# animal_output = []

# for animal in animals:
#     asci_value = capitalize_and_ascii_sum(animal)
#     animal_output.append(asci_value)

# print(animal_output)

def square(x):
    return x**2
# lambda x: x ** 2

numbers = [1, 2, 3, 4, 5]

squares = map(lambda x: x ** 2, numbers)
print(list(squares))  # [1, 4, 9, 16, 25]