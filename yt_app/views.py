from typing                         import Optional, List
from django.contrib.postgres.search import SearchQuery, SearchVector
from rest_framework.response import Response

from rest_framework.serializers     import ModelSerializer
from rest_framework.generics        import ListAPIView

from .models                        import YoutubeFeed


def _data_search(search: str) -> Optional[List[YoutubeFeed]]:
    "Helper function to filter Queryset based on given description"

    if not search:
        return YoutubeFeed.objects.all()

    _vector = SearchVector('description', 'title')
    _search = SearchQuery(search)
    _result = YoutubeFeed.objects.annotate(search=_vector).filter(search=_search)
    return _result


class YoutubeFeedSerializer(ModelSerializer):
    class Meta:
        model = YoutubeFeed
        exclude = ('created_on', 'modified_on')

class YoutubeFeedListView(ListAPIView):
    serializer_class = YoutubeFeedSerializer

    def get_queryset(self):
        _search = self.request.query_params.get("search", None)
        return _data_search(_search)

yt_feed_list = YoutubeFeedListView.as_view()
