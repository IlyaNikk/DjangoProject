from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

0
import datetime

# Create your models here.

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-question_added_at')

    def rat(self):
        return self.order_by('-question_rank')

    def newAns(self,id):
        return self.order_by('-answer_added_at').filter(question_id = id)

    def getbytag(self,tag):
        return self.filter(question_tag__tag_question = tag).order_by('-question_added_at')

    def search_for_username(self,this_username):
        return self.filter(username = this_username)



class Profile(models.Model):
    profile = models.OneToOneField(User)
    profile_avatar = models.ImageField()
    objects = QuestionManager()
    def __str__(self):
        return self.profile_login

class Tags_Question(models.Model):
    tag_question = models.CharField(max_length = 255)
    objects = QuestionManager()
    def __str__(self):
        return self.tag_question

class Question(models.Model):
    profile = models.ForeignKey(User)
    question_title = models.CharField(max_length = 255)
    question_text = models.CharField(max_length = 255)
    question_num_answers = models.IntegerField()
    question_rank = models.IntegerField()
    question_added_at = models.DateTimeField(default = datetime.datetime.now)
    question_tag = models.ManyToManyField(Tags_Question)
    objects = QuestionManager()
    # list(question.tags_question_set)
    def __str__(self):
        return self.question_title


class Answer(models.Model):
    question = models.ForeignKey(Question)
    profile = models.ForeignKey(User)
    answer_text = models.CharField(max_length = 255)
    answer_rank = models.CharField(max_length = 255)
    answer_added_at = models.DateTimeField(default = datetime.datetime.now)
    def __str__(self):
        return self.answer_title


class Liked_Question(models.Model):
    profile = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    what_pressed = models.BooleanField()
    def __str__(self):
        return self.what_pressed

    # unique_together







