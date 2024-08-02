import os
import random
import pygame as pg
import pygame.locals as keys

DIR = os.path.abspath(os.path.dirname(__file__))
WINDOW_SIZE = (800,800)
GREEN = (60,220,30)
GRAY = (50, 50, 50)
WHITE = (255, 255, 255)
YELLOW = (255, 240, 60)
BLACK = (0, 0, 0)

width, height = WINDOW_SIZE
width_road = int(width / 1.6)
separator_width = int(width / 200)
right_access = width / 2 + width_road / 4
left_access = width / 2 - width_road / 4


pg.init()
pg.display.set_caption("Catch a Beer")
screen = pg.display.set_mode(WINDOW_SIZE)
screen.fill(GREEN)
pg.display.update()

# Font
letter = pg.font.SysFont("Comic Sans MS", 30)
higher_letter = pg.font.SysFont("Comic Sans MS", 90)

# Player
player = pg.image.load(os.path.join(DIR, "assets/player", "player.png"))
player = pg.transform.scale(player, (150, 150))
player_position = player.get_rect()
player_position.center = right_access, height * 0.8

# Beer
def load_random_beer():
    i = random.randint(1, 5)
    beer = pg.image.load(os.path.join(DIR, "assets/beers", f"{i}.png"))
    beer = pg.transform.scale(beer, (100, 100))
    beer_position = beer.get_rect()
    if random.randint(0, 1) == 0:
        beer_position.center = right_access, height * 0.2
    else:
        beer_position.center = left_access, height * 0.2
    return beer, beer_position


beer, beer_position = load_random_beer()


running = True
speed = 2
drank = 0
missed = 0
turns = 0

while running:
    turns += 1
    # Game Status

    if (
        10 < (player_position[1] - beer_position[1]) < 30
        and player_position[0] == beer_position[0] - 25
    ):
        drank += 1
        sound = pg.mixer.music.load(os.path.join(
            DIR, "assets/sound", "sensacional.mp3")
            )
        pg.mixer.music.play(0)
        beer, beer_position = load_random_beer()

    if turns == 5000:
        speed += 0.15
        turns = 0
        print("Level Up", speed)

    beer_position[1] += speed

    # Event Capture
    for event in pg.event.get():
        match event.type:
            case keys.QUIT:
                running = False
            case keys.KEYDOWN:
                if event.key in (keys.K_a, keys.K_LEFT):
                    player_position = player_position.move(
                        (-int(width_road / 2), 0)
                    )
                elif event.key in (keys.K_d, keys.K_RIGHT):
                    player_position = player_position.move(
                        (int(width_road / 2), 0)
                    )
                elif event.key in (keys.K_s, keys.K_DOWN):
                    player_position = player_position.move(
                        (-0, int(height / 4))
                    )
                elif event.key in (keys.K_w, keys.K_UP):
                    player_position = player_position.move(
                        (0, -int(height / 4))
                    )



    # road
    pg.draw.rect(
        screen,
        GRAY,
        (width / 2 - width_road / 2, 0, width_road, height)
    )
    # separator
    pg.draw.rect(
        screen,
        YELLOW,
        (width / 2 - separator_width / 2, 0, separator_width, height)
    )
    # border
    pg.draw.rect(
        screen,
        WHITE,
        (
            width / 2 - width_road / 2 + separator_width * 2,
            0,
            separator_width,
            height
        )
    )
    pg.draw.rect(
        screen,
        WHITE,
        (
            width / 2 + width_road / 2 - separator_width * 2,
            0,
            separator_width,
            height
        )
    )


    # Title and Score
    title = letter.render(
        f"  Catch a beer!                    Drank: {drank}     Missed: {missed}", True, WHITE,
    )
    screen.blit(title, (width / 5, 0))

    # Player and Beers
    screen.blit(player, player_position)
    screen.blit(beer, beer_position)

    # Screen Update
    pg.display.update()


    # Reload Beer / Nex Round
    if beer_position[1] > width:
        missed += 1
        beer, beer_position = load_random_beer()

    if missed > 100:
        sound = pg.mixer.music.load(os.path.join(
            DIR, "assets/sound", "zika.mp3")
            )
        pg.mixer.music.play(0)
        msg = higher_letter.render("GAME OVER", True, YELLOW, BLACK)
        screen.blit(msg, (width / 4, 100))
        pg.display.update()
        wait_key = True
        while wait_key:
            for event in pg.event.get():
                if event.type == keys.KEYDOWN:
                    wait_key = False
        break





pg.quit()
