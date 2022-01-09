from my_lib.hello_world import hello_world


def test_hello_world():
    a_very_long_list = [
        "some",
        "very",
        "long",
        "list",
        "of",
        "variables",
        "that",
        "will",
        "go",
        "to",
        "the",
        "edge",
    ]
    a_dict = {
        "a": 1,
        "b": 2,
        "c": 3,
    }

    returned_list, returned_dict = hello_world()

    assert a_very_long_list == returned_list
    assert a_dict == returned_dict
