# create tests for EventManager
from candiy.presenter.events import EventID
from candiy.presenter.events_manager import EventManager


def test_event_manager_create_event_trigger():
    event_manager = EventManager()
    command = event_manager.create_event_trigger(EventID.HEARTBEAT)
    assert command is not None


def test_subscribe():
    subscriber_notified = False

    def my_callback():
        nonlocal subscriber_notified
        subscriber_notified = True

    event_manager = EventManager()
    event_manager.subscribe(EventID.HEARTBEAT, my_callback)
    trigger = event_manager.create_event_trigger(EventID.HEARTBEAT)
    assert not subscriber_notified
    trigger()
    assert subscriber_notified


def test_unsubscribe():
    subscriber_notified = False

    def my_callback():
        nonlocal subscriber_notified
        subscriber_notified = True

    event_manager = EventManager()
    event_manager.subscribe(EventID.HEARTBEAT, my_callback)
    trigger = event_manager.create_event_trigger(EventID.HEARTBEAT)
    assert not subscriber_notified
    trigger()
    assert subscriber_notified
    subscriber_notified = False
    event_manager.unsubscribe(EventID.HEARTBEAT, my_callback)
    trigger()
    assert not subscriber_notified
