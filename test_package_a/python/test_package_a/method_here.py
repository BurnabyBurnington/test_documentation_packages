"""An example module with interlinks."""

from dependency import api


def do_something():
    """Make a call to :func:`dependency.api.some_function`."""
    print(api.some_function(True))
