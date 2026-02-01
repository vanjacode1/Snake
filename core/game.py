from .snake import Snake
from .apple import Apple
from config import RIGHT

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake = Snake([(10, 4), (10, 5), (10, 6), (10, 7), (10, 8)], RIGHT)
        self.apple = Apple(self.height-1, self.width-1)
        self.apple.spawn_apple(self.snake.body)

    def board_matrix(self):
        matrix = [[None] * self.width for _ in range(self.height)]
        for i,j in self.snake.body:
            matrix[i][j] = "O"
        matrix[self.snake.head()[0]][self.snake.head()[1]] = "X"

        matrix[self.apple.location[0]][self.apple.location[1]] = "A"
        return matrix
    
    def render_board(self):
        M = self.board_matrix()
        print("-" * (self.width*2 +2))
        for i in range(self.height):
            print("|", end="")
            for j in range(self.width):
                if M[i][j] == None:
                    print(" "*2, end="")
                elif M[i][j] == "O":
                    print("O ", end="")
                elif M[i][j] == "A":
                    print("A ", end="")
                else:
                    print("X ", end="")
            print("|")
        print("-" * (self.width*2 +2))