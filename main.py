import pygame
import random
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Math Quest")
font = pygame.font.SysFont(None, 48)
clock = pygame.time.Clock()

def main():
    questions = 5
    score = 0
    question_index = 0
    input_text = ""
    feedback = ""
    game_state = "ask"

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
            render_text = font.render(f"Q{question_index + 1}: {q_text}", True, (255, 255, 255))
            screen.blit(render_text, (50, 100))

            input_render = font.render(f"Your Answer: {input_text}", True, (255, 255, 0))
            screen.blit(input_render, (50, 180))

            feedback_render = font.render(feedback, True, (100, 255, 100))
            screen.blit(feedback_render, (50, 260))

        elif game_state == "end":
            end_text = font.render(f"You scored {score} out of {questions}!", True, (0, 200, 200))
            screen.blit(end_text, (50, 250))

        pygame.display.flip()
        clock.tick(60)

# Call the main game function
main()
