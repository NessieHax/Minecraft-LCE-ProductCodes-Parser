from dataclasses import dataclass, field
import struct, sys
from InputStream import InputStream
from ProductCode import ProductCode
from WiiUProductCode import WiiUProductCode
from PS3ProductCode import PS3ProductCode
from XBOXProductCode import XBOXProductCode
from VitaProductCode import VitaProductCode

WIIU    = "WIIU"
PS3     = "PS3"
PS_VITA = "PSV"
XBOX    = "XBX"

@dataclass(init=False, slots=True, repr=False)
class ProductCodeReader(InputStream):
    __consoleType: str = field(default_factory=str)
    __productList: list[ProductCode] = field(default_factory=list)

    def __init__(self, data: bytes, consoleType: str) -> None:
        super(ProductCodeReader, self).__init__(data)

        skipSize = 9
        cls = WiiUProductCode
        fmt = ">i"
        if consoleType == PS3:
            skipSize = 0xb0
            cls = PS3ProductCode
        if consoleType == XBOX:
            skipSize = 0
            cls = XBOXProductCode
        if consoleType == PS_VITA:
            fmt = "<i"
            skipSize = 0x61
            cls = VitaProductCode

        print(self.read(skipSize), file=sys.stderr)
        self.__consoleType = consoleType
        self.__productList = [cls(self) for _ in range(struct.unpack(fmt, self.read(4))[0])]

    def __repr__(self) -> str:
        return f"{self.__consoleType}\n" + "\n".join(p.__repr__() for p in self.__productList)