import toga
from toga.style.pack import CENTER, COLUMN, ROW, Pack


class Graze(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow()

        self.webview = toga.WebView(
            on_webview_load=self.on_webview_loaded, style=Pack(flex=1)
        )
        self.url_input = toga.TextInput(
            value="https://beeware.org/", style=Pack(flex=1)
        )

        box = toga.Box(
            children=[
                toga.Box(
                    children=[
                        self.url_input,
                        toga.Button(
                            "Go",
                            on_press=self.load_page,
                            style=Pack(width=50, margin_left=5),
                        ),
                    ],
                    style=Pack(
                        direction=ROW,
                        align_items=CENTER,
                        margin=5,
                    ),
                ),
                self.webview,
            ],
            style=Pack(direction=COLUMN),
        )

        self.main_window.content = box
        self.webview.url = self.url_input.value

        # Show the main window
        self.main_window.show()

    def load_page(self, widget):
        self.webview.url = self.url_input.value

    def on_webview_loaded(self, widget):
        self.url_input.value = self.webview.url


def main():
    return Graze("Graze", "org.beeware.toga.examples.tutorial")


if __name__ == "__main__":
    main().main_loop()
