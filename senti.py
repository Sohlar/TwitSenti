
import vaderSentiment 


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def generateScore(str_input):

    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(str_input)
    return scores