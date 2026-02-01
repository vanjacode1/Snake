
from utils import draw_game, direction_from_keys
from core import Game
import pygame as pg
from config import CELL, FPS


if __name__ == "__main__":
    
    WIDTH, HEIGHT = 25, 25
    pg.init()

    screen = pg.display.set_mode((WIDTH * CELL, HEIGHT * CELL))
    pg.display.set_caption("Snake (Press Esc to quit the game)")
    clock = pg.time.Clock()
    font  = pg.font.SysFont("consolas,menlo,monospace", 18)

    game = Game(WIDTH, HEIGHT)
    alive = True
    score = 0

    while True:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit(); raise SystemExit
            if e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE:
                pg.quit(); raise SystemExit

        # allow diagonals with simultaneous keys)
        keys = pg.key.get_pressed()
        new_dir = direction_from_keys(keys, game.snake.direction)
        game.snake.set_direction(new_dir)

        # update (only if alive)
        if alive:

            # move one step 
            game.snake.take_step()

            # self-collision
            if not game.snake.valid_move():
                alive = False

            if game.apple.golden_apple:
                now = pg.time.get_ticks()

                # 3 seconds = 3000 ms
                if now - game.apple.golden_apple_spawn_time > 3000: 
                    game.apple.spawn_apple(game.snake.body)

            if game.apple.toxic_apple:
                game.apple.chase(game.snake.head(), game.snake.body)

            # eating
            if game.snake.head() == game.apple.location:

                # growth function extends the tail
                if game.apple.toxic_apple:
                    #game.snake.shrink_body()
                    alive = False
                elif game.apple.golden_apple:
                    for _ in range(5):
                        game.snake.grow_body()
                    score += 5
                else:
                    game.snake.grow_body()
                    score += 1
                if alive:
                    game.apple.spawn_apple(game.snake.body)

        # draw 
        draw_game(screen, game)
        if not alive:
            msg = font.render("Game Over — press R to restart, Esc to quit", True, (240,240,240))
            screen.blit(msg, (10, 10))
        else:
            hud = font.render(f"Score: {score}", True, (240,240,240))
            screen.blit(hud, (10, 10))
        pg.display.flip()
        clock.tick(FPS)

        # restart key R
        if not alive and (pg.key.get_pressed()[pg.K_r]):
            game = Game(WIDTH, HEIGHT)
            alive = True
            score = 0