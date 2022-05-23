from typing import Protocol
from InputStream import InputStream


class ProductCode(Protocol):
    def __init__(self, input: InputStream) -> None: ...