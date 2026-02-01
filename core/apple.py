import random
import pygame as pg

class Apple:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.golden_apple = False
        self.golden_apple_spawn_time = 0
        self.toxic_apple = False
        self.toxic_apple_spawn_time = 0
        self.chasing = False
        self.chase_time = 0
        self.last_move = 0
    
    def spawn_apple(self, snake_body=None):
        while True:
            self.location = (random.randint(0, self.height), random.randint(0, self.width))
            if self.location not in snake_body:
                self.golden_apple = (random.random() < 0.1)
                self.golden_apple_spawn_time = pg.time.get_ticks()
                self.toxic_apple = (random.random() < 0.1)
                if self.toxic_apple:
                    self.toxic_apple_spawn_time = pg.time.get_ticks()
                    self.chasing = True
                    self.chase_time = pg.time.get_ticks()
                return self.location
            
    def chase(self, snake_head, snake_body):
        if pg.time.get_ticks() - self.chase_time > 5000:
            self.chasing = False
            self.toxic_apple = False
            return
        
        now = pg.time.get_ticks()
        if now - self.last_move < 200:
            return
        self.last_move = now
        
        ar, ac = self.location
        hr, hc = snake_head
        dr = 0 if ar == hr else (1 if hr > ar else -1)
        dc = 0 if ac == hc else (1 if hc > ac else -1)

        # wrap to board 
        nr = (ar + dr) % (self.height + 1)
        nc = (ac + dc) % (self.width  + 1)
        new_loc = (nr, nc)

        # avoid moving into the snake body (except head)
        if snake_body is not None and new_loc in snake_body[:-1]:
            return 

        self.location = new_loc