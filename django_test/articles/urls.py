from django.conf.urls import include,url
from django.contrib import admin
from articles import views
from articles.views import HelloTemplate
from api import ArticleResource

article_resource = ArticleResource()


urlpatterns = [
    url(r'^all/',views.articles,name='articles'),
    url(r'^get/(?P<article_id>\d+)/',views.article,name='article'),
    url(r'^language/(?P<language>[a-z\-]+)/',views.language,name='language'),
    url(r'^create/',views.create,name='create'),
    url(r'^like/(?P<article_id>\d+)/',views.like_article,name='like_article'),
    url(r'^add_comment/(?P<article_id>\d+)/',views.add_comment,name='add_comment'),
    url(r'^search/',views.search_titles,name='search_titles'),
    url(r'^api/',include(article_resource.urls)),
    ]  
