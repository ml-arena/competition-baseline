"""Awalé (Oware, abapa rules) in plain Python: lists and integers only.

One file, three users: the challenge's env.py referees with it, the starter
notebook plays local games with it, and an agent may upload it next to
agent.py to look ahead (`import awale`).

The board is always described from the point of view of the player to move:

    my_pits        your 6 pits, index 0 on your left, 5 on your right
    opponent_pits  the opponent's 6 pits, in sowing order: opponent_pits[0]
                   is the pit that receives a seed right after my_pits[5]

Seeds travel my_pits[0] -> ... -> my_pits[5] -> opponent_pits[0] -> ... ->
opponent_pits[5] -> my_pits[0] (counter-clockwise on the table).
"""
import random
import time

PITS = 6             # pits per player
SEEDS_PER_PIT = 4    # 48 seeds in all
WIN_SCORE = 25       # more than half of the seeds
MAX_MOVES = 200      # moves in a game, both players together
CLOCK_SECONDS = 10.0  # each player's thinking time for a whole game


def sow(my_pits, opponent_pits, move):
    """Play pit `move` (0 to 5). Returns (my_pits, opponent_pits, captured)
    after the move, as new lists: the arguments are not modified.

    The seeds of the pit are sown one by one in the following pits; the
    starting pit is skipped when the move goes all the way round (12 seeds or
    more). If the last seed makes 2 or 3 in an opponent pit, those seeds are
    captured, and so are the seeds of the pits just before it for as long as
    they also hold 2 or 3. A move that would capture every seed the opponent
    has captures nothing.
    """
    ring = list(my_pits) + list(opponent_pits)
    seeds = ring[move]
    if seeds == 0:
        raise ValueError(f"pit {move} is empty")
    ring[move] = 0
    position = move
    while seeds > 0:
        position = (position + 1) % (2 * PITS)
        if position == move:
            continue
        ring[position] += 1
        seeds -= 1

    captured = 0
    taken = []
    while position >= PITS and ring[position] in (2, 3):
        taken.append(position)
        captured += ring[position]
        position -= 1
    if captured == sum(ring[PITS:]):
        captured = 0  # it would leave the opponent with nothing: no capture
    else:
        for index in taken:
            ring[index] = 0
    return ring[:PITS], ring[PITS:], captured


def legal_moves(my_pits, opponent_pits):
    """The pits you may play: every pit of yours that holds seeds. When the
    opponent has no seed left, only the moves that give them at least one."""
    moves = [i for i in range(PITS) if my_pits[i] > 0]
    if sum(opponent_pits) == 0:
        moves = [i for i in moves if sum(sow(my_pits, opponent_pits, i)[1]) > 0]
    return moves


class Game:
    """One game. Player 0 moves first. `pits[p]` and `scores[p]` belong to
    player `p`; `to_move` is the player whose turn it is."""

    def __init__(self):
        self.pits = [[SEEDS_PER_PIT] * PITS, [SEEDS_PER_PIT] * PITS]
        self.scores = [0, 0]
        self.to_move = 0
        self.moves_played = 0
        self.over = False
        self.winner = None      # 0, 1, or None for a draw (once over)
        self.end_reason = None

    def legal_moves(self):
        me = self.to_move
        return legal_moves(self.pits[me], self.pits[1 - me])

    def state(self, time_left=CLOCK_SECONDS):
        """What the player to move receives in `choose_move(state)`."""
        me = self.to_move
        return {
            "my_pits": list(self.pits[me]),
            "opponent_pits": list(self.pits[1 - me]),
            "my_score": self.scores[me],
            "opponent_score": self.scores[1 - me],
            "legal_moves": self.legal_moves(),
            "time_left": time_left,
            "move_number": self.moves_played,
        }

    def play(self, move):
        """Play `move` for the player to move. Returns the seeds captured."""
        if self.over:
            raise ValueError("the game is over")
        if move not in self.legal_moves():
            raise ValueError(f"illegal move {move!r}: legal moves are {self.legal_moves()}")
        me = self.to_move
        self.pits[me], self.pits[1 - me], captured = sow(self.pits[me], self.pits[1 - me], move)
        self.scores[me] += captured
        self.moves_played += 1
        self.to_move = 1 - me

        if max(self.scores) >= WIN_SCORE:
            self._finish(f"{WIN_SCORE} seeds captured")
        elif self.scores[0] == self.scores[1] == WIN_SCORE - 1:
            self._finish("24 seeds each")
        elif not self.legal_moves():
            # Nobody can play on: each player keeps the seeds on their side.
            for player in (0, 1):
                self.scores[player] += sum(self.pits[player])
                self.pits[player] = [0] * PITS
            self._finish("no move left")
        elif self.moves_played >= MAX_MOVES:
            self._finish(f"{MAX_MOVES} moves played")
        return captured

    def forfeit(self, loser, reason):
        """End the game now as a loss for `loser` (clock, illegal move)."""
        self.over = True
        self.winner = 1 - loser
        self.end_reason = reason

    def _finish(self, reason):
        self.over = True
        self.end_reason = reason
        if self.scores[0] != self.scores[1]:
            self.winner = 0 if self.scores[0] > self.scores[1] else 1


def show(state):
    """Print a state the way the player to move sees the table."""
    top = "  ".join(f"{n:2d}" for n in reversed(state["opponent_pits"]))
    bottom = "  ".join(f"{n:2d}" for n in state["my_pits"])
    print(f"opponent ({state['opponent_score']:2d})   {top}")
    print(f"you      ({state['my_score']:2d})   {bottom}")
    print("pit number       " + "   ".join(str(i) for i in range(PITS)))


class RandomAgent:
    """Plays any legal move."""

    def choose_move(self, state):
        return random.choice(state["legal_moves"])


def play_game(first, second, verbose=False):
    """Play one game between two agents, `first` moving first, with the
    challenge's clock. Returns the finished `Game` (`winner` is 0 for `first`,
    1 for `second`, None for a draw)."""
    game = Game()
    agents = [first, second]
    clocks = [CLOCK_SECONDS, CLOCK_SECONDS]
    while not game.over:
        player = game.to_move
        state = game.state(time_left=clocks[player])
        if verbose:
            print(f"\nmove {game.moves_played + 1}, player {player} to play")
            show(state)
        started = time.perf_counter()
        move = agents[player].choose_move(state)
        clocks[player] -= time.perf_counter() - started
        if clocks[player] < 0:
            game.forfeit(player, "out of time")
        elif type(move) is not int or move not in state["legal_moves"]:
            game.forfeit(player, f"illegal move {move!r}")
        else:
            captured = game.play(move)
            if verbose:
                print(f"-> plays pit {move}" + (f", captures {captured}" if captured else ""))
    if verbose:
        result = "draw" if game.winner is None else f"player {game.winner} wins"
        print(f"\n{result} ({game.end_reason}), score {game.scores[0]} - {game.scores[1]}")
    return game


def play_match(agent, opponent, games=20):
    """Play `games` games, alternating who moves first. Returns the counts
    {"wins", "draws", "losses"} from `agent`'s side and prints them."""
    counts = {"wins": 0, "draws": 0, "losses": 0}
    for index in range(games):
        agent_seat = index % 2
        pair = [agent, opponent] if agent_seat == 0 else [opponent, agent]
        game = play_game(pair[0], pair[1])
        if game.winner is None:
            counts["draws"] += 1
        elif game.winner == agent_seat:
            counts["wins"] += 1
        else:
            counts["losses"] += 1
    print(f"{games} games: {counts['wins']} wins, {counts['draws']} draws, "
          f"{counts['losses']} losses")
    return counts
