from dataclasses import dataclass, field
from typing import overload
import struct
from InputStream import InputStream

@dataclass(slots=True)
class VitaProductCode:
    categoryType: int     = field(default=1) #! CategoryType (0 = Map Pack | 1 = Skin Pack | 2 = Texture Pack | 3 = Mash-Up Pack | 4 = Bundle Pack)
    iUnk0x04: int         = field(default=1)
    contentIdStrLen: int  = field(default=0, repr=False)
    contentId: str        = field(default="")
    contentIdStrLen2: int = field(default=0, repr=False)
    contentId2: str       = field(default="")
    nameStrLen: int       = field(default=7, repr=False)
    name: str             = field(default="no_name")
    dlcImageStrLen: int   = field(default=0, repr=False)
    dlcImageName: str     = field(default="")
    packGraphicId: int    = field(default=0)
    iUnk2: int            = field(default=0)

    @overload
    def __init__(self, stream: InputStream) -> None: ...
    def __init__(self, stream: InputStream) -> None:
        (self.categoryType,
         self.iUnk0x04,
         self.contentIdStrLen) = struct.unpack("<3i", stream.read(12))
        self.contentId = stream.read(self.contentIdStrLen).decode("UTF-8")
        self.contentIdStrLen2 = struct.unpack("<i", stream.read(4))[0]
        self.contentId2 = stream.read(self.contentIdStrLen2).decode("UTF-8")
        self.nameStrLen = struct.unpack("<i", stream.read(4))[0]
        self.name = stream.read(self.nameStrLen).decode("UTF-8")
        self.dlcImageStrLen = struct.unpack("<i", stream.read(4))[0]
        self.dlcImageName = stream.read(self.dlcImageStrLen).decode("UTF-8")
        self.packGraphicId, self.iUnk2 = struct.unpack("<2i", stream.read(8))