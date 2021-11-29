from django.http import HttpResponse
from django.shortcuts import render
from classifier.sentiment_analyzer import MessageClassifier
from django.views import View


class AnalyzerApi(View):
    """ Statement classifier Api """

    def post(self, request, *args, **kwargs):
        """
        Get Text from user and return its sentiment

        Returns:
            Html Page
        """

        text = str(self.request.POST.get('text'))
        classifier = MessageClassifier(text)
        content = '<h1> Text: {} <br> Polarity: {}</h1>'.format(
            str(self.request.POST.get('text')),
            classifier.analyze()
        )
        data = {
            'sentiment': classifier.analyze(),
            'text': str(self.request.POST.get('text'))
        }
        context = {'data': data}
        return render(
            request=self.request,
            template_name='classifier_app/result_page.html',
            context=context
        )

    def get(self, request, *args, **kwargs):
        """
        Show Page so that user can input Text.
        """

        return render(
            request=self.request,
            template_name='classifier_app/page.html'
        )
