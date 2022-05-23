from dataclasses import dataclass, field
from typing import overload
import struct
from InputStream import InputStream

@dataclass(slots=True)
class WiiUProductCode:
    categoryType: int   = field(default=1) #! CategoryType (0 = Map Pack | 1 = Skin Pack | 2 = Texture Pack | 3 = Mash-Up Pack | 4 = Bundle Pack)
    iUnk0x04: int       = field(default=1)
    iUnk0x08: int       = field(default=0)
    nameStrLen: int     = field(default=7, repr=False)
    name: str           = field(default="no_name")
    dlcImageStrLen: int = field(default=0, repr=False)
    dlcImageName: str   = field(default="")
    packGraphicId: int  = field(default=0) #! if not valid it'll use default.png found in the .arc file
    iUnk2: int          = field(default=0)
    strUnk0: str        = field(default="----")

    @overload
    def __init__(self, stream: InputStream) -> None: ...
    def __init__(self, stream: InputStream) -> None:
        (self.categoryType,
         self.iUnk0x04,
         self.iUnk0x08,
         self.nameStrLen) = struct.unpack(">4i", stream.read(16))
        self.name = stream.read(self.nameStrLen).decode("UTF-8")
        self.dlcImageStrLen = struct.unpack(">i", stream.read(4))[0]
        self.dlcImageName = stream.read(self.dlcImageStrLen).decode("UTF-8")
        self.packGraphicId, self.iUnk2 = struct.unpack(">2i", stream.read(8))
        self.strUnk0 = stream.read(4).decode("UTF-8")
        stream.read(1) # pad byte