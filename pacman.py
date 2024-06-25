import random

class PacmanGame:
    def __init__(self):
        self.grid_size = (7, 7)  # Size of the grid
        self.pacman_position = (3, 3)  # Initial position of Pacman
        self.dots = set([(i, j) for i in range(self.grid_size[0]) for j in range(self.grid_size[1])])
        self.ghost_positions = [(0, 0), (6, 0), (0, 6), (6, 6)]  # Initial positions of ghosts

    def print_grid(self):
        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                if (i, j) == self.pacman_position:
                    print("P", end=" ")
                elif (i, j) in self.ghost_positions:
                    print("G", end=" ")
                elif (i, j) in self.dots:
                    print(".", end=" ")
                else:
                    print(" ", end=" ")
            print()

    def move_pacman(self, direction):
        x, y = self.pacman_position
        if direction == "up":
            new_position = (x - 1, y)
        elif direction == "down":
            new_position = (x + 1, y)
        elif direction == "left":
            new_position = (x, y - 1)
        elif direction == "right":
            new_position = (x, y + 1)
        else:
            return False  # Invalid direction

        if 0 <= new_position[0] < self.grid_size[0] and 0 <= new_position[1] < self.grid_size[1]:
            self.pacman_position = new_position
            if self.pacman_position in self.dots:
                self.dots.remove(self.pacman_position)
            self.check_collision()
            return True
        else:
            return False

    def move_ghosts(self):
        for i in range(len(self.ghost_positions)):
            x, y = self.ghost_positions[i]
            dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
            new_position = (x + dx, y + dy)
            if 0 <= new_position[0] < self.grid_size[0] and 0 <= new_position[1] < self.grid_size[1]:
                self.ghost_positions[i] = new_position
                self.check_collision()

    def check_collision(self):
        if self.pacman_position in self.ghost_positions:
            print("Game Over! Pacman got caught by a ghost.")
            exit()

    def play(self):
        print("Welcome to Pacman!")
        while True:
            self.print_grid()
            direction = input("Enter direction (up/down/left/right): ").lower()
            if direction in ["up", "down", "left", "right"]:
                self.move_pacman(direction)
                self.move_ghosts()
            else:
                print("Invalid direction. Use up/down/left/right.")

            if not self.dots:
                print("Congratulations! You ate all the dots. You win!")
                break

if __name__ == "__main__":
    game = PacmanGame()
    game.play()
