from typing import Optional, List
from django.shortcuts import render
from django.contrib.postgres.search import SearchQuery, SearchVector

from .models import YoutubeFeed


def _description_search(search: str) -> Optional[List[YoutubeFeed]]:
    "Helper function to filter Queryset based on given description"

    _vector = SearchVector('description',)
    _search = SearchQuery(search)
    _result = YoutubeFeed.objects.annotate(search=_vector).filter(search=_search)
    return _result
