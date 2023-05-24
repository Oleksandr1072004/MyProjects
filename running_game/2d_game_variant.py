import pygame
import pygame_menu
import random
import json

filename = "records.json"

# initialize pygame
pygame.init()

# set screen size
screen_width = 800
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Running Game")
car_image_menu = pygame_menu.baseimage.BaseImage("images/75825.png")
car_image_menu.scale(0.3,0.3)

# sound, when you click any button
button_click_s = \
        pygame.mixer.Sound(
            'sounds/mixkit-arcade-game-jump-coin-216.wav')


def game():
    pygame.mixer.Sound.play(button_click_s)
    username = user_input.get_value()
    if len(username) > 0:
        carImg = pygame.image.load(
            'images/pngtree-car-top-view-image-png-image_6557068.png')
        CarImg_i = pygame.transform.scale(carImg, (120, 130))
        obstacleImg = pygame.image.load('images/bullet_hole_PNG6050.png')
        obstacle_img_i = pygame.transform.scale(obstacleImg, (110, 110))

        img_life = pygame.image.load("images/heart-icon.png")
        img_life_small = pygame.transform.scale(img_life, (35, 35))

        # set life attributes
        lives = 9
        live_font = pygame.font.Font(None, 50)

        meter = 0

        # set background color
        bg_color = (0, 1, 1)

        # set player attributes
        player_width = 70
        player_height = 75
        player_x = screen_width // 2 - player_width // 2
        player_y = screen_height - player_height - 60
        player_speed = 1

        # set obstacle attributes
        obstacle_width = 100
        obstacle_height = 100
        obstacle_x = random.randint(0, screen_width - obstacle_width)
        obstacle_y = -obstacle_height
        obstacle_speed = 0.5

        # set coin attributes
        coin_width = 25
        coin_height = 25
        coin_x = random.randint(0, screen_width - coin_width)
        coin_y = -coin_height
        coin_speed = 1

        # set counter attributes
        counter = 0
        counter_font = pygame.font.Font(None, 30)
        meter_font = pygame.font.Font(None, 30)
        #
        side_road_markup_left_width = 8
        side_road_markup_left_height = screen_height
        side_road_markup_left_x = 1
        side_road_markup_left_y = 0

        side_road_markup_right_width = 8
        side_road_markup_right_height = screen_height
        side_road_markup_right_x = screen_width - 10
        side_road_markup_right_y = 0

        #
        road_markup_left_width = 12
        road_markup_left_height = 250
        road_markup_left_x = screen_width // 3
        road_markup_left_y = -road_markup_left_height
        road_markup_left_speed = 1.5

        road_markup_right_width = 12
        road_markup_right_height = 250
        road_markup_right_x = screen_width / 1.5
        road_markup_right_y = -road_markup_right_height
        road_markup_right_speed = 1.5

        # sounds
        game_over_s = \
            pygame.mixer.Sound(
                'sounds/mixkit-arcade-retro-game-over-213.wav')
        shotdown_obstacle_s = \
            pygame.mixer.Sound(
                'sounds/mixkit-blow-breaking-the-air-2057.wav')
        collect_money_s = \
            pygame.mixer.Sound(
                'sounds/mixkit-atm-cash-machine-key-press-2841.wav')

        # game loop
        while True:
            # handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # handle player movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player_x > 0:
                player_x -= player_speed
            if keys[pygame.K_RIGHT] and player_x < screen_width - (player_width+25):
                player_x += player_speed
            screen.blit(CarImg_i, (player_x, player_y))

            road_markup_left_y += road_markup_left_speed
            road_markup_right_y += road_markup_right_speed

            # update obstacle and coin positions
            obstacle_y += obstacle_speed
            coin_y += coin_speed

            road_markup_left_rect = pygame.Rect(road_markup_left_x,
                                                road_markup_left_y,
                                                road_markup_left_width,
                                                road_markup_left_height)
            road_markup_right_rect = pygame.Rect(road_markup_right_x,
                                                 road_markup_right_y,
                                                 road_markup_right_width,
                                                 road_markup_right_height)
            # check if obstacle and coin collide with player
            obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width,
                                        obstacle_height)
            coin_rect = pygame.Rect(coin_x, coin_y, coin_width, coin_height)
            player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
            if obstacle_rect.colliderect(player_rect):
                obstacle_x = random.randint(0, screen_width - coin_width)
                obstacle_y = -obstacle_height
                lives -= 1
                if lives == 0:
                    pygame.mixer.Sound.play(game_over_s)
                    if counter == 1:
                        print("Game Over\nCounter: {} money".format(counter))
                    else:
                        print("Game Over\nCounter: {} moneys".format(counter))
                    pygame.quit()
                    dict_record = {"Username:": username, "Counter:":counter, "Distance:":int(meter)}
                    with open(filename, 'w', encoding='utf-8') as f_w:
                        json.dump(dict_record, f_w)
                    exit()
                pygame.mixer.Sound.play(shotdown_obstacle_s)

            elif coin_rect.colliderect(player_rect):
                coin_x = random.randint(0, screen_width - coin_width)
                coin_y = -coin_height
                counter += 1
                pygame.mixer.Sound.play(collect_money_s)

            # check if obstacle and coin are out of screen
            if obstacle_y > screen_height:
                obstacle_x = random.randint(0, screen_width - obstacle_width)
                obstacle_y = -obstacle_height
            if coin_y > screen_height:
                coin_x = random.randint(0, screen_width - coin_width)
                coin_y = -coin_height
            if road_markup_left_y >= (screen_height) and \
                road_markup_right_y >= (screen_height):
                road_markup_left_x = screen_width // 3
                road_markup_left_y = -road_markup_left_height
                road_markup_right_x = screen_width / 1.5
                road_markup_right_y = -road_markup_right_height

            meter += road_markup_left_speed/50
            # draw screen
            screen.fill(bg_color)

            pygame.draw.rect(screen, (255, 255, 255),
                             (side_road_markup_left_x, side_road_markup_left_y,
                              side_road_markup_left_width,
                              side_road_markup_left_height))
            pygame.draw.rect(screen, (255, 255, 255),
                             (side_road_markup_right_x, side_road_markup_right_y,
                              side_road_markup_right_width,
                              side_road_markup_right_height))
            pygame.draw.rect(screen, (255, 255, 255),
                             (road_markup_left_x, road_markup_left_y,
                              road_markup_left_width,
                              road_markup_left_height))
            pygame.draw.rect(screen, (255, 255, 255),
                             (road_markup_right_x, road_markup_right_y,
                              road_markup_right_width, road_markup_right_height))
            # pygame.draw.rect(screen, (255, 0, 0),
            #                  (obstacle_x, obstacle_y, obstacle_width, obstacle_height))
            pygame.draw.rect(screen, (255, 255, 0),
                             (coin_x, coin_y, coin_width, coin_height))
            screen.blit(CarImg_i, (player_x, player_y))
            screen.blit(obstacle_img_i, (obstacle_x, obstacle_y))
            # pygame.draw.rect(screen, (0, 0, 255),
            #                  (player_x, player_y, player_width, player_height))
            screen.blit(img_life_small, (745, 10))
            # draw counter
            if counter == 1:
                counter_text = counter_font.render(
                    "Counter: {} money".format(counter), True, (250, 250, 250))
            else:
                counter_text = counter_font.render(
                    "Counter: {} moneys".format(counter), True, (250, 250, 250))
            screen.blit(counter_text, (15, 10))
            meter_text = meter_font.render(
                "Distance: {} m".format(int(meter)), True, (250, 250, 250))
            screen.blit(meter_text, (15,40))

            live_text = live_font.render(
                "{}".format(int(lives)), True, (250, 5, 0))
            screen.blit(live_text, (720, 12))
            # update screen
            pygame.display.update()
    else:
        print('You will enter your name!')


def exit_game():
    pygame.mixer.Sound.play(button_click_s)
    pygame_menu.events.EXIT()


menu = pygame_menu.Menu('Menu', 700, 500, theme=pygame_menu.themes.THEME_BLUE)
user_input = menu.add_text_input('Your name: ')
menu.add_image(image_path=car_image_menu.copy())
menu.add_button('Start',game)
menu.add_button('Exit',exit_game)
menu.mainloop(screen)