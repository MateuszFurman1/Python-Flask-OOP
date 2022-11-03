def show(chessboard):
    """Shows the chessboard in the console.
    DOES NOT WORK UNTIL ALL CLASES: Pawn, Knight, Queen, King, Rook, Bishop ARE CREATED!!!
    """
    WHITE = {
        Pawn: chr(9817),
        Knight: chr(9816),
        Queen: chr(9813),
        King: chr(9812),
        Rook: chr(9814),
        Bishop: chr(9815),
    }
    BLACK = {
        Pawn: chr(9823),
        Knight: chr(9822),
        Queen: chr(9819),
        King: chr(9818),
        Rook: chr(9820),
        Bishop: chr(9821),
    }
    for y in range(7, -1, -1):
        print(y, end='\t')
        for x in range(8):
            if chessboard.board[x][y] is not None:
                if chessboard.board[x][y].color == 'white':
                    print(WHITE[type(chessboard.board[x][y])], end='\t')
                else:
                    print(BLACK[type(chessboard.board[x][y])], end='\t')
            else:
                print('\t', end='')
        print('\n')
    print('\t', end='')
    for x in range(8):
        print(x, end='\t')
    print()


class Chessboard:
    def __init__(self):
        self.color = "white"
        self.board = [[None] * 8 for r in range(8)]

    def isinside(self, x, y):
        return 0 <= x <= 7 and 0 <= y <= 7

    def only_inside(self, moves):
        return [(x, y) for (x, y) in moves if self.isinside(x, y)]

    def setup(self):
        figures = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for x in range(8):
            self.board[x][1] = Pawn("white", x, 1)
            self.board[x][6] = Pawn("black", x, 6)
            self.board[x][0] = figures[x]("white", x, 0)
            self.board[x][7] = figures[x]("black", x, 7)

    def list_allowed_moves(self, x, y):
        f = self.board[x][y]
        if f is None or f.color != self.color:
            return None
        else:
            return f.list_allowed_moves(self)

    def move(self, from_x, from_y, to_x, to_y):
        allowed = self.list_allowed_moves(from_x, from_y)
        if allowed is not None and (to_x, to_y) in allowed:
            f = self.board[from_x][from_y]
            f.move(to_x, to_y)
            killed = self.board[to_x][to_y]
            self.board[to_x][to_y] = f
            self.board[from_x][from_y] = None
            res = None
            if isinstance(killed, King):
                res = f"{self.color.upper()} WON"
            self.color = "white" if self.color == "black" else "black"
            return res
        else:
            raise ValueError("Niedozwolony ruch !!!")



class Figure:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def moves_in_dir(self, dx, dy, maxdist, chessboard):
        result = []
        x, y = self.x, self.y
        dist = 0
        while True:
            dist += 1
            if dist > maxdist:
                break
            x, y = x + dx, y + dy
            if not chessboard.isinside(x, y):
                break
            f = chessboard.board[x][y]
            if f is None:
                result.append((x, y))
            else:
                if f.color != self.color:
                    result.append((x, y))
                break
        return result


class Pawn(Figure):
    def list_allowed_moves(self, chessboard):
        baselines = {
            "white": 1,
            "black": 6
        }
        direction = {
            "white": 1,
            "black": -1
        }
        result = []
        x, y = self.x, self.y + direction[self.color]
        if chessboard.isinside(x, y) and chessboard.board[x][y] is None:
            result.append((x, y))
            if self.y == baselines[self.color]:
                x, y = x, y + direction[self.color]
                if chessboard.isinside(x, y) and chessboard.board[x][y] is None:
                    result.append((x, y))

        x, y = self.x - 1, self.y + direction[self.color]
        if (
                chessboard.isinside(x, y)
                and chessboard.board[x][y] is not None
                and chessboard.board[x][y].color != self.color
        ):
            result.append((x, y))

        x, y = self.x + 1, self.y + direction[self.color]
        if (
                chessboard.isinside(x, y)
                and chessboard.board[x][y] is not None
                and chessboard.board[x][y].color != self.color
        ):
            result.append((x, y))

        return result


class Knight(Figure):
    def list_allowed_moves(self, chessboard):
        jumps = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        potential_result = [
            (self.x + dx, self.y + dy) for (dx, dy) in jumps]
        result = []
        for x, y in potential_result:
            if not chessboard.isinside(x, y):
                continue
            f = chessboard.board[x][y]
            if f is None or f.color != self.color:
                result.append((x, y))
        return result




class Rook(Figure):
    def list_allowed_moves(self, chessboard):
        return (
            self.moves_in_dir(1, 0, 7, chessboard)
            + self.moves_in_dir(-1, 0, 7, chessboard)
            + self.moves_in_dir(0, 1, 7, chessboard)
            + self.moves_in_dir(0, -1, 7, chessboard)
        )


class King(Figure):
    def list_allowed_moves(self, chessboard):
        return (
            self.moves_in_dir(1, 0, 1, chessboard)
            + self.moves_in_dir(-1, 0, 1, chessboard)
            + self.moves_in_dir(0, 1, 1, chessboard)
            + self.moves_in_dir(0, -1, 1, chessboard)
            + self.moves_in_dir(1, 1, 1, chessboard)
            + self.moves_in_dir(1, -1, 1, chessboard)
            + self.moves_in_dir(-1, 1, 1, chessboard)
            + self.moves_in_dir(-1, -1, 1, chessboard)
        )


class Bishop(Figure):
    def list_allowed_moves(self, chessboard):
        return (
            self.moves_in_dir(1, 1, 7, chessboard)
            + self.moves_in_dir(1, -1, 7, chessboard)
            + self.moves_in_dir(-1, 1, 7, chessboard)
            + self.moves_in_dir(-1, -1, 7, chessboard)
        )


class Queen(Figure):
    def list_allowed_moves(self, chessboard):
        return (
            self.moves_in_dir(1, 0, 7, chessboard)
            + self.moves_in_dir(-1, 0, 7, chessboard)
            + self.moves_in_dir(0, 1, 7, chessboard)
            + self.moves_in_dir(0, -1, 7, chessboard)
            + self.moves_in_dir(1, 1, 7, chessboard)
            + self.moves_in_dir(1, -1, 7, chessboard)
            + self.moves_in_dir(-1, 1, 7, chessboard)
            + self.moves_in_dir(-1, -1, 7, chessboard)
        )
