from candiy.presenter.event_manager import EventManager
from candiy.views.main_view import MainView


def test_main_view_update_text():
    view = MainView(EventManager())
    view.update_text("Hello World")
    assert view.status_label.cget("text") == "Hello World"
