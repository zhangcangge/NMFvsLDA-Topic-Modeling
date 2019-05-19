from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.datasets import fetch_20newsgroups
from sklearn.decomposition import NMF, LatentDirichletAllocation

import pickle

# ---------------------------------------Define a function to store the final result in pickle file and display.---------------------------------------
def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        TopicId = "Topic{}".format(topic_idx)
        TopWords = " ".join([feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1]])
        print(TopicId)
        print(TopWords)
        pickle_out = open("{}.pickle".format(TopicId), "wb")
        pickle.dump(TopWords, pickle_out)
        pickle_out.close()

import sklearn
from sklearn import datasets
from pprint import pprint

#---------------------------------------Load the articles form local folder.---------------------------------------
categories = ['Election']
docs_to_train = sklearn.datasets.load_files('./20Articles',
                                            description=None, categories=categories,
                                            load_content=True, encoding="utf-8", shuffle=True, random_state=0)

documents = docs_to_train.data

no_features = 1000 #Define how many features will be used in modeling

#---------------------------------------NMF is able to use tf-idf---------------------------------------
#Change the documents to word count vector, it will count how many times a word shown in a document
tfidf_vectorizer = TfidfVectorizer(max_df=0.90, min_df=2, max_features=no_features, stop_words='english')
tfidf = tfidf_vectorizer.fit_transform(documents)
tfidf_feature_names = tfidf_vectorizer.get_feature_names() #Get the feature list

# print(tfidf_vectorizer.get_feature_names())
# print(tfidf_vectorizer.vocabulary_)
# print(tfidf.toarray())

#---------------------------------------LDA can only use raw term counts for LDA because it is a probabilistic graphical model---------------------------------------
#Change the documents to word count vector
tf_vectorizer = CountVectorizer(max_df=0.90, min_df=2, max_features=no_features, stop_words='english')
tf = tf_vectorizer.fit_transform(documents)
tf_feature_names = tf_vectorizer.get_feature_names() #Get the feature list

no_topics = 1 #Define how many topics want to find

#---------------------------------------Run NMF---------------------------------------
nmf = NMF(n_components=no_topics, random_state=1, alpha=.1, l1_ratio=.5, init='nndsvd').fit(tfidf)
#
#---------------------------------------Run LDA---------------------------------------
lda = LatentDirichletAllocation(n_components=no_topics, max_iter=5, learning_method='online', learning_offset=50.,random_state=0).fit(tf)

no_top_words = 5 #Define how many to to words want to find.
print('--------------------------------NMF result--------------------------------')
display_topics(nmf, tfidf_feature_names, no_top_words)
print('--------------------------------LDA result--------------------------------')
display_topics(lda, tf_feature_names, no_top_words)