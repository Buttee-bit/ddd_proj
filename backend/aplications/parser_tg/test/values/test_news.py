from backend.aplications.parser_tg.domain.values.news.title import Title

def test_title_value_object():
    title = Title('Test Title')
    assert title.value == 'Test Title'