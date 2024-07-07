import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


# Question模型包括问题描述和发布时间
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # 给Question增加__str__()方法
    def __str__(self):
        return self.question_text

    # # 当 pub_date 为未来某天时，
    # # Question.was_published_recently() 应该返回 False
    # def was_published_recently(self):
    #     now = timezone.now()
    #     return now - datetime.timedelta(days=1) <= self.pub_date <= now
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


# Choice模型有两个字段，选项描述和当前得票数
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # 给模型增加__str__()方法是很重要的，这不仅仅能给你在命令行里使用带来方便，Django自动生成的admin里也使用这个方法来表示对象
    def __str__(self):
        return self.choice_text
