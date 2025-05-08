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

def draw_rotated_text(text, x, y, font, color, angle):
    text_surface = font.render(text, True, color)
    rotated_surface = pygame.transform.rotate(text_surface, angle)
    rect = rotated_surface.get_rect(center=(x, y))
    screen.blit(rotated_surface, rect)

def main():
    questions_per_level = 5
    max_levels = 10
    question_count = 0
    score = 0
    level = 1

    current_question, correct_answer = get_question()
    user_answer = ''
    game_over = False

    running = True
    while running:
        screen.fill((30, 30, 30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if game_over:
                    if event.key == pygame.K_RETURN:
                        main()  # restart the game
                        return
                elif event.key == pygame.K_RETURN:
                    try:
                        if int(user_answer) == correct_answer:
                            score += 1
                        question_count += 1

                        if question_count >= questions_per_level:
                            level += 1
                            question_count = 0
                            if level > max_levels:
                                game_over = True
                                continue

                        current_question, correct_answer = get_question()
                        user_answer = ''
                    except ValueError:
                        pass  # Ignore invalid input
                elif event.key == pygame.K_BACKSPACE:
                    user_answer = user_answer[:-1]
                elif event.unicode.isdigit() or (event.unicode == '-' and len(user_answer) == 0):
                    user_answer += event.unicode

        if game_over:
            text = font.render("Game Over!", True, (255, 255, 255))
            screen.blit(text, (300, 200))
            result = small_font.render(f"Final Score: {score}/{questions_per_level * max_levels}", True, (200, 200, 200))
            screen.blit(result, (270, 260))
            prompt = small_font.render("Press Enter to Restart", True, (200, 200, 200))
            screen.blit(prompt, (260, 320))
        else:
            # Display level and question count
            level_text = small_font.render(f"Level {level}", True, (200, 200, 255))
            screen.blit(level_text, (10, 10))
            progress_text = small_font.render(f"Question {question_count + 1}/{questions_per_level}", True, (180, 180, 180))
            screen.blit(progress_text, (10, 40))

            # Display question (rotate if level 5+)
            if level >= 5:
                draw_rotated_text(current_question, 400, 200, font, (255, 255, 255), 180)
            else:
                question_surface = font.render(current_question, True, (255, 255, 255))
                screen.blit(question_surface, (350, 200))

            # Display user input
            input_text = font.render(user_answer, True, (200, 200, 0))
            screen.blit(input_text, (350, 260))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
