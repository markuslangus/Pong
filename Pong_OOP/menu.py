import pygame as pg
from settings import *

class Menu:
    def __init__(self, game):
        self.game = game

    def game_over(self):
        if self.game.score_player == 3 or self.game.score_ai == 3:
            self.game.game_over = True
            
            while self.game.game_over:
                font = pg.font.Font(None, GAME_OVER_SIZE)
                if self.game.score_player > self.game.score_ai:
                    winner = font.render("Player 1 wins", True, GREEN)
                else:
                    winner = font.render("Pongie wins", True, RED)
                self.game.screen.blit(winner, GAME_OVER_POSITION)

                font2 = pg.font.Font(None, 40)
                info1 = font2.render("press 'r' for restart", True, WHITE)
                info2 = font2.render("press 'esc' for escape", True, WHITE)
                self.game.screen.blit(info1, INFO1_POSITION)
                self.game.screen.blit(info2, INFO2_POSITION)
                
                self.game.handle_events()
                pg.display.flip()
