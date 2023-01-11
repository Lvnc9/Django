# Start
# Modules
from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):
    """ question and publish date """
    question_text = models.CharField(max_length=200)
    publish_date = models.DateTimeField("date published")

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.publish_date <= now

class Choices(models.Model):
    """ text of choice and voice tally """

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)
    


# End