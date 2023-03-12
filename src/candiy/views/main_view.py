import customtkinter
from candiy.presenter.events import EventID
from candiy.presenter.events_manager import EventManager

from candiy.views.icons import Icons
from candiy.views.view import View


customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")


class MainView(customtkinter.CTk, View):
    def __init__(self, event_manager: EventManager = None):
        super().__init__()
        self.event_manager = event_manager or EventManager()

        # configure window
        self.title("CANDIY")
        self.geometry(f"{1080}x{580}")

        # update app icon
        self.iconbitmap(Icons.LOLLIPOP_ICON.file)

        # create widgets
        self.heartbeat_button = customtkinter.CTkButton(
            self,
            text="Heartbeat",
            command=self.event_manager.create_event_trigger(EventID.HEARTBEAT),
        )
        self.heartbeat_button.pack()
        # create text label to display text
        self.text_label = customtkinter.CTkLabel(self, text="Hello World!")
        self.text_label.pack()

    def update_text(self, text: str):
        self.text_label.configure(text=text)


if __name__ == "__main__":
    MainView().mainloop()
