from dictogram import Dictogram
import random

class MarkovChain:

    def __init__(self, word_list):


        #The Markov chain will be a DICTIONARY OF DICTIONARIES { {} {} {} {} }
        #Example: for "one fish two fish red fish blue fish"
        #{"one": {fish:1}, "fish": {"two":1, "red":1, "blue":1}, "two": {"fish":1}, "red": {"fish":1}, "blue": {"fish:1"}}
        self.markov_chain = self.build_markov(word_list)
        self.first_word = list(self.markov_chain.keys())[0]

    #1st order markov chain
    def build_markov(self, word_list):
        markov_chain = {}

        #traverse the string
        for i in range(len(word_list) - 1):
            #get the current word and the word after
            current_word = word_list[i]
            next_word = word_list[i+1]

            #checks if current word is in the chain already
            if current_word in markov_chain.keys():
                #get the histogram(dic) for that word in the chain
                histogram = markov_chain[current_word]
                #finds the next_word in the histogram and adds to its weight (chance of it showing up enxt after current word)
                histogram.add_count(next_word)
                #histogram[next_word] = histogram[next_word].add_count(next_word)
            else: #first entry in the chain and creates a new dictionary with next_word as the first entry
                markov_chain[current_word] = Dictogram([next_word])
            print(markov_chain[current_word], "|")

        return markov_chain

    def walk(self, num_words):
        #choose a random key from markov chain and makes a enw string
        sentence = random.choice(list(self.markov_chain))
        #gets the dictionary at that randomized key
        current = self.markov_chain[sentence]
        #loops through to get as many words as num_words specifies
        for num in range(num_words):
            print(current)
            #randomly picks a key from the one of the inner dictionary
            word = current.sample()
            #makes the new current dictionary the dic at the random word
            current = self.markov_chain[word]
            #print(self.markov_chain[word].tokens)
            sentence += " " + word
            #print(sentence)
        return sentence
        

    def print_chain(self):
        for word, histogram in self.markov_chain.items():
            print(word, histogram)



markov_chain = MarkovChain(["one", "fish", "two", "fish", "red", "fish", "blue", "fish"])
markov_chain.print_chain()
print(markov_chain.walk(20))