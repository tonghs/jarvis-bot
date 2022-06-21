from bot.handler import cmd_route


def test_cmd_route():
    def test(*args, **kwargs):
        print(args, kwargs)  # noqa

    cmd_route('test')(test)

    assert len(cmd_route.handler_list) == 1
