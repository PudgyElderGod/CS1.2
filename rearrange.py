import sys
import random


def rearrange(words):
    if (len(words) <= 1):
        return
    wordsList = words[1:]
    random.shuffle(wordsList)
    return wordsList


if __name__ == '__main__':
    print(str(rearrange(sys.argv)))
