from config import DOWN, DIAGONALLY_DOWN_LEFT, DIAGONALLY_UP_RIGHT, DIAGONALLY_DOWN_RIGHT, DIAGONALLY_UP_LEFT, CELL, FPS, UP, LEFT, RIGHT
import pygame as pg

def direction_from_keys(keys, current_dir):
    dr = dc = 0
    if keys[pg.K_w] or keys[pg.K_UP]:
        if current_dir != DOWN:
            dr = -1
    if keys[pg.K_s] or keys[pg.K_DOWN]:  
        if current_dir != UP:
            dr = 1
    if keys[pg.K_a] or keys[pg.K_LEFT]: 
        if current_dir != RIGHT:
            dc = -1
    if keys[pg.K_d] or keys[pg.K_RIGHT]: 
        if current_dir != LEFT:
            dc = 1
    if dr == 0 and dc == 0:
        return current_dir               
    dr = max(-1, min(1, dr))
    dc = max(-1, min(1, dc))
    new_dir = (dr, dc)

    if current_dir == DIAGONALLY_UP_LEFT:
        if new_dir == DIAGONALLY_DOWN_RIGHT:
            return current_dir
    if current_dir == DIAGONALLY_UP_RIGHT:
        if new_dir == DIAGONALLY_DOWN_LEFT:
            return current_dir
    if current_dir == DIAGONALLY_DOWN_RIGHT:
        if new_dir == DIAGONALLY_UP_LEFT:
            return current_dir
    if current_dir == DIAGONALLY_DOWN_LEFT:
        if new_dir == DIAGONALLY_UP_RIGHT:
            return current_dir
    return new_dir

def draw_game(surface, game):
    surface.fill((16,39,146))
    M = game.board_matrix()
    h, w = game.height, game.width
    time_now = pg.time.get_ticks()

    for r in range(h):
        for c in range(w):
            val = M[r][c]
            if val is None:
                continue
            if val == "A":
                color = (220, 70, 70)
                if game.apple.golden_apple:
                    lifetime = 5000  
                    elapsed  = max(0, time_now - game.apple.golden_apple_spawn_time)
                    remaining = max(0, lifetime - elapsed)
                    start_ms, end_ms = 300, 80
                    blink_period = int(end_ms + (start_ms - end_ms) * (remaining / lifetime))
                    if blink_period < 40: 
                        blink_period = 40
                    phase = (time_now // blink_period) % 2
                    color = (255, 215, 0) if phase == 0 else (255, 165,  0)
                if game.apple.toxic_apple:
                    color = (134, 1, 175)
                        
            elif val == "X":
                color = (0, 200, 120)   
            else:
                color = (0, 140, 100)   
            x, y = c * CELL, r * CELL
           
            pg.draw.rect(surface, color, (x+2, y+2, CELL-4, CELL-4), border_radius=5)