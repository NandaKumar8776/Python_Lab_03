#######################################################
# GIVEN CODE

# These 3 functions calculate the cosine similarity for
# any 2 word vectors
def dot_product(vec_a, vec_b):
    dot_prod = 0.0;
    for i in range(len(vec_a)):
        dot_prod += vec_a[i] * vec_b[i]
    return dot_prod

import math
def magnitude(vector):
    return math.sqrt(dot_product(vector, vector))

# The entry point function
def cosine_similarity(vec_a, vec_b):
    dot_prod = dot_product(vec_a, vec_b)
    magnitude_a = magnitude(vec_a)
    magnitude_b = magnitude(vec_b)

    return dot_prod / (magnitude_a * magnitude_b)
#######################################################
# CUSTOM CODE

# Python Lab 3
# Nandakumar Balakrishnan


import time

print("Start time:", time.strftime("%H:%M:%S", time.localtime()))

# Reading the text file
with open('FastText100K.txt', "r", encoding="utf-8") as f:
    lines = f.readlines()

# Initializing a dictionary for storing words with their vectors, and a seperate cosine value dictionary.
word_dictionary = dict()
cosine_dictionary = dict()

# Iterating through the text file to store the words and their associated vector values.
for line in lines:
    line = line.split()
    word_dictionary[line[0]] = [float(i) for i in line[1:]]
    
# Printing out the time take to load the text file.
print("Finish time:", time.strftime("%H:%M:%S", time.localtime()))
print()
print("Word vector dictionary is loaded")
print()

word = 'not null'
similarity_list = []

# Initaling the while loop to request the word(s) from the user.
while word != '':
    print()
    word = input("Enter search word: ")

    # To end loop if no words are entered.
    if word == '':
        break

    # Getting the word vector for the given word.
    given_word_vector = word_dictionary[word]
    
    # Looping through the keys (words) of the dictionary to perform cosine similarity function and store the results in a list. 
    for key in word_dictionary.keys():
        
        iterative_vector = word_dictionary[key]
        cosine_sim = cosine_similarity(given_word_vector,iterative_vector)
        cosine_dictionary[cosine_sim] = key
        similarity_list.append(cosine_sim)
        
    # Sorting the whole cosine similarity list by descending order and indexing, to get the top 5 resemblant words.
    similarity_list.sort(reverse=True)
    most_similar = similarity_list[1:6]
    
    print("The words with the highest cosine similarity are:")

    # Printing out the output.
    for cos in most_similar:
        print(str(cos) +"\t" + cosine_dictionary[cos])

    # To reset the list for the next potential word from user.
    similarity_list = []
