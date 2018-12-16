from django.contrib import admin
from django.urls import path
from polls import views

# django.conf.urls __init__.py
# url(regex, view, kwargs=None, name=None, prefix='')
# polls/3/detail

app_name = 'polls'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', views.index, name='index'),
    path('polls/<int:question_id>/', views.detail, name='detail'),
    path('polls/<int:question_id>/vote/', views.vote, name='vote'),
    path('polls/<int:question_id>/results/', views.results, name='results'),
]
