import pygame
import random
import sys

# Initialize
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Math Quest")
font = pygame.font.Font(None, 48)
small_font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

def get_question():
    a, b = random.randint(1, 12), random.randint(1, 12)
    op = random.choice(["+", "-", "*"])
    ans = eval(f"{a}{op}{b}")
    return f"{a} {op} {b}", ans

def draw_rotated_text(text, x, y, font, color, angle):
    surface = font.render(text, True, color)
    rotated = pygame.transform.rotate(surface, angle)
    rect = rotated.get_rect(center=(x, y))
    screen.blit(rotated, rect)

def title_screen():
    while True:
        screen.fill((0, 0, 0))
        title = font.render("🎮 Math Quest", True, (255, 255, 255))
        screen.blit(title, (280, 150))

        prompt = small_font.render("Press Enter or Tap to Start", True, (200, 200, 200))
        screen.blit(prompt, (240, 300))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                return

        pygame.display.flip()
        clock.tick(30)

def main():
    high_score = 0

    while True:
        title_screen()

        level = 1
        score = 0
        questions_per_level = 5
        max_levels = 10
        question_count = 0

        current_question, correct_answer = get_question()
        user_answer = ''
        game_over = False
        feedback_timer = 0
        feedback_color = (255, 255, 255)

        while True:
            screen.fill((30, 30, 30))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if game_over:
                        if event.key == pygame.K_RETURN:
                            break
                    elif event.key == pygame.K_RETURN:
                        try:
                            if int(user_answer) == correct_answer:
                                score += 1
                                feedback_color = (0, 255, 0)
                            else:
                                feedback_color = (255, 0, 0)
                            feedback_timer = 30

                            question_count += 1
                            if question_count >= questions_per_level:
                                level += 1
                                question_count = 0
                                if level > max_levels:
                                    game_over = True
                                    high_score = max(score, high_score)
                                    continue

                            current_question, correct_answer = get_question()
                            user_answer = ''
                        except ValueError:
                            pass
                    elif event.key == pygame.K_BACKSPACE:
                        user_answer = user_answer[:-1]
                    elif event.unicode.isdigit() or (event.unicode == '-' and len(user_answer) == 0):
                        user_answer += event.unicode
                elif event.type == pygame.MOUSEBUTTONDOWN and game_over:
                    break

            if game_over:
                screen.blit(font.render("Game Over!", True, (255, 255, 255)), (300, 200))
                screen.blit(small_font.render(f"Score: {score}/{questions_per_level * max_levels}", True, (200, 200, 200)), (270, 260))
                screen.blit(small_font.render(f"High Score: {high_score}", True, (255, 215, 0)), (290, 300))
                screen.blit(small_font.render("Press Enter or Tap to Restart", True, (200, 200, 200)), (230, 350))
            else:
                screen.blit(small_font.render(f"Level {level}", True, (200, 200, 255)), (10, 10))
                screen.blit(small_font.render(f"Question {question_count+1}/{questions_per_level}", True, (180, 180, 180)), (10, 40))

                if level >= 5:
                    draw_rotated_text(current_question, 400, 200, font, (255, 255, 255), 180)
                else:
                    screen.blit(font.render(current_question, True, (255, 255, 255)), (350, 200))

                screen.blit(font.render(user_answer, True, (200, 200, 0)), (350, 260))

                if feedback_timer > 0:
                    sym = "✔" if feedback_color == (0, 255, 0) else "✘"
                    screen.blit(small_font.render(sym, True, feedback_color), (400, 320))
                    feedback_timer -= 1

            pygame.display.flip()
            clock.tick(30)

if __name__ == "__main__":
    main()
