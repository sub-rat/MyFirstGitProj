def capitalize_and_ascii_sum(word: str):
    """
    This method capitalizes the word and finds out the sum of ASCII value of
    all characters of a word
    """
    return sum(ord(x) for x in word.capitalize())


animals = ['cat', 'dog', 'cow']
## normal way
# animal_output = []

# for animal in animals:
#     asci_value = capitalize_and_ascii_sum(animal)
#     animal_output.append(asci_value)

# print(animal_output)

#using map
animal_output = list(map(capitalize_and_ascii_sum, animals))
print(animal_output)
