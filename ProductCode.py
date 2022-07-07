from io import BufferedReader
from typing import Protocol

class ProductCode(Protocol):
    def __init__(self, input: BufferedReader) -> None: ...