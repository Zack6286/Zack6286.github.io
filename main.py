import pygame
import random
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Math Quest")
font = pygame.font.SysFont(None, 48)
clock = pygame.time.Clock()

# Load sound effects (make sure these files exist in your project folder)
correct_sound = pygame.mixer.Sound("correct.wav")
wrong_sound = pygame.mixer.Sound("wrong.wav")

def get_question():
    a, b = random.randint(1, 12), random.randint(1, 12)
    op = random.choice(["+", "-", "*"])
    if op == "+":
        ans = a + b
    elif op == "-":
        ans = a - b
    else:
        ans = a * b
    q_text = f"{a} {op} {b}"
    return q_text, ans

def main():
    questions = 5
    score = 0
    question_index = 0
    input_text = ""
    feedback = ""
    game_state = "ask"
    q_text, answer = get_question()

    while True:
        screen.fill((30, 30, 30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if game_state == "ask":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if input_text.strip().isdigit() and int(input_text.strip()) == answer:
                            feedback = "Correct!"
                            score += 1
                            correct_sound.play()
                        else:
                            feedback = f"Wrong! Answer was {answer}"
                            wrong_sound.play()
                        question_index += 1
                        input
