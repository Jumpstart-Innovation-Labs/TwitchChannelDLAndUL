from twitchdl import twitch
from twitchdl.exceptions import ConsoleError
from twitchdl.output import print_out, print_video


def _continue():
    print_out(
        "\nThere are more videos. "
        "Press <green><b>Enter</green> to continue, "
        "<yellow><b>Ctrl+C</yellow> to break."
    )

    try:
        input()
    except KeyboardInterrupt:
        return False

    return True


def _get_game_ids(names):
    if not names:
        return []

    game_ids = []
    for name in names:
        print_out("<dim>Looking up game '{}'...</dim>".format(name))
        game_id = twitch.get_game_id(name)
        if not game_id:
            raise ConsoleError("Game '{}' not found".format(name))
        game_ids.append(int(game_id))

    return game_ids


def videos(channel_name, limit=10, sort='time', type='archive', game=None):

    game_ids = _get_game_ids(game)
    print_out("<dim>Loading videos...</dim>")
    generator = twitch.channel_videos_generator(
        channel_name, limit, sort, type, game_ids=game_ids)

    data = []
    first = 0
    error = 0
    try:
        for videos, has_more in generator:
            count = len(videos["edges"]) if "edges" in videos else 0
            total = videos["totalCount"]
            last = first + count - 1

            print_out("-" * 80)
            print_out("<yellow>Showing videos {}-{} of {}</yellow>".format(first, last, total))
            for video in videos["edges"]:
                try:
                    data.append(video['node'])
                except Exception as e:
                    print(e)
                    error += 1

            first += count
        print_out(f"<yellow>{first} Videos Found!</yellow>")
        print_out(f"<red>{error} Errors Found!</error>")
        return data
    except TypeError:
        return []
