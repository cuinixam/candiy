from typing import Protocol


class View(Protocol):
    def update_text(self, text: str):
        ...
