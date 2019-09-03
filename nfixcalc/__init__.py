from enum import Enum

__version__ = '0.1.0'


class Mode(Enum):
    """
    Different calculator modes.
    """
    INFIX = 0
    PREFIX = 1
    POSTFIX = 2

    def __str__(self) -> str:
        return self.name.title()

    @property
    def key_text(self) -> str:
        """
        Text to be displayed on the GUI button.
        """
        if self is Mode.INFIX:
            return "(", ")"
        else:
            return "Enter ↑", ""
