import pygame
from settings import *
from fruit import SuperFruit

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((WINDOW_X // 2), (WINDOW_Y // 2))]
        self.direction = pygame.Vector2(1, 0)

    def move(self):
        current_head = self.positions[0]
        new_head = ((current_head[0] + self.direction[0] * GRID_SIZE) % WINDOW_X,
                    (current_head[1] + self.direction[1] * GRID_SIZE) % WINDOW_Y)
        self.positions.insert(0, new_head)

        if len(self.positions) > self.length:
            self.positions.pop()

    def draw(self, surface):
        for pos in self.positions:
            pygame.draw.rect(surface, white, (pos[0], pos[1], GRID_SIZE, GRID_SIZE))
    
    def eatCheck(self, fruit):
        head_pos = self.positions[0]
        if head_pos[0] == fruit.position[0] and head_pos[1] == fruit.position[1]:
            return True
        else:
            return False
    
    def collisionCheck(self):
        head_pos = self.positions[0]
        if head_pos in self.positions[1:]:
            return True
        else:
            return False

        
    def eat(self):
        current_head = self.positions[0]
        new_part = ((current_head[0] + self.direction[0] * GRID_SIZE) % WINDOW_X,
                    (current_head[1] + self.direction[1] * GRID_SIZE) % WINDOW_Y)
        self.length+=1
        self.positions.append(new_part)

