from Orange.widgets.widget import OWWidget
from Orange.widgets import gui


class MyWidget(OWWidget):
    name = "Recommendation System Widget"
    icon = "icons/recommend.svg"

    def __init__(self):
        super().__init__()

        gui.label(self, self, "test")
