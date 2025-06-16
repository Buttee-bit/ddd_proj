from backend.aplications.parser_tg.domain.entity.channel.channel import Channel


def convert_channel_entity_to_document(channel: Channel) -> dict:
    return {
        'oid': channel.oid,
        'created_at': channel.created_at,
        'url': channel.url,
        'subscribers': channel.subscribers,
        'title': channel.title,
        'id_channel': channel.id_channel,
    }

def convert_channel_document_to_entity(document: dict) -> Channel:
    return Channel(
        oid=document['oid'],
        created_at=document['created_at'],
        url=document['url'],
        subscribers=document.get('subscribers', 0),
        id_channel=document.get('id_channel', 0),
        title=document.get('title', '')
    )