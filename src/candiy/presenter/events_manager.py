from typing import Dict, List

from candiy.presenter.events import EventID


class EventManager:
    """Manages events and their subscribers."""

    def __init__(self):
        self._events: Dict[EventID, List[callable]] = {}

    def create_event_trigger(self, event_id: EventID) -> callable:
        return lambda: self._trigger_event(event_id)

    def _trigger_event(self, event_id: EventID):
        for callback in self._events.get(event_id, []):
            callback()

    def subscribe(self, event_id: EventID, callback: callable):
        self._events.setdefault(event_id, []).append(callback)

    def unsubscribe(self, event_id: EventID, callback: callable):
        self._events[event_id].remove(callback)
