import operator

# This function calculates the NGram of a given string.
# The time complexity of this algorithm is O(k(n - k)) where n is the length of the String and k the length of
# the desired NGram. This because the iteration takes into account just n - k characters of the String, so the full
# String is never iterated. The k multiplies n - k because the complexity of Python's string slicing is O(k), where
# k is the length of the desired substring.
# It is important to mention that when the length of the string is the same than the length of the
# desired NGram the complexity will be O(1) as the for instruction is omitted.

def calculateNGrams(text, n):
    nGrams = []
    if n == len(text):
        nGrams.append(text)
    else:
        for char_index in range(0, len(text) - n + 1):
            nGrams.append(text[char_index:char_index + n])
    return nGrams

# This function calculates the most common NGram of a given string.
# The time complexity of this algorithm is O(k(n - k)) taking into consideration that Python's native dictionary
# functions of getting and setting values on the dictionary have a time complexity of O(1) on the best cases.
# On the worst case, the algorithm has a time complexity of O(knˆ2) - O(nkˆ2). Both complexities taking into account
def mostFrequentNGram(text, n):
    nGram_dict = {}

    max = -1
    ngram = ''

    if n == len(text):
        max = text
    else:
        for char_index in range(0, len(text) - n + 1):
            if nGram_dict.get(text[char_index:char_index + n]) is None:
                nGram_dict[text[char_index:char_index + n]] = 1
            else:
                nGram_dict[text[char_index:char_index + n]] += 1
                if nGram_dict[text[char_index:char_index + n]] > max:
                    max = nGram_dict[text[char_index:char_index + n]]
                    ngram = text[char_index:char_index + n]

    return ngram


