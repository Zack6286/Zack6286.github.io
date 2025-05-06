import pygame
import random
import sys
import asyncio

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Math Quest")
font = pygame.font.SysFont(None, 48)
clock = pygame.time.Clock()

async def main():
    questions = 5
    score = 0
    question_index = 0
    input_text = ""
    feedback = ""
    game_state = "ask"

    def get_question():
        a, b = random.randint(1, 12), random.randint(1, 12)
        op = random.choice(["+", "-", "*"])
        ans = eval(f"{a}{op}{b}")
        return f"{a} {op} {b}", ans

    q_text, answer = get_question()

    running = True
    while running:
        screen.fill((30, 30, 30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if game_state == "ask":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if input_text.strip().isdigit() and int(input_text.strip()) == answer:
                            feedback = "Correct!"
                            score += 1
                        else:
                            feedback = f"Wrong! Answer was {answer}"
                        question_index += 1
                        input_text = ""
                        if question_index < questions:
                            q_text, answer = get_question()
                        else:
                            game_state = "end"
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode

        if game_state == "ask":
            screen.blit(font.render(f"Q{question_index + 1}: {q_text}", True, (255, 255, 255)), (50, 100))
            screen.blit(font.render(f"Your Answer: {input_text}", True, (255, 255, 0)), (50, 180))
            screen.blit(font.render(feedback, True, (100, 255, 100)), (50, 260))
        elif game_state == "end":
            screen.blit(font.render(f"You scored {score} out of {questions}!", True, (0, 200, 255)), (50, 240))

        pygame.display.flip()
        await asyncio.sleep(0)
