import customtkinter
from tkinter import END, NO, W
from tkinter import ttk
from typing import Any, Callable, Dict, List, Union

from candiy.presenter.events import EventID
from candiy.presenter.event_manager import EventManager
from candiy.views.icons import Icons
from candiy.views.view import View


customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")


class TraceViewData:
    headings = ["ID", "DLC", "Data", "Channel"]

    def __init__(
        self, id: str, dlc: str, data: List[str], channel: str, timestamp: str
    ) -> None:
        self.id = id
        self.dlc = dlc
        self.data = data
        self.channel = channel
        self.timestamp = timestamp

    def __eq__(self, other):
        return (
            self.id,
            self.dlc,
            self.data,
            self.channel,
            self.timestamp,
        ) == (
            other.id,
            other.dlc,
            other.data,
            other.channel,
            other.timestamp,
        )


class ToggleButton(customtkinter.CTkButton):
    def __init__(
        self,
        master: Any,
        image_on: Icons = Icons.TOGGLE_ON,
        image_off: Icons = Icons.TOGGLE_OFF,
        text: str = "",
        command: Union[Callable[[], None], None] = None,
    ):
        self.state: bool = False
        self.image_on = image_on.image
        self.image_off = image_off.image
        self._user_command = command
        super().__init__(
            master,
            text=text,
            command=self.command,
            fg_color="transparent",
            border_spacing=0,
            hover_color=("gray70", "gray30"),
            compound="top",
            image=self.image_off,
        )

    def command(self):
        self.state = not self.state
        if self.state:
            self.configure(image=self.image_on)
        else:
            self.configure(image=self.image_off)
        if self._user_command:
            self._user_command()

    def add_user_command(self, command: Callable[[], None]):
        self._user_command = command


