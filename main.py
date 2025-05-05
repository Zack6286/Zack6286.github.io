import pygame
import asyncio
import random

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 50, 200)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
FONT_SIZE = 36
TIMER_SECONDS = 30

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Math Quest")
font = pygame.font.SysFont(None, FONT_SIZE)

clock = pygame.time.Clock()

# Game state
score = 0
question_index = 0
current_question = None
user_answer = ''
feedback = ''
timer_start = 0

def generate_question(level):
    if level >= 5:
        # Flip operands for difficulty
        b, a = random.randint(1, 12), random.randint(1, 12)
    else:
        a, b = random.randint(1, 12), random.randint(1, 12)
    
    op = random.choice(["+", "-", "*"])
    correct = eval(f"{a}{op}{b}")
    return f"{a} {op} {b}", str(correct)

questions = []
for i in range(10):
    q, a = generate_question(i // 2 +_
