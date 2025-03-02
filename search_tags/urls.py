from django.urls import path
from .views import SearchTagsListView, SearchTagsDetailView

urlpatterns = [
    path('', SearchTagsListView.as_view()),
    path('<int:searchtags_id>', SearchTagsDetailView.as_view())
]