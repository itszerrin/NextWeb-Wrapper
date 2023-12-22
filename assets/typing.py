import typing as t

Response = t.Dict[str, t.Any]
Model = t.NewType("Model", str)
Headers = t.Dict[str, str]
Messages = t.List[t.Dict[str, str]]
Address = t.NewType("Address", str)
Url = t.NewType("Url", str)
Any = t.Any

_all__ = [
    "Response",
    "Model",
    "Headers",
    "Messages",
    "Address",
    "Url",
    "Any",
]

# Path: assets/scripts/typing.py