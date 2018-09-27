def answer(src, dest):
    visited = {}

    class Tile:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __eq__(self, other):
            return self.x == other.x and self.y == other.y

    def num_to_tile(num):
        x, y = num % 8, int(num / 8)
        return Tile(x, y)

    def tile_to_num(tile):
        x, y = tile.x, tile.y
        return x + (8 * y)

    def is_valid(tile):
        x, y = tile.x, tile.y
        key = make_key(tile)
        if x < 0 or y < 0 or x > 7 or y > 7:
            return False
        else:
            return key not in visited

    def make_key(tile):
        return str(tile.x) + str(tile.y)

    def possible_moves(tile):
        moves = []
        new_tile(tile, -1, -2, moves)
        new_tile(tile, -1, 2, moves)
        new_tile(tile, -2, -1, moves)
        new_tile(tile, -2, 1, moves)
        new_tile(tile, 1, -2, moves)
        new_tile(tile, 1, 2, moves)
        new_tile(tile, 2, -1, moves)
        new_tile(tile, 2, 1, moves)
        return moves

    def new_tile(tile, dx, dy, moves):
        x, y = tile.x, tile.y
        new_x, new_y = x + dx, y + dy
        new_tile = Tile(new_x, new_y)
        if is_valid(new_tile):
            moves.append(new_tile)
            set_path(tile, new_tile)
        return moves

    def set_path(tile1, tile2):
        key = make_key(tile2)
        visited[key] = tile1

    def backtrack(tile, src):
        arr, p = [], tile
        arr.append(p)
        while not(p.x == src.x and p.y == src.y):
            key = str(p.x) + str(p.y)
            x = visited[key].x
            y = visited[key].y
            arr.append(Tile(x, y))
            p = Tile(x, y)
        return arr

    def search(src, dest):
        queue = []
        queue.append(src)
        while queue:
            temp_tile = queue.pop(0)
            if (temp_tile.x == dest.x and temp_tile.y == dest.y):
                return backtrack(temp_tile, src)
            else:
                temp_arr = possible_moves(temp_tile)
                queue.extend(temp_arr)

    def solve(src, dest):
        if src == dest:
            return 0
        s, d = num_to_tile(src), num_to_tile(dest)
        ans = search(s, d)
        return len(ans) - 1

    return solve(src, dest)
