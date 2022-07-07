from dataclasses import dataclass, field
from typing import overload
import struct
from io import BufferedReader

@dataclass
class XBOXProductCode:
    #! CategoryType (0 = Map Pack | 1 = Skin Pack | 2 = Texture Pack | 3 = Mash-Up Pack | 4 = Bundle Pack)
    #! and more for xbox specific "products" like avatar items
    categoryType: int   = field(default=1)
    iUnk2: int          = field(default=1)
    nameStrLen: int     = field(default=7, repr=False)
    name: str           = field(default="no_name")
    nameStrLen2: int    = field(default=7, repr=False)
    name2: str          = field(default="no_name")
    dlcImageStrLen: int = field(default=0)
    dlcImageName: str   = field(default="")
    iUnk4: int          = field(default=1)
    iUnk5: int          = field(default=1)
    iUnk6: int          = field(default=1)

    @overload
    def __init__(self, stream: BufferedReader) -> None: ...
    def __init__(self, stream: BufferedReader) -> None:
        (self.categoryType,
         self.iUnk2,
         self.nameStrLen) = struct.unpack(">3i", stream.read(12))
        self.name = stream.read(self.nameStrLen).decode("UTF-8")
        self.nameStrLen2 = struct.unpack(">i", stream.read(4))[0]
        self.name2 = stream.read(self.nameStrLen2).decode("UTF-8")
        self.dlcImageStrLen = struct.unpack(">i", stream.read(4))[0]
        self.dlcImageName = stream.read(self.dlcImageStrLen).decode("UTF-8")
        self.iUnk4, self.iUnk5, self.iUnk6 = struct.unpack(">3i", stream.read(12))