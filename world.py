import math
import random
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

    def get_spawn_coordinates(self, min_dist: int = 50, max_dist: int = 150, num_candidates: int = 20) -> tuple:
        if not self.players:
            return (0, 0)
        
        best_candidate = None
        best_fitness = -1

        for _ in range(num_candidates):
            ref_player = random.choice(self.players)
            
            angle = random.uniform(0, 2 * math.pi)
            distance = random.uniform(min_dist, max_dist)
            cand_x = int(ref_player[0] + distance * math.cos(angle))
            cand_y = int(ref_player[1] + distance * math.sin(angle))
            candidate = (cand_x, cand_y)
            
            distances = []
            for p in self.players:
                dist = math.hypot(candidate[0] - p[0], candidate[1] - p[1])
                distances.append(dist)
            
            min_distance_to_anyone = min(distances)
            if min_distance_to_anyone >= min_dist:
                fitness = min_distance_to_anyone
                if fitness > best_fitness:
                    best_fitness = fitness
                    best_candidate = candidate

        if best_candidate is None:
            return (self.players[0][0] + max_dist, self.players[0][1] + max_dist)
            
        return best_candidate