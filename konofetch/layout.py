from prompt_toolkit.application import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import VSplit, Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.output.color_depth import ColorDepth

from .fmt import asci_fmt, info_fmt

def box(renderer, height=None, width=None):
    b = None
    def render():
        return renderer(b)
    b = Window(
        content=FormattedTextControl(render),
        height=height,
        width=width,
    )
    return b

asci_box = box(asci_fmt)
info_box = box(info_fmt,width=34)

layout = Layout(VSplit([info_box, asci_box]))
layout.focus_stack = []

kb = KeyBindings()
@kb.add("q")
def exit_(event):
    event.app.exit()

app = Application(
    layout=layout,
    key_bindings=kb,
    color_depth=ColorDepth.TRUE_COLOR,
    full_screen=True,
)
