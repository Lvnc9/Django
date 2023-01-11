import datetime

from django.test import TestCase
from django.utils import timezone
from .models import Question
# Create your tests here.


class QuestionModelTests(TestCase):

    def test_was_published_rencently_with_future_question(self):
        """ 
        was_published_rencently() returns False for question whose pub_date
        is in the future """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(publish_date=time)
        self.assertIn(future_question.was_published_recently(), False)