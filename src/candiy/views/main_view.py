import customtkinter
from candiy.presenter.events import EventID
from candiy.presenter.events_manager import EventManager

from candiy.views.icons import Icons


customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")


class MainView(customtkinter.CTk):
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

    def heartbeat(self):
        print("Heartbeat")


if __name__ == "__main__":
    MainView().mainloop()
