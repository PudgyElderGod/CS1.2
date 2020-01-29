import random
import sys


words = open("/usr/share/dict/words", "r")
words = words.read().split("\n")
sentence_len = int(sys.argv[1])
print(sentence_len)


def random_sentence(sentence_len):
    sentence = []
    for word in range(sentence_len):
        word = random.choice(words)
        sentence.append(word)
    return ' '.join(sentence)


if __name__ == "__main__":
    print(random_sentence(sentence_len))
