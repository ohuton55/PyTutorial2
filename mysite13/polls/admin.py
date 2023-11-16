from django.contrib import admin
from django.views.generic.detail import DetailView
from django.urls import path, reverse
from django.utils.html import format_html

from .models import Question, Choice

# viewとして呼び出す
class QuestionDetailView(DetailView):
    template_name = "admin/polls/question/new_page.html"
    model = Question

class ChoiceInline(admin.TabularInline):
# class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3   # extra ... 余分スロット数


class QuestionAdmin(admin.ModelAdmin):
    # fields = ["pub_date", "question_text"]
    fieldsets = [
            (None, {"fields":["question_text"]}),
            ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
            #classes = ["collapse"] 境界を重ねて並べる
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently","question_new_page"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

    def get_urls(self):
        urls = super().get_urls()   # defaultのadmin urlをロード

        detail_urls = [
            path("new_page/<pk>", self.admin_site.admin_view(QuestionDetailView.as_view()), name=f"new_question_page",)
        ]
        return detail_urls + urls

    def question_new_page(self, obj):
        url = reverse("admin:new_question_page", args=[obj.pk])
        return format_html(f'<a href="{url}">&#x1f4dd</a>')
    
admin.site.register(Question, QuestionAdmin)

