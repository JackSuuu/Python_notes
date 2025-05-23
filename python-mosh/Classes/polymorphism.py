from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


# polymorphism
def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
textbox = TextBox()
draw([ddl, textbox])  # we can render multiple object


