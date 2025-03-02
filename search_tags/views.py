from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .models import SearchTags

from .serializers.common import SearchTagsSerializer

class SearchTagsListView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = SearchTags.objects.all()
    serializer_class = SearchTagsSerializer


class SearchTagsDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = SearchTags.objects.all()
    serializer_class = SearchTagsSerializer