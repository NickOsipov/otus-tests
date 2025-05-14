import pytest

@pytest.mark.skip(reason="Функционал еще не реализован")
def test_new_feature():
    assert new_feature() == "expected result"
