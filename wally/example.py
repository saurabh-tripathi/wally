"""Example script."""
from datetime import datetime


def akiri(param_1: str, param_2: float) -> str:
    """Sample function.

    Place holer method
    :param param_1: dummy parameter 1.
    :param param_2: dummy parameter 2.
    """
    return f"[{datetime.now().isoformat()}] {param_1}: {param_2:.2f}"


def meow() -> str:
    """Another sample method."""
    return "meow!"
