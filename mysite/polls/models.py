from django.db import models

# Create your models here.
class Question(models.Model):
    # 質問文フィールド　２００文字まで
    question_text = models.CharField(max_length=200)
    # 発行日　人間可読フィールド
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    # Question modelと関連付け
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 選択文フィールド
    choice_text = models.CharField(max_length=200)
    # 投票　数値フィールド
    votes = models.IntegerField(default=0)
