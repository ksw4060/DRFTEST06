from django.contrib import admin
from articles.models import TodoArticle


# Now register the new ArticleAdmin...
admin.site.register(TodoArticle)
