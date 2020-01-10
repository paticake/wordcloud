import os
import pandas as pd
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import random

# this reads an image and saves it as img, if you want to add the wordcloud to a personalised background
img=mpimg.imread('') # change this to another image

# this function takes in a colour image and returns a grayscale image
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

# this reads the csv for frequent words and saves it to a a variable called 'df'
df = pd.read_csv('')

# these are the words to ignore in the word cloud
ignore_words = [''] # add ignored words here

# this list will include all words used in all tweets
comment_words = []

# iterate through the rows of the csv provided, csv is in this format word, frequency
for idx, row in df.iterrows():
    # here we check if a word is in the ignore_words list and if it is we
    # don't add it to the comment_words list
    if row.word in ignore_words:
        continue

    for i in range(row.frequency):
        comment_words.append(row.word)

comment_words = " ".join(comment_words)

# here we replace similar words to tidy up the cloud
comment_words = comment_words.replace()

# this makes the wordcloud use the colours of the provided image
image_colors = ImageColorGenerator(img)
# generate the WordCloud object

wc = WordCloud(width=2000, height=1000,
 collocations=False, random_state=1,
 background_color='white', stopwords=[]).generate(comment_words)

# plot the wordcloud object and save as png or svg
plt.figure()
plt.figure( figsize=(20,10) )
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.tight_layout(pad=0)
plt.savefig('wordcloud.svg')
