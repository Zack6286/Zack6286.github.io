import pygame
import random
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Math Quest")
font = pygame.font.SysFont(None, 48)
small_font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

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

    print("Game started!")

    while True:
        screen.fill((30, 30, 30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if game_state == "ask":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if input_text.strip().isdigit():
                            if int(input_text.strip()) == answer:
                                feedback = "✅ Correct!"
                                score += 1
                            else:
                                feedback = f"❌ Wrong! Answer was {answer}"

                            question_index += 1
                            input_text = ""
                            if question_index >= questions:
                                game_state = "done"
                            else:
                                q_text, answer = get_question()
                        else:
                            feedback = "Please enter a number."
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        if event.unicode.isdigit():
                            input_text += event.unicode

        if game_state == "ask":
            screen.blit(font.render(f"Q{question_index + 1}: {q_text} =", True, (255, 255, 255)), (100, 150))
            screen.blit(font.render(input_text, True, (0, 255, 0)), (100, 220))
            screen.blit(small_font.render(feedback, True, (255, 255, 0)), (100, 280))
        elif game_state == "done":
            screen.blit(font.render(f"You scored {score} out of {questions}!", True, (255, 255, 255)), (100, 250))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
