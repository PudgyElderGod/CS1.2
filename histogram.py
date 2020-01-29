import sys
import random


def histogram(source_text):
    source_text = open(source_text)
    source_text = source_text.read().replace("\n", '').split(" ")
    word_frequency = dict()

    for word in source_text:
        word = word.lower()
        if word in word_frequency.keys():
            word_frequency[word] += 1
            pass

        elif word == '':
            pass

        elif word not in word_frequency.keys():
            if "." in word:
                word = word.strip(".")
                word_frequency.update({word: 1})
                pass

            else:
                word_frequency.update({word: 1})
                pass

        else:
            pass

    weighted_histo = {}
    total_items = len(word_frequency.values())
    for key, value in word_frequency.items():
        value = value / total_items
        weighted_histo.update({f"{key}": float(f"{value}")})
    return weighted_histo


def histogram_randomizer(histogram):
    words = []
    for word in histogram(source_text):
        words.append(word)
    return random.choice(words)


if __name__ == "__main__":
    source_text = sys.argv[1]
    print(histogram(source_text))
