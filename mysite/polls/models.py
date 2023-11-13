import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    # 質問文フィールド　２００文字まで
    question_text = models.CharField(max_length=200)
    # 発行日　人間可読フィールド
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    # Question modelと関連付け
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 選択文フィールド
    choice_text = models.CharField(max_length=200)
    # 投票　数値フィールド
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
