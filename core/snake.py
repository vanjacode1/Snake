class Snake:
    def __init__(self, start_body, start_direction):
        self.body = start_body
        self.direction = start_direction

    def take_step(self):
        r, c = self.head()
        dr, dc = self.direction
        nr = (r + dr) % 25
        nc = (c + dc) % 25
        self.body = self.body[1:] + [(nr, nc)] 

    def set_direction(self, direction):
        self.direction = direction
    
    def head(self):
        return self.body[-1]
    
    def valid_move(self):
        return self.head() not in self.body[:-1]
    
    def grow_body(self):
        if len(self.body) > 1:
            tail_dir = (self.body[0][0] - self.body[1][0], self.body[0][1] - self.body[1][1])
            new_tail = (self.body[0][0] + tail_dir[0], self.body[0][1] + tail_dir[1])
        else:
            dr, dc = self.direction
            new_tail = (self.body[0][0] - dr, self.body[0][1] - dc)

        self.body.insert(0, new_tail)
    
    def shrink_body(self):
        self.body = self.body[4:]