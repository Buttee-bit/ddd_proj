from backend.domain.values.title import Title



def test_title_value_object():
    title = Title('Test Title')
    assert title.value == 'Test Title'