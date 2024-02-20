import pygame as pg
import sys
from settings import *
from ball import *
from paddle import *
from menu import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pg.time.Clock()
        self.new_game()

    def new_game(self):
        self.ball = Ball(self)
        self.paddle_player = Paddle(self, True)
        self.paddle_ai = Paddle(self, False)
        self.menu = Menu(self)
        
        self.score_player = 0
        self.score_ai = 0
        self.score = False
        self.game_over = False

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit() 
            elif (event.type == pg.KEYDOWN and event.key == pg.K_r):
                self.new_game()
                self.run()

    def update(self):
        self.ball.update()
        self.paddle_player.move()
        self.paddle_ai.move()
        self.menu.game_over()
        
        self.clock.tick(FPS)
        pg.display.set_caption("Pong")

    def draw(self):
        self.screen.fill(BLACK)
        
        self.ball.draw(self.screen)
        self.paddle_player.draw(self.screen)
        self.paddle_ai.draw(self.screen)
        self.draw_score(self.screen)
        
        pg.display.flip()

    def draw_score(self, screen):
        font = pg.font.Font(None, FONT_SIZE)
        
        score_surf_player = font.render(str(self.score_player), True, GREEN)
        name_surf_player = font.render("Player 1", True, GREEN)
        screen.blit(score_surf_player, SCORE_POSITION_PLAYER)
        screen.blit(name_surf_player, NAME_POSITION_PLAYER)
        
        score_surf_ai = font.render(str(self.score_ai), True, RED)
        name_surf_ai = font.render("Pongie", True, RED)
        screen.blit(score_surf_ai, SCORE_POSITION_AI)
        screen.blit(name_surf_ai, NAME_POSITION_AI)
    
    def run(self):
        while True:
            if self.score:
                pg.time.delay(1000)
                self.score = False
            self.handle_events()
            self.update()
            self.draw()

if __name__ == "__main__":
    game = Game()
    game.run()
