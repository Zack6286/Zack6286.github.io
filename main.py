# math_game_async.py
import pygame
import random
import asyncio

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Math Quest")
font = pygame.font.Font(None, 48)
clock = pygame.time.Clock()

# Questions and game state
score = 0
level = 1
questions_per_level = 5
question_index = 0
question = ""
answer = 0
user_answer = ""
feedback = ""
time_limit = 30  # seconds
time_left = time_limit
show_feedback = False

def new_question():
    global question, answer, user_answer, time_left
    limit = level * 10
    a, b = random.randint(1, limit), random.randint(1, limit)
    op = random.choice(["+", "-", "*"])
    if op == "+":
        answer = a + b
    elif op == "-":
        answer = a - b
    else:
        answer = a * b
    question = f"{a} {op} {b} = ?"
    user_answer = ""
    time_left = time_limit

async def main():
    global user_answer, score, level, question_index, feedback, show_feedback
    running = True
    new_question()

    while running:
        screen.fill((30, 30, 30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_answer = user_answer[:-1]
                elif event.key == pygame.K_RETURN:
                    if user_answer.isdigit() and int(user_answer) == answer:
                        feedback = "Correct!"
                        score += 1
                    else:
                        feedback = f"Wrong! Answer was {answer}"
                    show_feedback = True
                    await asyncio.sleep(1.5)
                    show_feedback = False

                    question_index += 1
                    if question_index >= questions_per_level:
                        if score >= 3:
                            level += 1
                            feedback = "Level up!"
                        else:
                            feedback = "Game Over"
                            running = False
                        await asyncio.sleep(2)
                        question_index = 0
                        score = 0 if feedback == "Game Over" else score

                    new_question()
                elif event.unicode.isdigit():
                    user_answer += event.unicode

        # Render question and input
        question_surface = font.render(question, True, (255, 255, 255))
        input_surface = font.render(user_answer, True, (100, 255, 100))
        level_surface = font.render(f"Level {level}  Score {score}", True, (180, 180, 255))

        screen.blit(question_surface, (100, 150))
        screen.blit(input_surface, (100, 220))
        screen.blit(level_surface, (100, 50))

        if show_feedback:
            feedback_surface = font.render(feedback, True, (255, 180, 180))
            screen.blit(feedback_surface, (100, 300))

        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)

asyncio.run(main())
# Placeholder for main.py content — replace with actual logic
