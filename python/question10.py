import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

def count_pos_tags(text):
    # Tokenize the text into individual words
    tokens = word_tokenize(text)

    # Tag each word with its part of speech
    tagged_tokens = pos_tag(tokens)

    # Initialize counts for verbs, nouns, pronouns, and adjectives
    counts = {
        'verbs': 0,
        'nouns': 0,
        'pronouns': 0,
        'adjectives': 0
    }

    # Iterate through the tagged tokens and update the respective counts
    for word, tag in tagged_tokens:
        if tag.startswith('V'):
            counts['verbs'] += 1
        elif tag.startswith('N'):
            counts['nouns'] += 1
        elif tag == 'PRP' or tag == 'PRP$':
            counts['pronouns'] += 1
        elif tag.startswith('JJ'):
            counts['adjectives'] += 1

    return counts

# Example usage
# phrase = str(input())
# counts = count_pos_tags(phrase)
# print(counts)

# Test case I
phrase = 'a quick brown fox jumps over the lazy dog.'
dic1 = count_pos_tags(phrase)
print(dic1)

# Test case II
phrase = "The headphones were on. They had been utilized on purpose. She could hear her mom yelling in the background, but couldn't make out exactly what the yelling was about. That was exactly why she had put them on. She knew her mom would enter her room at any minute, and she could pretend that she hadn't heard any of the previous yelling."
dic2 = count_pos_tags(phrase)
print(dic2)