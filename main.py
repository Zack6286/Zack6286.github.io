import pygame
import random

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Math Quest")
font = pygame.font.Font(None, 48)
small_font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# Generate a random math question and answer
def get_question():
    a, b = random.randint(1, 12), random.randint(1, 12)
    op = random.choice(["+", "-", "*"])
    if op == "+":
        ans = a + b
    elif op == "-":
        ans = a - b
    else:
        ans = a * b
    return f"{a} {op} {b}", ans

def main():
    questions = 5
    score = 0
    quest
