"""A module that does something."""

from test_package_a import method_here as a_method_here
from test_package_b import method_here as b_method_here


def use_both():
    """Use two linked Rez package dependencies at once.

    References:
        - :func:`test_package_a.method_here.do_something`
        - :func:`test_package_b.method_here.do_something`

    """
    a_method_here.do_something()
    b_method_here.do_something()

    print("It works")
