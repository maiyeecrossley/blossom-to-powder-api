from rest_framework.serializers import ModelSerializer
from ..models import SearchTags

class SearchTagsSerializer(ModelSerializer):
    class Meta:
        model = SearchTags
        fields = "__all__"