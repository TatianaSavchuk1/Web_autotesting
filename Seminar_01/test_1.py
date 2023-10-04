from REST_API import get, get_1
import pytest


def test_step1(get_token):
    result = get(get_token)
    lst = result['data']
    lst_id = [el["id"] for el in lst]
    assert 81803 in lst_id


def test_step2(get_token):
    result = get_1(get_token)
    lst = result['data']
    lst_descr = [el['description'] for el in lst]
    assert 'test description' in lst_descr


if __name__ == '__main__':
    pytest.main(['-v'])

