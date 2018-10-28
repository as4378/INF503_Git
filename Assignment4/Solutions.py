import sys
import random


# Question 1 part A
def calculate_average():
    total_sum = 0
    for i in range(1000):
        num = 100
        count = 0
        while num > 5:
            num = random.randint(1, 1000)
            count += 1
        total_sum += count
    return total_sum / 1000


# Question 1 part B
def calculate_average_num_of_success():
    total_sum = 0

    for i in range(1000):  # number of times experiment is performed
        for j in range(10000):  # number of trials
            num = random.randint(1, 1000)
            if num <= 5:
                total_sum += 1

    return total_sum / 1000


# Question 2 part A
def generate_random_fragments(file_name):
    file = open(file_name, "r")
    characters = []
    hash_table = {}  # for storing the 16-mer fragments

    total_unique = 0

    file.readline()  # skipping the first header line

    # read file one character at a time and store it in a list
    character = file.read(1)
    while character:
        characters.append(character)
        character = file.read(1)

    # filter the list to store only characters representing bases in genome
    characters = [c for c in characters if ((c == 'A') or (c == 'C') or (c == 'G') or (c == 'T'))]

    for k in range(100):
        for i in range(100000):
            index = random.randint(0, len(characters) - 15)  # this serves as starting index for fragment
            fragment = ''.join(characters[index:(index + 16)])

            if fragment not in hash_table:
                hash_table[fragment] = True

        total_unique += len(hash_table)
        hash_table = {}

    return total_unique / 100


# Question 2 part B and C
def generate_random_fragments_with_error(file_name, error_rate):
    file = open(file_name, "r")
    characters = []
    hash_table = {}  # for storing the 16-mer fragments
    total_unique = 0

    file.readline()  # skipping the first header line

    character = file.read(1)
    while character:
        characters.append(character)
        character = file.read(1)

    # filter the list to store only characters representing bases in genome
    characters = [c for c in characters if ((c == 'A') or (c == 'C') or (c == 'G') or (c == 'T'))]

    for k in range(100):
        for i in range(100000):
            index = random.randint(0, len(characters) - 15)  # this serves as starting index for fragment

            temp_list = [flip(c, error_rate) for c in characters[index:(index + 16)]]
            fragment = ''.join(temp_list)

            if fragment not in hash_table:
                hash_table[fragment] = True

        total_unique += len(hash_table)
        hash_table = {}

    return total_unique / 100


# utility function
def flip(character, error_rate):
    num = random.randint(1, 100)
    if num <= error_rate:
        if character == 'A':
            return 'C'
        elif character == 'C':
            return 'G'
        elif character == 'G':
            return 'T'
        elif character == 'T':
            return 'A'

    return character


# driver program
if __name__ == '__main__':

    file_name = sys.argv[1]
    part = sys.argv[2]

    if part == 'A':
        print(calculate_average())
    elif part == 'B':
        print(calculate_average_num_of_success())
    elif part == 'C':
        print(generate_random_fragments(file_name))
    elif part == 'D':
        print(generate_random_fragments_with_error(file_name, 1))
    elif part == 'E':
        print(generate_random_fragments_with_error(file_name, 5))
    else:
        print("invalid option")


