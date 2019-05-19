# NMFvsLDA-Topic-Modeling
Besides topic modeling, this project also will find the 5 common context words of the determine words of each topic

# General description
It contain two 'py' file, NMFvsLDA-Topic-Modeling.py and FindContextWords.py.
It also contain a folder "20Articles" that collected today news about "Australian election" from different website.

#-------------------------------------------First step-------------------------------------------
Run NMFvsLDA-Topic-Modeling.py first, 
it will build two models based on NMF and LDA respectively,
it will find and store the 5 determine words of dominant topic to a pickle file.
The terminal result shown as below figure:



     
#-------------------------------------------Sencond step-------------------------------------------
Then, run FindContextWords.py,
it will load the pickle file that was created in first step,
and find the 5 most common context words for each determine words.
The terminal result shown as below figure:

as shown in red box, except 'Labor' (one determine word) itself, the most 5 common context words for labor are 'leader', 'win', 'seats', 'victory', and 'Party',
and the number after each words is shown how many times a context word shown around labor.

