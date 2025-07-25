from app.domain.entity.channel.channel import Channel
from app.domain.entity.news.news import News
from app.infra.tracing.handler import trace_custom



def convert_news_entity_to_document(news: News) -> dict:
    return {
        'oid': news.oid,
        'created_at': news.created_at,
        'title': news.title,
        'text': news.text,
        'published_at': news.published_at,
        'oid_channel': news.id_channel
   }

def convert_news_document_to_entity(document: dict) -> News:
    return News(
        oid=document['oid'],
        created_at=document['created_at'],
        title=document['title'],
        text=document['text'],
        published_at=document['published_at'],
        id_channel=document['oid_channel'],
    )
