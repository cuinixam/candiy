from typing import Protocol
from candiy.presenter.events_manager import EventManager
from candiy.views.view import View


class Presenter(Protocol):
    def __init__(self, view: View, event_manager: EventManager):
        ...
