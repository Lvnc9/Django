# Start
# Modules
from django.db import models


class Question(models.Model):
    """ question and publish date """
    question_text = models.CharField(max_length=200)
    publish_date = models.DateTimeField("date published")

class Choices(models.Model):
    """ text of choice and voice tally """

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)
    


# End