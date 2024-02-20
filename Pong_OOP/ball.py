import pygame as pg
from pygame.math import Vector2
import random
from settings import *

class Ball:
    def __init__(self, game):
        self.game = game
        
        self.position = Vector2(BALL_INIT_X, BALL_INIT_Y)
        self.velocity = Vector2(BALL_DX, BALL_DY)
        self.radius = BALL_RADIUS
        self.color = BALL_COLOR

    def update(self):
        self.move()
        self.ball_collision(self.game.paddle_player.rect, self.game.paddle_ai.rect)
        self.check_score_update()

    def move(self):
        if self.velocity.x > BALL_MAX_SPEED:
            self.velocity.x = BALL_MAX_SPEED
        if self.velocity.y > BALL_MAX_SPEED:
            self.velocity.y = BALL_MAX_SPEED
            
        self.position += self.velocity

    def draw(self, screen):
        pg.draw.circle(screen, self.color, self.position, self.radius)

    def reset_ball(self):
        self.position = Vector2(BALL_INIT_X, BALL_INIT_Y)
        self.velocity = Vector2(BALL_DX, random.choice(list(range(-5, 0)) + list(range(1, 6))))
        
    def ball_collision(self, paddle_player, paddle_ai):
        if paddle_player.left <= self.position.x - self.radius <= paddle_player.right and paddle_player.top - self.radius <= self.position.y  <= paddle_player.bottom + self.radius:
            self.velocity.x *= -1.5
        elif paddle_ai.left <= self.position.x + self.radius <= paddle_ai.right and paddle_ai.top - self.radius <= self.position.y <= paddle_ai.bottom + self.radius:
            self.velocity.x *= -1.5
        elif -20 <= self.position.y <= 0 + self.radius or SCREEN_HEIGHT + 20 >= self.position.y >= SCREEN_HEIGHT - self.radius:
            self.velocity.y *= -1.5

    def check_score_update(self):
        if self.position.x < 0:
            self.reset_ball()
            self.game.score_ai += 1
            self.game.score = True
        elif self.position.x > SCREEN_WIDTH:
            self.reset_ball()
            self.game.score_player += 1
            self.game.score = True
