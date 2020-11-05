import random


class BefungeInterpreter:
    directions = {
        '>': (0, 1),
        '<': (0, -1),
        '^': (-1, 0),
        'v': (1, 0)
    }

    def __init__(self, code):
        self.code = [[*a] for a in code.splitlines()]
        self.stack = []
        self.output = []
        self.string_mode = False
        self.i = 0
        self.j = 0
        self.direction = ">"

    def add(self):
        self.stack.append(self.stack.pop() + self.stack.pop())

    def sub(self):
        a = self.stack.pop()
        self.stack.append(self.stack.pop() - a)

    def mul(self):
        self.stack.append(self.stack.pop() * self.stack.pop())

    def div(self):
        a = self.stack.pop()
        self.stack.append(0 if a == 0 else self.stack.pop() / a)

    def mod(self):
        a = self.stack.pop()
        self.stack.append(0 if a == 0 else self.stack.pop() % a)

    def logical_not(self):
        self.stack.append(1 if self.stack.pop() == 0 else 0)

    def back_tick(self):
        b = self.stack.pop()
        self.stack.append(1 if b > self.stack.pop() else 0)

    def random_direction(self):
        self.direction = random.choice(list(self.directions.keys()))

    def underscore(self):
        self.direction = '>' if self.stack.pop() == 0 else '<'

    def pipe(self):
        self.direction = 'v' if self.stack.pop() == 0 else '^'

    def move(self):
        _i, _j = self.directions[self.direction]
        self.i += _i
        self.j += _j

    def dup(self):
        self.stack.append(self.stack[-1] if len(self.stack) > 0 else 0)

    def swap(self):
        a = self.stack.pop() if len(self.stack) > 0 else 0
        b = self.stack.pop() if len(self.stack) > 0 else 0
        self.stack.append(a)
        self.stack.append(b)

    def discard(self):
        if len(self.stack) > 0:
            self.stack.pop()

    def dot(self):
        self.output.append(int(self.stack.pop()))

    def comma(self):
        self.output.append(chr(int(self.stack.pop())))

    def put(self):
        x = int(self.stack.pop())
        y = int(self.stack.pop())
        self.code[x][y] = chr(self.stack.pop())

    def get(self):
        x = int(self.stack.pop())
        y = int(self.stack.pop())
        self.stack.append(ord(self.code[x][y]))

    def right(self):
        self.direction = '>'

    def left(self):
        self.direction = '<'

    def up(self):
        self.direction = '^'

    def down(self):
        self.direction = 'v'

    def toggle_string_mode(self):
        self.string_mode = not self.string_mode

    actions = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div,
        "%": mod,
        "!": logical_not,
        "`": back_tick,
        ">": right,
        "<": left,
        "^": up,
        "v": down,
        "?": random_direction,
        "_": underscore,
        "|": pipe,
        ":": dup,
        "\\": swap,
        "$": discard,
        ".": dot,
        ",": comma,
        "#": move,
        "p": put,
        "g": get,
        " ": lambda x: None
    }

    def solve(self):
        char = self.code[self.i][self.j]
        while char != '@':
            if char == '"':
                self.toggle_string_mode()
            elif self.string_mode:
                self.stack.append(ord(char))
            elif char.isdigit():
                self.stack.append(ord(char) - 48)
            else:
                self.actions[char](self)
            self.move()
            char = self.code[self.i][self.j]
        return "".join(map(str, self.output))


def interpret(code):
    return BefungeInterpreter(code).solve()
