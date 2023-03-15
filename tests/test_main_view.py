import pytest

from candiy.presenter.event_manager import EventManager
from candiy.views.main_view import MainView


@pytest.mark.skip(
    reason="For some reason it fails on Ubuntu when initializing the tkinter.Tk.",
)
def test_main_view_update_text():
    view = MainView(EventManager())
    view.update_text("Hello World")
    assert view.status_label.cget("text") == "Hello World"
    assert view.root is None
