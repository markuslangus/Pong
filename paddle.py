import pygame as pg
from settings import *

class Paddle:
    def __init__(self, game, is_player=True):
        self.game = game
        self.is_player = is_player

        self.velocity = PADDLE_DY
        
        if is_player == True:
            self.rect = pg.Rect(PADDLE1_INIT_X, PADDLE1_INIT_Y, PADDLE_WIDTH, PADDLE_HEIGHT)
            self.color = GREEN
        else:
            self.rect = pg.Rect(PADDLE2_INIT_X, PADDLE2_INIT_X, PADDLE_WIDTH, PADDLE_HEIGHT)
            self.color = RED

    def move(self):
        if self.is_player:
            keys = pg.key.get_pressed()
            if keys[pg.K_UP] and self.rect.top > 0:
                self.rect.y -= self.velocity
            if keys[pg.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
                self.rect.y += self.velocity
        else:
            self.move_ai()

    def move_ai(self):
        if self.game.ball.position.y < self.rect.centery and self.rect.top > 0:
            self.rect.y -= self.velocity
        elif self.game.ball.position.y > self.rect.centery and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.velocity
        
    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)
