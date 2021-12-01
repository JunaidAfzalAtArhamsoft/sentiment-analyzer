""" This module contains Apis to handle Sentiment Analysis on pdf """

import os
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from classifier.sentiment_analyzer import MessageClassifier
from django.views import View
import fitz
import re


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


class SentimentOfFile(View):
    """ Get file from user for processing"""

    def get(self, request, *args, **kwargs):
        """
        Show Page so that user can input Text.
        """

        return render(
            request=self.request,
            template_name='classifier_app/get_file.html'
        )

    def post(self, request, *args, **kwargs):
        """
        Get pdf from user and return its sentiment

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
            # os.remove(filename)
            classifier = MessageClassifier(text)
            data = {
                'data': classifier.analyze()
            }
            return render(
                request=self.request,
                template_name='classifier_app/result_page.html',
                context=data
            )


class ShowFileOperations(View):
    """ Show operations available on file """

    def get(self, request, *args, **kwargs):
        """ return Page containing operations file """
        return render(
            request=request,
            template_name='classifier_app/file_upload.html',
            context={}
        )


class SearchInFile(View):
    """ Search in file """
    def get(self, request, *args, **kwargs):
        """ get the file and search keyword from user """
        return render(
            request=request,
            template_name='classifier_app/search_in_file.html',
            context={}
        )

    def post(self, request, *args, **kwargs):
        """ show the search results to user """
        file = request.FILES['myfile']
        query = str(self.request.POST.get('query'))
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)

        with fitz.open(filename) as doc:
            text = ""
            page_locations = []
            for page in doc:
                t = page.get_text()
                text += t
                if query in t:
                    page_locations.append(page.number + 1)

            result = text.lower().replace(query, '<b style="color:#008000">{}</b>'.format(query))
            data = {
                'data': text,
                'query': result,
                'page_locations': page_locations,
            }

        return render(
            request=request,
            template_name='classifier_app/search_result_file.html',
            context=data
        )
