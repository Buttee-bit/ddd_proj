from backend.aplications.parser_tg.domain.entity.channel.channel import Channel
from backend.aplications.parser_tg.domain.entity.news.news import News


def convert_channel_entity_to_document(channel: Channel) -> dict:
    return {
        'oid': channel.oid,
        'created_at': channel.created_at,
        'url': channel.url,
    }


def convert_channel_document_to_entity(document: dict) -> Channel:
    return Channel(
        oid=document['oid'],
        created_at=document['created_at'],
        # name=document['name'],
        # description=document['description'],
        url=document['url'],
        # news=document['news'],
    )

def convert_news_entity_to_document(news: News) -> dict:
    return {
        'oid': news.oid,
        'created_at': news.created_at,
        'title': news.title,
        'text': news.text,
        'published_at': news.published_at,
        'oid_channel': news.oid_channel
   }

def convert_news_document_to_entity(document: dict) -> News:
    return News(
        oid=document['oid'],
        created_at=document['created_at'],
        title=document['title'],
        text=document['text'],
        published_at=document['published_at'],
        oid_channel=document['oid_channel'],
    )
