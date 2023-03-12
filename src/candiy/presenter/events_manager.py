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
        if self.is_already_subscribed(event_id, callback):
            raise ValueError(
                f"Callback {callback} is already subscribed to event {event_id}"
            )
        self._events.setdefault(event_id, []).append(callback)

    def unsubscribe(self, event_id: EventID, callback: callable):
        self._events[event_id].remove(callback)

    def is_already_subscribed(self, event_id: EventID, callback: callable) -> bool:
        return callback in self._events.get(event_id, [])
