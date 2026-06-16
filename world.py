import struct

class World:
    def __init__(self):
        self.players = []

    def pack_to_bytes(self) -> bytes:
        count = len(self.players)
        fmt = f"<I{count * 2}i"
        
        flat_players = [coord for player in self.players for coord in player]
        
        return struct.pack(fmt, count, *flat_players)

    def unpack_from_bytes(self, data: bytes):
        count = struct.unpack_from("<I", data, 0)[0]
        fmt = f"<{count * 2}i"
        flat_players = struct.unpack_from(fmt, data, 4)
        self.players = list(zip(*[iter(flat_players)] * 2))