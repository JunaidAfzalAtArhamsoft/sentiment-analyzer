""" This module contain the sentiment analyzer """

from textblob import TextBlob


class MessageClassifier:
    """ Classify message as positive or negative """

    def __init__(self, text='I am very powerful.'):
        self.text = text

    def sentiment(self):
        """ classify text as positive or negative."""

        result = TextBlob(self.text)
        return result.sentiment

    def tokens(self):
        """
        Return tokens of provided text.
        Returns:
            tokens: Tokens of text
        """

        result = TextBlob(self.text)
        return result.words

    def analyze(self) -> str:
        """
            Analyze the tone and return it.
        Returns:
            Tone of statement (str):
        """
        polarity, subjectivity = self.sentiment()

        if polarity > 0.6:
            return 'Highly Positive'
        if polarity > 0.3:
            return 'Positive'
        if polarity > 0:
            return 'Just Fine'
        if polarity == 0:
            return 'Neutral'
        if polarity > -0.3:
            return 'Negative'
        if polarity > -0.6:
            return 'Highly Negative'

        return 'Extremely Negative'
