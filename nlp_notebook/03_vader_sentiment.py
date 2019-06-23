import csv
import pandas as pd
import vaderSentiment

# Reference: NLP tutorial with Python Vader package
# https://medium.com/analytics-vidhya/simplifying-social-media-sentiment-analysis-using-vader-in-python-f9e6ec6fc52f

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    print("{:-<40} {}".format(sentence, str(score)))

votes = pd.DataFrame.from_csv('../data/mock-data-05.csv', index_col=None)

for index, row in votes.iterrows():
    sentiment_analyzer_scores(row['comment'])
