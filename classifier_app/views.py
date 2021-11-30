""" This module contains Apis to handle Sentiment Analysis on pdf """

import os
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from classifier.sentiment_analyzer import MessageClassifier
from django.views import View
import fitz


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
        data = {
            'data': classifier.analyze(),
        }
        return render(
            request=self.request,
            template_name='classifier_app/result_page.html',
            context=data
        )

    def get(self, request, *args, **kwargs):
        """
        Show Page so that user can input Text.
        """

        return render(
            request=self.request,
            template_name='classifier_app/page.html'
        )


class UploadFile(View):
    """ upload file to server for processing """

    def get(self, request, *args, **kwargs):
        """
        Show Page so that user can input Text.
        """

        return render(
            request=self.request,
            template_name='classifier_app/file_upload.html'
        )

    def post(self, request, *args, **kwargs):
        """
        Get Text from user and return its sentiment

        Returns:
            Html Page
        """

        file = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)

        with fitz.open(filename) as doc:
            text = ""
            for page in doc:
                text += page.getText()
            os.remove(filename)
            classifier = MessageClassifier(text)
            data = {
                'data': classifier.analyze()
            }
            return render(
                request=self.request,
                template_name='classifier_app/result_page.html',
                context=data
            )
