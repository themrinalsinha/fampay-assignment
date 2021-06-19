from typing      import Dict, Tuple
from requests    import Session
from django.db   import IntegrityError
from django.conf import settings

from .celery     import app
from .models     import YoutubeFeed


def _get_key():
    # TODO: add key rotation
    return 'AIzaSyA06wApcx_E8eTFwaCCwWoXeMCtLEKFa9M'

@app.task
def fetch_data(pageToken: str = "", search_query: str = None) -> Tuple[bool, Dict]:
    "Helper function to fetch data from youtube API"

    BASE_URL = "https://www.googleapis.com/youtube/v3/search/"

    KEY = _get_key()
    if not KEY:
        return False, 'No active key found!'

    PARAMS = {
        "part": "snippet",
        "q": search_query or settings.SEARCH_QUERY,
        "key": KEY,
        "maxResults": int(settings.QUERY_PER_PAGE),
        "pageToken": pageToken,
    }

    with Session() as session:
        with session.get(BASE_URL, params=PARAMS) as response:
            _data = response.json()

            if response.status_code == 200:
                for item in _data.get('items', []):
                    payload = {}

                    _snippet = item.get('snippet')
                    payload.setdefault('title', _snippet.get('title'))
                    payload.setdefault('description', _snippet.get('description'))
                    payload.setdefault('thumbnails', _snippet.get('thumbnails'))
                    payload.setdefault('published_at', _snippet.get('publishedAt'))

                    payload.setdefault('meta_info', {})
                    payload['meta_info'].setdefault('channel_id', _snippet.get('channelId'))
                    payload['meta_info'].setdefault('id', _snippet.get('id'))
                    payload['meta_info'].setdefault('channel_title', _snippet.get('channelTitle'))
                    payload['meta_info'].setdefault('live_broadcast', _snippet.get('liveBroadcastContent'))

                    try:
                        YoutubeFeed.objects.get_or_create(
                            video_id=item['id']['videoId'],
                            defaults={**payload}
                        )
                    except IntegrityError:
                        ...

                return True, _data

                # NOTE: Avoiding recursive call.
                # _next_page = _data.get("prevPageToken", None)
                # if _next_page:
                #     yield _fetch_data(_next_page)
            else:
                return False, _data
