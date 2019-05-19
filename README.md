# NMFvsLDA-Topic-Modeling
Besides topic modeling, this project also will find the 5 common context words of the determine words of each topic

# General description
It contain two 'py' file, NMFvsLDA-Topic-Modeling.py and FindContextWords.py.
It also contain a folder "20Articles" that collected today news about "Australian election" from different website.

#-------------------------------------------First step-------------------------------------------

Run NMFvsLDA-Topic-Modeling.py first, 
it will build two models based on NMF and LDA respectively, to find the most important topic.
it will find and store the 5 determine words of dominant topic to a pickle file.
The terminal result shown as below:

--------------------------------NMF result--------------------------------
Topic0
labor shorten morrison coalition election
--------------------------------LDA result--------------------------------
Topic0
labor morrison election coalition shorten

     
#-------------------------------------------Sencond step-------------------------------------------

Then, run FindContextWords.py,
it will load the pickle file that was created in first step,
and find the 5 most common context words for each determine words.
The terminal result shown as below:

as shown in red box, except 'Labor' (one determine word) itself, the most 5 common context words for labor are 'leader', 'win', 'seats', 'victory', and 'Party',
and the number after each words is shown how many times a context word shown around labor.

The 5 determine words of dorminant topic are [['labor', 'morrison', 'election', 'coalition', 'shorten']].
----------------------------------------------------------------------------------------------
---------------------------The most common context words for each determine words shown as below--------------------------
labor
Counter({'Labor': 138, 'leader': 12, 'win': 10, 'seats': 8, 'victory': 7, 'Party': 7, 'next': 7, 'Shorten': 6, '$1': 6, -
-----------------------------------------------------------------------------------------------------
morrison
Counter({'Morrison': 73, 'Scott': 28, 'Minister': 8, 'Prime': 7, 'Mr': 7, 'called': 6, 'victory': 5, 'Liberal': 5, 
-----------------------------------------------------------------------------------------------------
election
Counter({'election': 64, 'campaign': 9, 'Coalition': 6, 'Labor': 6, 'victory': 6, 'result': 6, 'night': 5, 'two': 4, 
-----------------------------------------------------------------------------------------------------
coalition
Counter({'Coalition': 55, 'coalition': 16, 'election': 7, 'seats': 6, 'ruling': 5, 'Liberal-National': 5, 'Liberal': 5, 
-----------------------------------------------------------------------------------------------------
shorten
Counter({'Shorten': 55, 'Bill': 17, 'Labor': 6, 'announced': 5, 'Party': 4, 'prime': 4, 'end': 3, 'Morrison': 3, 
-----------------------------------------------------------------------------------------------------
