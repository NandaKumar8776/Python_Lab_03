# Python Lab 3: Cosine Similarity of Word Vectors

## Description
This lab project involves calculating the cosine similarity between word vectors using a given text file, `FastText100K.txt`, which contains word embeddings. The goal is to find and display the top 5 words most similar to a given word based on their cosine similarity.

## Objective
The objective of this lab is to:
1. Load a text file containing word embeddings.
2. Allow the user to input a word.
3. Calculate and display the top 5 words with the highest cosine similarity to the input word.

## Requirements
- Python 3.x
- A text file named `FastText100K.txt` containing word vectors, where each line contains a word followed by its vector components.

## Setup
1. Place the `FastText100K.txt` file in the same directory as this script.
2. Run the Python script using the command:
   ```bash
   python lab3.py
   ```

## Usage
1. Run the script.
2. Enter a word when prompted. The script will then calculate the cosine similarity between the entered word's vector and all other word vectors in the text file.
3. The script will display the top 5 words with the highest cosine similarity to the input word.
4. The process repeats until the user presses Enter without providing a word, which exits the program.

## Code Explanation

### Given Functions
- **`dot_product(vec_a, vec_b)`**: Computes the dot product of two vectors.
- **`magnitude(vector)`**: Calculates the magnitude of a vector.
- **`cosine_similarity(vec_a, vec_b)`**: Computes the cosine similarity between two vectors.

### Custom Code
- **Loading Word Vectors**: 
   - The script reads the `FastText100K.txt` file and stores the words along with their vectors in a dictionary.
   - The loading process is timed to provide insight into performance.
- **Finding Similar Words**:
   - The user is prompted to enter a word.
   - The script calculates the cosine similarity between the input word's vector and all other word vectors.
   - The top 5 words with the highest cosine similarity are displayed.
   - The list is reset for the next word input.

### Important Notes
- The cosine similarity score ranges from -1 to 1, where 1 means the vectors are identical, 0 means they are orthogonal (no similarity), and -1 means they are diametrically opposed.
- The input word must be present in the `FastText100K.txt` file; otherwise, the program will raise a KeyError.

## Example
```
Enter search word: king
The words with the highest cosine similarity are:
0.789  king
0.785  queen
0.780  prince
0.779  monarch
0.777  ruler
```

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## References
- [FastText](https://fasttext.cc/)
- [Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity)
