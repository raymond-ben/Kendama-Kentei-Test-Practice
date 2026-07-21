from dataclasses import dataclass


@dataclass
class Trick:
    """
    Represents one trick in a Kentei class.
    """

    number: int
    name: str

    attempts: int = 0
    completed: bool = False