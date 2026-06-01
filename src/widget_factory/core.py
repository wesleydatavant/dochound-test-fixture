"""Core widget functionality."""


class WidgetBuilder:
    """Build widgets from definitions."""

    def build(self, definition: dict) -> dict:
        return {"type": "widget", **definition}


def render_widget(widget: dict) -> str:
    """Convert a widget to HTML."""
    return f"<div class='widget'>{widget}</div>"