class MainView(customtkinter.CTk, View):
    def __init__(self, event_manager: EventManager = None):
        super().__init__()
        self.event_manager = event_manager or EventManager()
        self.messages: Dict[str, TraceViewData] = {}

        # configure window
        self.title("CANDIY")
        self.geometry(f"{1080}x{580}")

        # update app icon
        self.iconbitmap(Icons.LOLLIPOP_ICON.file)

        # configure grid layout (1x2)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)

        # create menu
        # TODO: Create menu. CTK does not yet have a custom Menu element.
        #  The standard TK element looks awfull.

        # ========================================================
        # create main toolbar
        self.main_toolbar = customtkinter.CTkFrame(self)
        self.main_toolbar.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.heartbeat_button = ToggleButton(
            self.main_toolbar,
            text="Heartbeat",
            command=self.event_manager.create_event_trigger(EventID.HEARTBEAT),
            image_off=Icons.HEARTBEAT_OFF,
            image_on=Icons.HEARTBEAT_ON,
        )
        self.heartbeat_button.grid(row=0, column=0)

        self.spy_button = ToggleButton(
            self.main_toolbar,
            text="Spy",
            command=self.toolbar_button_spy_command,
            image_off=Icons.SPY_OFF,
            image_on=Icons.SPY_ON,
        )
        self.spy_button.grid(row=0, column=1)

        self.power_button = ToggleButton(
            self.main_toolbar,
            text="Power",
            command=self.toolbar_button_power_command,
            image_off=Icons.POWER_OFF,
            image_on=Icons.POWER_ON,
        )
        self.power_button.grid(row=0, column=2)

        # ========================================================
        # create tabview
        self.tabview = customtkinter.CTkTabview(self)
        self.tabview.grid(row=1, column=0, padx=10, sticky="nsew")
        # TODO: add hardware configuration tab
        # self.tabview.add("Configure")
        # self.tabview.tab("Configure").grid_columnconfigure(0, weight=1)
        self.trace_tab = self.tabview.add("Trace")
        self.diagnostics_tab = self.tabview.add("Diagnostics")

        # ========================================================
        # create trace tab
        self.trace_tab.grid_rowconfigure(0, weight=10)
        self.trace_tab.grid_rowconfigure(1, weight=1)
        self.trace_tab.grid_columnconfigure(0, weight=1)

        # create trace message tree
        # create a Treeview widget
        # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

        columns = TraceViewData.headings

        style = ttk.Style()
        style.configure(
            "mystyle.Treeview", highlightthickness=0, bd=0, font=("Calibri", 12)
        )  # Modify the font of the body
        style.configure(
            "mystyle.Treeview.Heading", font=("Calibri", 14, "bold")
        )  # Modify the font of the headings

        # create a Treeview widget
        self.trace_treeview = ttk.Treeview(
            self.trace_tab,
            columns=columns,
            show="tree headings",
            style="mystyle.Treeview",
        )
        self.trace_treeview.grid(row=0, column=0, sticky="nsew")

        # define column headings
        self.trace_treeview.heading("#0", text="Time")
        for column in columns:
            self.trace_treeview.heading(column, text=column, anchor=W)
        self.trace_treeview.column("#0", minwidth=0, width=150, stretch=NO)
        self.trace_treeview.column(columns[0], minwidth=0, width=150, stretch=NO)
        self.trace_treeview.column(columns[1], minwidth=0, width=50, stretch=NO)

        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        # create trace textbox
        self.trace_textbox = customtkinter.CTkTextbox(
            self.trace_tab, activate_scrollbars=True
        )
        self.trace_textbox.grid(row=1, column=0, sticky="nsew")
        self.trace_textbox.insert("0.0", "No network activity...")
        self.trace_textbox.configure(state="disabled")

        # ========================================================
        # create dignostics tab
        self.diagnostics_tab.grid_rowconfigure(0, weight=0)
        self.diagnostics_tab.grid_rowconfigure(1, weight=1)
        self.diagnostics_tab.grid_columnconfigure(0, weight=0)
        self.diagnostics_tab.grid_columnconfigure(1, weight=1)

        # ========================================================
        # create diagnostics toolbar
        self.diagnostics_toolbar = customtkinter.CTkFrame(self.diagnostics_tab)
        self.diagnostics_toolbar.grid(row=0, column=0, sticky="new", columnspan=2)

        self.tester_mode_button = ToggleButton(
            self.diagnostics_toolbar,
            text="Tester mode",
            command=self.toolbar_button_tester_mode_command,
        )
        self.tester_mode_button.grid(row=0, column=0)

        self.xcp_mode_button = ToggleButton(
            self.diagnostics_toolbar,
            text="XCP mode",
            command=self.toolbar_button_xcp_mode_command,
        )
        self.xcp_mode_button.grid(row=0, column=1)

        # create diagnostics textbox
        self.diagnostics_textbox = customtkinter.CTkTextbox(
            self.diagnostics_tab, activate_scrollbars=True
        )
        self.diagnostics_textbox.grid(row=1, column=1, sticky="nsew")
        self.diagnostics_textbox.insert("0.0", "No network activity...")
        self.diagnostics_textbox.configure(state="disabled")
        self.xcp_textbox = customtkinter.CTkTextbox(
            self.diagnostics_tab, activate_scrollbars=True
        )
        self.xcp_send_ecu_info_button = customtkinter.CTkButton(
            self.diagnostics_tab, text="Get ECU Info"
        )
        self.xcp_send_ecu_info_button.grid(
            row=1, column=0, padx=(0, 10), pady=(10, 0), sticky="n"
        )

        # ========================================================
        # create statusbar
        self.status_frame = customtkinter.CTkFrame(self)
        self.status_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.status_label = customtkinter.CTkLabel(
            self.status_frame, text="Status unknown..."
        )
        self.status_label.grid(row=0, column=0)

    def toolbar_button_heartbeat_command(self):
        self.write_toggle_button_status(self.heartbeat_button)

    def toolbar_button_spy_command(self):
        self.write_toggle_button_status(self.spy_button)

    def toolbar_button_tester_mode_command(self):
        self.write_toggle_button_status(self.tester_mode_button)

    def toolbar_button_power_command(self):
        self.write_toggle_button_status(self.power_button)

    def toolbar_button_xcp_mode_command(self):
        self.write_toggle_button_status(self.xcp_mode_button)

    def write_toggle_button_status(self, button: ToggleButton):
        self.status_label.configure(
            text=f"{button.cget('text')} button is {'ON' if button.state else 'OFF' }"
        )

    def update_text(self, text: str):
        return self.status_label.configure(text=text)

    def update_trace_view(self, messages: Dict[str, TraceViewData]):
        self.messages.update(messages)
        existing_ids = self.trace_treeview.get_children("")
        for id, message in self.messages.items():
            if id in existing_ids:
                self.trace_treeview.item(
                    id,
                    text=message.timestamp,
                    values=(message.id, message.dlc, message.data, message.channel),
                )
                for index, data in enumerate(message.data):
                    self.trace_treeview.item(
                        f"{id}.{index}",
                        text=f"data {data}",
                        values=[],
                    )
            else:  # new message
                self.trace_treeview.insert(
                    "",
                    END,
                    text=message.timestamp,
                    iid=id,
                    values=(message.id, message.dlc, message.data),
                    open=False,
                )
                for index, data in enumerate(message.data):
                    self.trace_treeview.insert(
                        id,
                        END,
                        iid=f"{id}.{index}",
                        text=f"data {data}",
                        values=[],
                    )

    def update_trace_textbox(self, text: str):
        self.update_text_box(self.trace_textbox, text)

    def update_xcp_textbox(self, text: str):
        self.update_text_box(self.xcp_textbox, text)

    @staticmethod
    def update_text_box(text_box: customtkinter.CTkTextbox, text: str):
        text_box.configure(state="normal")
        text_box.delete(1.0, END)
        text_box.insert("0.0", text)
        text_box.configure(state="disabled")


if __name__ == "__main__":
    MainView().mainloop()
