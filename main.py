
import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Math Quest: Online Edition")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

WHITE, BLACK = (255, 255, 255), (0, 0, 0)
LIGHT_BLUE, GREEN, RED, GRAY = (173, 216, 230), (0, 255, 0), (255, 0, 0), (200, 200, 200)

settings = {
    "time_limit": 20,
    "choices": 4,
    "topics": {
        "arithmetic": True,
        "fractions": True,
        "decimals": True,
        "geometry": False,
        "algebra": False
    }
}

score, level, high_score = 0, 1, 0

def post_score_online(name, score):
    print(f"[ONLINE] Score posted: {name} - {score} (simulated)")

def generate_arithmetic():
    a, b = random.randint(10, 99), random.randint(1, 9)
    op = random.choice(["+", "-", "*", "/"])
    question = f"{a} {op} {b}"
    return question, round(eval(question), 2)

def generate_fraction():
    a, b = random.randint(1, 9), random.randint(1, 9)
    c, d = random.randint(1, 9), random.randint(1, 9)
    question = f"{a}/{b} + {c}/{d}"
    return question, round(a/b + c/d, 2)

def generate_decimal():
    a = round(random.uniform(0.1, 9.9), 1)
    b = round(random.uniform(0.1, 9.9), 1)
    op = random.choice(["+", "-", "*", "/"])
    question = f"{a} {op} {b}"
    try:
        answer = round(eval(question), 2)
    except ZeroDivisionError:
        return generate_decimal()
    return question, answer

def get_question():
    generators = []
    if settings["topics"]["arithmetic"]:
        generators.append(generate_arithmetic)
    if settings["topics"]["fractions"]:
        generators.append(generate_fraction)
    if settings["topics"]["decimals"]:
        generators.append(generate_decimal)
    gen = random.choice(generators)
    return gen()

def generate_choices(correct, total=4):
    choices = [correct]
    while len(choices) < total:
        fake = round(correct + random.uniform(-10, 10), 2)
        if fake not in choices:
            choices.append(fake)
    random.shuffle(choices)
    return choices

def draw_text(text, x, y, color=BLACK):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

def main():
    global score, level
    running = True
    question, answer = get_question()
    choices = generate_choices(answer, settings["choices"])
    selected = None
    timer = settings["time_limit"]
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    while running:
        screen.fill(WHITE)
        draw_text(f"Score: {score} | Level: {level}", 20, 20)
        draw_text(f"Time Left: {timer}", WIDTH - 200, 20)
        draw_text(f"Q: {question}", 100, 100)

        for i, choice in enumerate(choices):
            color = LIGHT_BLUE if selected == i else GRAY
            pygame.draw.rect(screen, color, (100, 200 + i * 80, 300, 50))
            draw_text(str(choice), 120, 210 + i * 80)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.USEREVENT:
                timer -= 1
                if timer <= 0:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                for i in range(len(choices)):
                    if 100 <= mx <= 400 and 200 + i * 80 <= my <= 250 + i * 80:
                        selected = i
                        if choices[i] == answer:
                            score += 10
                            level += 1
                        else:
                            score -= 5
                        question, answer = get_question()
                        choices = generate_choices(answer, settings["choices"])
                        selected = None
                        timer = settings["time_limit"]

        pygame.display.flip()
        clock.tick(30)

    post_score_online("Player", score)
    pygame.quit()
    sys.exit()

main()
