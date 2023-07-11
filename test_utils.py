import pytest
from utils import translate, get_paragraphs, build_document

def test_get_paragraphs():
    assert all(list(map(lambda paragraph: isinstance(paragraph, str), get_paragraphs("test_material/my_essay_for_test.docx"))))

def test_build_document():
    assert "testing_doc.docx" in build_document(get_paragraphs("test_material/my_essay_for_test.docx"), "testing_doc")

def test_translate():
    assert translate("en", "es", ["Hello World!"]) == ["¡Hola mundo!"]
    assert translate("es", "en", ["Hola Mundo!"]) == ["Hello World!"]
    assert translate("es", "en", ["Hola", "Mundo!"]) == ["Hello.", "World!"]
    assert translate("en", "es", ["Hello", "World!"]) == ["Hola.", "¡Mundo!"]    

pytest.main(["-v", "--tb=line", "-rN", __file__])