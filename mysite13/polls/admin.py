from django.contrib import admin
from django.views.generic.detail import DetailView
from django.urls import path, reverse
from django.utils.html import format_html

from .models import Question, Choice

# custom action
@admin.action(description="titleをotherに変更")
def change_question_title(modeladmin, request, queryset):
    queryset.update(question_text='other')

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
    list_display_links = ["pub_date"]
    list_filter = ["pub_date"]
    list_editable = ["question_text"]
    search_fields = ["question_text"]
    actions = [change_question_title]

    def get_urls(self):
        urls = super().get_urls()   # defaultのadmin urlをロード

        new_page_urls = [
            path("new_page/<pk>", self.admin_site.admin_view(QuestionDetailView.as_view()), name=f"new_question_page"),
        ]
        return new_page_urls + urls

    def question_new_page(self, obj):
        url = reverse("admin:new_question_page", args=[obj.pk])
        return format_html(f'<a href="{url}">&#x1f4dd</a>')
        
    
admin.site.register(Question, QuestionAdmin)

