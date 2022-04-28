def some_function(allowed):
    """Get some string back.

    Args:
        allowed (bool):
            If True, return a string. If False, return another string.

    Returns:
        str: Some string.

    """
    if allowed:
        return "foo"

    return "bar"
