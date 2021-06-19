from typing                         import Optional, List
from django.contrib.postgres.search import SearchQuery, SearchVector

from rest_framework.serializers     import ModelSerializer
from rest_framework.generics        import ListAPIView

from .models                        import YoutubeFeed


def _description_search(search: str) -> Optional[List[YoutubeFeed]]:
    "Helper function to filter Queryset based on given description"

    _vector = SearchVector('description',)
    _search = SearchQuery(search)
    _result = YoutubeFeed.objects.annotate(search=_vector).filter(search=_search)
    return _result


class YoutubeFeedSerializer(ModelSerializer):
    class Meta:
        model = YoutubeFeed
        exclude = ('created_on', 'modified_on')

class YoutubeFeedListView(ListAPIView):
    serializer_class = YoutubeFeedSerializer
    queryset = YoutubeFeed.objects.all()

yt_feed_list = YoutubeFeedListView.as_view()
