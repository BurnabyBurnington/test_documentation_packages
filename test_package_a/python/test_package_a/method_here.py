"""An example module with interlinks."""

from dependency import api


def do_something(thing="stuff"):
    """Make a call to :func:`dependency.api.some_function`.

    Args:
        thing (str, optional): Text to either include or not include.

    Returns:
        dependency.api.SomeObject: Some created object.

    """
    if thing == "stuff":
        print(api.some_function(True))

    return api.SomeObject()
