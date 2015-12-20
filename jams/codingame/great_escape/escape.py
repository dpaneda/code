import sys
import time


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return "Point({},{})".format(self.x, self.y)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(str(self))


class Player:
    def __init__(self, pos, id):
        self.pos = pos
        self.id = id

    def __str__(self):
        return "Player({},{})".format(self.pos, self.id)

    def __repr__(self):
        return str(self)


class Game:
    def __init__(self, players, walls, me):
        self.players, self.walls, self.me = players, walls, me

    def neighbors(self, p):
        neig = [
            ("UP", Point(p.x, p.y - 1)),
            ("DOWN", Point(p.x, p.y + 1)),
            ("LEFT", Point(p.x - 1, p.y)),
            ("RIGHT", Point(p.x + 1, p.y))]
        return neig

    def move(self, p, where):
        if where == "UP":
            p.y -= 1
        elif where == "DOWN":
            p.y += 1
        elif where == "LEFT":
            p.x -= 1
        else:
            p.x += 1

    def valid_destinations(self, p):
        destinations = []

        pos = (p.x, p.y)
        up = (p.x, p.y - 1)

        right = (p.x + 1, p.y)
        up_right = (p.x + 1, p.y - 1)

        left = (p.x - 1, p.y)

        down = (p.x, p.y + 1)
        down_left = (p.x - 1, p.y + 1)

        walls = self.walls

        if p.x > 0 and pos not in walls['V'] and up not in walls['V']:
            destinations.append('LEFT')
        if p.x < 8 and right not in walls['V'] and up_right not in walls['V']:
            destinations.append('RIGHT')
        if p.y > 0 and pos not in walls['H'] and left not in walls['H']:
            destinations.append('UP')
        if p.y < 8 and down not in walls['H'] and down_left not in walls['H']:
            destinations.append('DOWN')
        return destinations

    def free_neighbors(self, p):
        ps = []
        destinations = self.valid_destinations(p)
        for pos in self.neighbors(p):
            if pos[0] in destinations:
                ps.append(pos)
        return ps

    def find_path(self, player):
        id = player.id

        explored = {player.pos}
        border = {player.pos}
        paths = {player.pos: []}

        if id == 0:
            escape = lambda p: p.x == 8
        elif id == 1:
            escape = lambda p: p.x == 0
        elif id == 2:
            escape = lambda p: p.y == 8

        while border:
            ps = list(border)
            explored |= border
            border = set()

            for p in ps:
                for neig in self.free_neighbors(p):
                    where, n = neig
                    if n not in explored:
                        paths[n] = paths[p] + [where]
                        border.add(n)
                        if escape(n):
                            return paths[n]
        return None

    def legal_wall(self, wall, kind):
        if wall in self.walls[kind]:
            return False

        # Check that the wall does not block anyone
        for p in self.players:
            if not p:
                continue
            if p.id == self.me:
                old_path = self.find_path(me)

            self.walls[kind].append(wall)
            path = self.find_path(p)
            self.walls[kind].pop()
            if not path:
                return False
            # Don't block our path
            if p.id == self.me and len(path) > len(old_path):
                return False

        x, y = wall
        if kind == 'H':
            if (x - 1, y) in walls['H'] or (x + 1, y) in walls['H']:
                return False
            if (x + 1, y - 1) in walls['V']:
                return False
            return 0 <= wall[0] < 8 and 0 <= wall[1] <= 8
        else:
            if (x, y - 1) in walls['V'] or (x, y + 1) in walls['V']:
                return False
            if (x - 1, y + 1) in walls['H']:
                return False
            return 0 <= wall[0] <= 8 and 0 <= wall[1] < 8

    def block_step(self, p, where):
        pos = (p.x, p.y)
        up = (p.x, p.y - 1)

        right = (p.x + 1, p.y)
        up_right = (p.x + 1, p.y - 1)

        left = (p.x - 1, p.y)

        down = (p.x, p.y + 1)
        down_left = (p.x - 1, p.y + 1)

        if where == 'RIGHT':
            return [right, up_right, 'V']
        elif where == 'LEFT':
            return [pos, up, 'V']
        elif where == 'UP':
            return [pos, left, 'H']
        else:
            return [down, down_left, 'H']

    def block(self, player):
        x, y = player.pos.x, player.pos.y

        path = self.find_path(player)
        path_len = len(path)
        best_block = 0
        best = None
        best_parity = None
        walls = self.walls

        for where in path:
            block_walls = self.block_step(player.pos, where)
            kind = block_walls.pop()
            while block_walls:
                w = block_walls.pop()
                if self.legal_wall(w, kind):
                    walls[kind].append(w)
                    parity = (w[0] % 2) + (w[1] % 2)
                    new_path = self.find_path(player)
                    block = len(new_path) - path_len
                    if new_path:
                        if (block > best_block) or (block == best_block and parity > best_parity):
                            best_block = len(new_path) - path_len
                            best_parity = parity
                            best = w[0], w[1], kind
                    walls[kind].pop()
            self.move(player.pos, where)

        if best:
            return best_block, "{} {} {}".format(best[0], best[1], best[2])
        else:
            return 0, None

w, h, player_count, my_id = [int(i) for i in raw_input().split()]

trick_walls_h = [(0, 5), (2, 5), (4, 5), (6, 5)]

for turn in xrange(1000):
    start_time = time.clock()
    players = []
    for i in xrange(player_count):
        x, y, wl = [int(j) for j in raw_input().split()]
        if x == -1:
            players.append(None)
        else:
            players.append(Player(Point(x, y), i))
        if i == my_id:
            walls_left = wl

    wall_count = input()
    walls = {}
    walls['H'] = []
    walls['V'] = []
    for i in xrange(wall_count):
        wall_x, wall_y, wall_orientation = raw_input().split()
        x = int(wall_x)
        y = int(wall_y)
        walls[wall_orientation].append((x, y))

    game = Game(players, walls, my_id)
    me = players[my_id]
    enemy = players[1]

    path = game.find_path(me)
    best_path = path
    best_block = 0
    best_action = None
    best_distance = None

    if player_count == 2 and trick_walls_h:
        print >>sys.stderr, "Trick wall placement"
        w = trick_walls_h.pop(0)
        if my_id == 1:
            print 1 + w[0], w[1], 'H'
        else:
            print w[0], w[1], 'H'
        continue

    # Walls
    for player in players:
        if not walls_left or not player or player == me:
            continue

        player_path = game.find_path(player)
        print >>sys.stderr, player, player_path

        # This limitation is to avoid huge branching causing timeout
        if len(player_path) < 6:
            block_len, action = game.block(player)
            if action and block_len > best_block:
                best_block, best_action, best_distance = block_len, action, len(player_path)
                print >>sys.stderr, "New best: {} {}".format(player, best_block)

    my_path = game.find_path(me)

    # Lets decide if we would block
    if best_action is None:
        pass
    elif len(my_path) < 2:
        best_action = None
        print >>sys.stderr, "Almost there!"
    elif best_distance < 2:
        print >>sys.stderr, "Enemy is near!", best_distance
    elif player_count == 2:
        if best_block < 2:
            best_action = None
    elif best_block < 4:
        best_action = None

    if best_action:
        print >>sys.stderr, "Blocking", best_block
        out = best_action
    else:
        print >>sys.stderr, "Path is", path
        out = str(my_path[0])

    end_time = time.clock()
    delta = int(1000 * (end_time - start_time))

    print out, delta
