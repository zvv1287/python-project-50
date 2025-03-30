from gendiff.formatter.plain import get_str


def test_get_str():
    true_res = "Property 'common.follow' was added with value: false"
    assert get_str('add', 'common.follow', 'false') == true_res

    true_res = "Property 'common.setting3' was updated. From true to null"
    assert get_str('modife', 'common.setting3', 'true', 'null') == true_res

