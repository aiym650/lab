import pygame
import random
import psycopg2


WIDTH = 800
HEIGHT = 600


WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (213, 50, 80)
BLACK = (0, 0, 0)
BLUE = (50, 153, 213)


snake_block = 10
snake_speed = 15  


conn = psycopg2.connect(
    dbname="snake_db",
    user="postgres",       
    password="250675", 
    host="localhost",
    port="5432"
)
cur = conn.cursor()


def your_score(screen, score, score_font):
    value = score_font.render("Ваши очки: " + str(score), True, BLACK)
    screen.blit(value, [0, 0])


def message(screen, msg, color, font_style):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 8, HEIGHT / 2])


def our_snake(screen, snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], snake_block, snake_block])


def gameLoop(username):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()

    font_style = pygame.font.SysFont("bahnschrift", 25)
    score_font = pygame.font.SysFont("comicsansms", 35)

    game_over = False
    game_close = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            screen.fill(BLUE)
            message(screen, "Вы проиграли! Q - выход | C - заново", RED, font_style)
            your_score(screen, Length_of_snake - 1, score_font)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop(username)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(BLUE)
        pygame.draw.rect(screen, RED, [foodx, foody, snake_block, snake_block])
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(screen, snake_block, snake_List)
        your_score(screen, Length_of_snake - 1, score_font)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            save_game_state(username, Length_of_snake - 1, 1, snake_speed, 3, "playing")

        clock.tick(snake_speed)

    pygame.quit()
    quit()


def save_game_state(username, score, level, speed, wall_density, game_state):
    cur.execute("SELECT user_id FROM users WHERE username = %s;", (username,))
    user_id = cur.fetchone()[0]

    cur.execute("""
        INSERT INTO user_scores (user_id, score, level, speed, wall_density, game_state)
        VALUES (%s, %s, %s, %s, %s, %s);
    """, (user_id, score, level, speed, wall_density, game_state))
    conn.commit()
    print("Состояние игры сохранено.")


def get_user_level(username):
    cur.execute("SELECT user_id FROM users WHERE username = %s;", (username,))
    result = cur.fetchone()

    if result:
        user_id = result[0]
        cur.execute("""
            SELECT score, level, speed, wall_density 
            FROM user_scores 
            WHERE user_id = %s
            ORDER BY timestamp DESC LIMIT 1;
        """, (user_id,))
        score_data = cur.fetchone()

        if score_data:
            print(f"Добро пожаловать обратно, {username}!")
            print(f"Текущий уровень: {score_data[1]}, Скорость: {score_data[2]}, Стены: {score_data[3]}")
            return score_data[1]
        else:
            print(f"Добро пожаловать, {username}! Начнём с уровня 1.")
            return 1
    else:
        print(f"Пользователь {username} не найден. Создаём нового.")
        create_new_user(username)
        return 1


def create_new_user(username):
    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING user_id;", (username,))
    user_id = cur.fetchone()[0]
    print(f"Создан пользователь {username} с ID {user_id}.")
    create_new_user_score(user_id)


def create_new_user_score(user_id):
    cur.execute("""
        INSERT INTO user_scores (user_id, score, level, speed, wall_density)
        VALUES (%s, 0, 1, 5, 3);
    """, (user_id,))
    conn.commit()


def main():
    username = input("Введите имя пользователя: ")
    current_level = get_user_level(username)
    print(f"Вы начинаете с уровня {current_level}")
    gameLoop(username)


if __name__ == "__main__":
    main()
