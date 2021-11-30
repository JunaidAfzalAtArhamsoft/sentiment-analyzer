""" This module contain the sentiment analyzer """

from textblob import TextBlob


class MessageClassifier:
    """ Classify message as positive or negative """

    def __init__(self, text='I am very powerful.'):
        self.text = text

    def analyze_text(self):
        """ classify text as positive or negative."""

        result = TextBlob(self.text)
        analyzed_data = {}
        for line in result.sentences:
            analyzed_data[line] = [line.sentiment.polarity, line.sentiment.subjectivity]
        return analyzed_data

    def tokens(self):
        """
        Return tokens of provided text.
        Returns:
            tokens: Tokens of text
        """

        result = TextBlob(self.text)
        return result.words

    def analyze(self) -> dict:
        """
            Analyze the tone and return it.
        Returns:
            Tone of statement (str):
        """
        data = self.analyze_text()
        new_data = {}
        for key in data:
            print(data[key][0], data[key][1])
            if data[key][0] > 0.6:
                new_data[key] = 'Highly Positive' + ' ' + str(data[key][0]) + ' ' + str(data[key][1])

            if data[key][0] > 0.3:
                new_data[key] = 'Positive' + ' ' + str(data[key][0]) + ' ' + str(data[key][1])

            if data[key][0] > 0:
                new_data[key] = 'Just Fine' + ' ' + str(data[key][0]) + ' ' + str(data[key][1])

            if data[key][0] == 0:
                new_data[key] = 'Neutral' + ' ' + str(data[key][0]) + ' ' + str(data[key][1])

            if data[key][0] < 0:
                new_data[key] = 'Not Good' + ' ' + str(data[key][0]) + ' ' + str(data[key][1])

            if data[key][0] < -0.3:
                new_data[key] = 'Negative' + ' ' + str(data[key][0]) + ' ' + str(data[key][1])

            if data[key][0] < -0.6:
                new_data[key] = 'Highly Negative' + ' ' + str(data[key][0]) + ' ' + str(data[key][1])

        return new_data
