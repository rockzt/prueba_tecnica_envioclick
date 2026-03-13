def parse_value(value: str):
    """
    Convert a string value to int, float, or keep it as string.

    Args:
        value: The string value to be parsed.
    Returns:
        The parsed value as int, float, or string.
    """

    try:
        return int(value)
    except ValueError:
        pass

    try:
        return float(value)
    except ValueError:
        pass

    return value