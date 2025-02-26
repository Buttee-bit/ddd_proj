from backend.aplications.parser_tg.domain.entity.channel.channel import Channel


def convert_entity_to_document(channel: Channel) -> dict:
    return {
        'oid': channel.oid,
        'created_at': channel.created_at,
        'name': channel.name,
        'description': channel.description,
        'url': channel.url,
        'news': channel.news,
    }


def convert_document_to_entity(document: dict) -> Channel:
    return Channel(
        oid=document['oid'],
        created_at=document['created_at'],
        name=document['name'],
        description=document['description'],
        url=document['url'],
        news=document['news'],
    )