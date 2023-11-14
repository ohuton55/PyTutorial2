import datetime
from django.test import TestCase
from django.utils import timezone

from .models import Question

# Create your tests here.

# django.test.TestCaseを継承
class QuestionModelTests(TestCase):
    
    def test_was_published_recently_with_future_question(self):
        # 今から30日後のpub_dateを持つインスタンスを作成
        
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        # .was_published_recently()の出力がfalseかチェック
        self.assertIs(future_question.was_published_recently(), False)

   
    def test_was_published_recently_with_old_question(self):
        # 今から1日と1秒前のpub_dateを持つインスタンスを作成

        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        future_question = Question(pub_date=time)
        # .was_published_recently()の出力がfalseかチェック
        self.assertIs(future_question.was_published_recently(), False)
             

    def test_was_published_recently_with_recent_question(self):
        # 今から23時間59分前のpub_dateを持つインスタンスを作成

        time = timezone.now() - datetime.timedelta(days=23, seconds=59)
        future_question = Question(pub_date=time)
        # .was_published_recently()の出力がfalseかチェック
        self.assertIs(future_question.was_published_recently(), True)
