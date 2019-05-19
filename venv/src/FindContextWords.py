import pickle

#Load the determine words from pickle file.
pickle_in = open("Topic0.pickle", "rb")
Topic0 = pickle.load(pickle_in)
pickle_in.close()

Topic0 = Topic0.split(" ")

print("The {} determine words of dorminant topic are [{}].".format(len(Topic0), Topic0))
print("----------------------------------------------------------------------------------------------")

import sklearn
from sklearn import datasets
from pprint import pprint

#---------------------------------------Load the articles form local folder.---------------------------------------
categories = ['Election']
docs_to_train = sklearn.datasets.load_files('./20Articles',
                                            description=None, categories=categories,
                                            load_content=True, encoding="utf-8", shuffle=True, random_state=0)

documents = docs_to_train.data

#---------------------------------------Split the documents to sentence list---------------------------------------
sentences = []
for document in documents:
    sentences.append(document.split("."))

#---------------------------------------Define a method to remove stop words from documents---------------------------------------
from nltk.corpus import stopwords
def remove_stop_words(corpus):
    #----------------------Since the preposition words could keep the logic between words,
    #----------------------this task finally decide only remove 'a' and 'the' when chose context words.
    #----------------------However, when show the final result (most commen context words),
    #----------------------it will discard all stop words of english
    # stop_words = stopwords.words('english')
    stop_words = ['the', 'a', "The", 'A']
    results = []
    for sentence in sentences:
        for txt in sentence:
            tmp = txt.strip("\n").split(" ")
            for stop_word in stop_words:
                while stop_word in tmp:
                    tmp.remove(stop_word)
            results.append(" ".join(tmp))

    return results

#---------------------------------------Remove stop words---------------------------------------
corpus = remove_stop_words(documents)

#---------------------------------------Find 5 context words before and after each determine words respectively---------------------------------------..
WINDOW_SIZE = 5

data = []
for topWord in Topic0:
    contexts = []
    contexts.append(topWord)
    for txt in corpus:
        tmp = txt.split(" ")
        for idx, word in enumerate(tmp):
            if topWord.lower() == word.lower():
                contexts.append(tmp[max(idx - WINDOW_SIZE, 0): min(idx + WINDOW_SIZE, len(tmp)) + 1])
    data.append(contexts)

# import nltk
# nltk.download("stopwords")

from collections import Counter

print("---------------------------The most common context words for each determine words shown as below---------------------------")
noiseWord = ['', 'would', 'said'] # These words are too common, thus here will remove them from result
for context in data:
    print(context[0])
    contextwords = []
    for words in context:
        # print(words)
        for word in words:
            if word in stopwords.words("english"): # Remove all english stop words
                continue
            if word in noiseWord: # Remove the noise words
                continue
            contextwords.append(word)
    print(Counter(contextwords))
    print("-----------------------------------------------------------------------------------------------------")