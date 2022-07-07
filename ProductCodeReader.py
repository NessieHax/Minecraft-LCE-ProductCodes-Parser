from dataclasses import dataclass, field
from io import BufferedReader
import struct, sys
from ProductCode import ProductCode
from WiiUProductCode import WiiUProductCode
from PS3ProductCode import PS3ProductCode
from XBOXProductCode import XBOXProductCode
from VitaProductCode import VitaProductCode

WIIU    = "WIIU"
PS3     = "PS3"
PS_VITA = "PSV"
XBOX    = "XBX"

@dataclass(repr=False)
class ProductCodeReader:
    __consoleType: str = field(default_factory=str)
    __productList: list[ProductCode] = field(default_factory=list)

    def process(self, stream: BufferedReader) -> None:
        skipSize = 9
        cls = WiiUProductCode
        fmt = ">i"
        if self.__consoleType == PS3:
            skipSize = 0xb0
            cls = PS3ProductCode
        if self.__consoleType == XBOX:
            skipSize = 0
            cls = XBOXProductCode
        if self.__consoleType == PS_VITA:
            fmt = "<i"
            skipSize = 0x61
            cls = VitaProductCode

        print(stream.read(skipSize), file=sys.stderr)
        self.__productList = [cls(stream) for _ in range(struct.unpack(fmt, stream.read(4))[0])]

    def __repr__(self) -> str:
        return f"{self.__consoleType}\n" + "\n".join(p.__repr__() for p in self.__productList)