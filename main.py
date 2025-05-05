import pygame
import random
import json
import asyncio
import os

pygame.init()
pygame.mixer.init()

# Load music
pygame.mixer.music.load("music_madness.ogg")
pygame.mixer.music.play(-1)

# Load cat sprite (replace with actual image in assets)
cat_image = pygame.image.load("cat_sprite.png")
cat_image = pygame.transform.scale(cat_image, (100, 100))

# Load scores
SCORE_FILE = "scoreboard.json"
def load_scores():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_score(name, score):
    scores = load_scores()
    scores[name] = max(score, scores.get(name, 0))
    with open(SCORE_FILE, 'w') as f:
        json.dump(scores, f)

# Setup display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Math Quest")
font = pygame.font.SysFont(None, 36)

# Ask question
def ask_question(level):
    max_num = level * 10
    a = random.randint(1, max_num)
    b = random.randint(1, max_num)
    op = random.choice(["+", "-", "*"])
    if op == "+":
        answer = a + b
    elif op == "-":
        answer = a - b
    else:
        answer = a * b
    question = f"{a} {op} {b}"
    return question, answer

# Draw text
def draw_text(text, y):
    surface = font.render(text, True, (255, 255, 255))
    rect = surface.get_rect(center=(400, y))
    screen.blit(surface, rect)

# Async game loop for browser
async def main():
    clock = pygame.time.Clock()
    score = 0
    level = 1
    name = "Player"

    running = True
    input_text = ""
    question, answer = ask_question(level)

    while running:
        screen.fill((20, 20, 40))
        screen.blit(cat_image, (350, 100))

        draw_text(f"Score: {score}", 20)
        draw_text(f"Level: {level}", 60)
        draw_text(f"Question: {question}", 200)
        draw_text(f"Answer: {input_text}", 250)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        if int(input_text.strip()) == answer:
                            score += 1
                            if score % 5 == 0:
                                level += 1
                        else:
                            running = False
                        question, answer = ask_question(level)
                    except:
                        pass
                    input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)

    save_score(name, score)

# Launch async main for Pygbag
asyncio.run(main())
