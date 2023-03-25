from django.urls import path
from .views import article_detail,home


urlpatterns = [
    path('', home, name='home'),
    # path('<slug:slug>/', article_detail, name='article_detail'),
]
