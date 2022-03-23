"""
Bonus3 - Task 7
Game 6 - [100 Game]
Name: Abd-Elrahman Yasser Ali Awad
ID: 20210564 """

# libraries used
import pygame
import time

# initialize
pygame.init()
running = True
last_player = 2
score_sum = 0

# Screen resolution
screen = pygame.display.set_mode((1280, 720))

# Game title.
pygame.display.set_caption("100 Game")

# Game icon.
icon = pygame.image.load("100.png")
pygame.display.set_icon(icon)
# ----------------------------------------------------------------------------------------------------------------------


# The 100s water mark above the background.
def water_mark():
    """The 100s water mark above the background."""
    mark = pygame.image.load('WaterMark.png')
    mark_X = 0
    mark_Y = 0
    screen.blit(mark, (mark_X, mark_Y))
# ----------------------------------------------------------------------------------------------------------------------


# Signature.
def developer_signature():
    """Signature."""
    signature = pygame.image.load('Author.png')
    signature_X = 4
    signature_Y = 704

    screen.blit(signature, (signature_X, signature_Y))
# ----------------------------------------------------------------------------------------------------------------------


# Black shade under the area of selection numbers.
def black_divider():
    """Black shade under the area of selection numbers."""
    divider = pygame.image.load('Divider.png')
    divider_X = 0
    divider_Y = 435
    screen.blit(divider, (divider_X, divider_Y))
# ----------------------------------------------------------------------------------------------------------------------


# Prints the score and the number of the current player.
def ui_printer():
    """Prints the score and the number of the current player."""
    global last_player

    if last_player == 2:
        print_player_one()
        player_one_score()

    elif last_player == 1:
        print_player_two()
        player_two_score()
# ----------------------------------------------------------------------------------------------------------------------


# Identify which number was clicked on and adds it's value to the main sum.
def click_on_number():
    """Identify which number was clicked on and adds it's value to the main sum."""
    global score_sum, last_player

    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:

            # Number 1
            for x in range(0, 129):
                for y in range(436, 565):
                    if event.pos == (x, y):
                        score_sum += 1

                        turns_switcher()

                        time.sleep(0.2)
                        break

            # Number 2
            for x in range(128, 257):
                for y in range(564, 693):
                    if event.pos == (x, y):
                        score_sum += 2

                        turns_switcher()

                        time.sleep(0.2)
                        break

            # Number 3
            for x in range(256, 385):
                for y in range(436, 565):
                    if event.pos == (x, y):
                        score_sum += 3

                        turns_switcher()

                        time.sleep(0.2)
                        break

            # Number 4
            for x in range(384, 513):
                for y in range(564, 693):
                    if event.pos == (x, y):
                        score_sum += 4

                        turns_switcher()

                        time.sleep(0.2)
                        break

            # Number 5
            for x in range(512, 641):
                for y in range(436, 564):
                    if event.pos == (x, y):
                        score_sum += 5

                        turns_switcher()

                        time.sleep(0.2)
                        break

            # Number 6
            for x in range(640, 769):
                for y in range(564, 693):
                    if event.pos == (x, y):
                        score_sum += 6

                        turns_switcher()

                        time.sleep(0.2)
                        break

            # Number 7
            for x in range(768, 897):
                for y in range(436, 564):
                    if event.pos == (x, y):
                        score_sum += 7

                        turns_switcher()

                        time.sleep(0.2)
                        break

            # Number 8
            for x in range(896, 1025):
                for y in range(564, 693):
                    if event.pos == (x, y):
                        score_sum += 8

                        turns_switcher()

                        time.sleep(0.2)
                        break

            # Number 9
            for x in range(1024, 1153):
                for y in range(436, 564):
                    if event.pos == (x, y):
                        score_sum += 9

                        turns_switcher()

                        time.sleep(0.2)
                        break

            # Number 10
            for x in range(1152, 1281):
                for y in range(564, 693):
                    if event.pos == (x, y):
                        score_sum += 10

                        turns_switcher()

                        time.sleep(0.2)
                        break
# ----------------------------------------------------------------------------------------------------------------------


# Prints all the numbers to select from.
def choose_numbers():
    """Prints all the numbers to select from."""
    one = pygame.image.load('1C.png')
    one_X = 0
    one_Y = 436
    screen.blit(one, (one_X, one_Y))

    two = pygame.image.load('2C.png')
    two_X = 128
    two_Y = 564
    screen.blit(two, (two_X, two_Y))

    three = pygame.image.load('3C.png')
    three_X = 256
    three_Y = 436
    screen.blit(three, (three_X, three_Y))

    four = pygame.image.load('4C.png')
    four_X = 384
    four_Y = 564
    screen.blit(four, (four_X, four_Y))

    five = pygame.image.load('5C.png')
    five_X = 512
    five_Y = 436
    screen.blit(five, (five_X, five_Y))

    six = pygame.image.load('6C.png')
    six_X = 640
    six_Y = 564
    screen.blit(six, (six_X, six_Y))

    seven = pygame.image.load('7C.png')
    seven_X = 768
    seven_Y = 436
    screen.blit(seven, (seven_X, seven_Y))

    eight = pygame.image.load('8C.png')
    eight_X = 896
    eight_Y = 564
    screen.blit(eight, (eight_X, eight_Y))

    nine = pygame.image.load('9C.png')
    nine_X = 1024
    nine_Y = 436
    screen.blit(nine, (nine_X, nine_Y))

    ten = pygame.image.load('10C.png')
    ten_X = 1152
    ten_Y = 564
    screen.blit(ten, (ten_X, ten_Y))
# ----------------------------------------------------------------------------------------------------------------------


# Coordinates of player one user interface and included images.
def print_player_one():
    """Coordinates of player one user interface and included images."""

    # Frame
    frame1 = pygame.image.load('frameBlue.png')
    frame1_X = 336
    frame1_Y = -95
    screen.blit(frame1, (frame1_X, frame1_Y))

    # word PLAYER in blue color.
    player_P = pygame.image.load('P.png')
    P_X = 380
    P_Y = 80

    player_L = pygame.image.load('L.png')
    L_X = 430
    L_Y = 80

    player_A = pygame.image.load('A.png')
    A_X = 480
    A_Y = 80

    player_Y = pygame.image.load('Y.png')
    Y_X = 530
    Y_Y = 80

    player_E = pygame.image.load('E.png')
    E_X = 580
    E_Y = 80

    player_R = pygame.image.load('R.png')
    R_X = 630
    R_Y = 80

    screen.blit(player_P, (P_X, P_Y))
    screen.blit(player_L, (L_X, L_Y))
    screen.blit(player_A, (A_X, A_Y))
    screen.blit(player_Y, (Y_X, Y_Y))
    screen.blit(player_E, (E_X, E_Y))
    screen.blit(player_R, (R_X, R_Y))

    one_O = pygame.image.load('O.png')
    O_X = 710
    O_Y = 80

    one_N = pygame.image.load('N.png')
    N_X = 760
    N_Y = 80

    one_E = pygame.image.load('E.png')
    E_X = 810
    E_Y = 80

    screen.blit(one_O, (O_X, O_Y))
    screen.blit(one_N, (N_X, N_Y))
    screen.blit(one_E, (E_X, E_Y))
# ----------------------------------------------------------------------------------------------------------------------


# Coordinates of player two user interface and included images.
def print_player_two():
    """Coordinates of player two user interface and included images."""

    # Frame
    frame2 = pygame.image.load('frameRed.png')
    frame2_X = 336
    frame2_Y = -95
    screen.blit(frame2, (frame2_X, frame2_Y))

    # word PLAYER in red color.
    player_P = pygame.image.load('P2.png')
    P_X = 380
    P_Y = 80

    player_L = pygame.image.load('L2.png')
    L_X = 430
    L_Y = 80

    player_A = pygame.image.load('A2.png')
    A_X = 480
    A_Y = 80

    player_Y = pygame.image.load('Y2.png')
    Y_X = 530
    Y_Y = 80

    player_E = pygame.image.load('E2.png')
    E_X = 580
    E_Y = 80

    player_R = pygame.image.load('R2.png')
    R_X = 630
    R_Y = 80

    screen.blit(player_P, (P_X, P_Y))
    screen.blit(player_L, (L_X, L_Y))
    screen.blit(player_A, (A_X, A_Y))
    screen.blit(player_Y, (Y_X, Y_Y))
    screen.blit(player_E, (E_X, E_Y))
    screen.blit(player_R, (R_X, R_Y))

    two_T = pygame.image.load('T2.png')
    T_X = 710
    T_Y = 80

    two_W = pygame.image.load('W2.png')
    W_X = 760
    W_Y = 84

    two_O = pygame.image.load('O2.png')
    O_X = 810
    O_Y = 81

    screen.blit(two_T, (T_X, T_Y))
    screen.blit(two_W, (W_X, W_Y))
    screen.blit(two_O, (O_X, O_Y))
# ----------------------------------------------------------------------------------------------------------------------


# Current score in player one turn.
def player_one_score():
    """Current score in player one turn."""
    if 0 <= score_sum < 50:
        if 0 <= score_sum < 10:
            for i in range(0, 10):
                if score_sum == i:
                    score1 = pygame.image.load(f"{i}.png")
                    score1_X = 592
                    score1_Y = 200
                    screen.blit(score1, (score1_X, score1_Y))

        elif 10 <= score_sum < 20:
            for i in range(0, 10):
                if score_sum == (10 + i):
                    score1 = pygame.image.load("1.png")
                    score1_X = 570
                    score1_Y = 200

                    score11 = pygame.image.load(f"{i}.png")
                    score11_X = 640
                    score11_Y = 200

                    screen.blit(score1, (score1_X, score1_Y))
                    screen.blit(score11, (score11_X, score11_Y))

        elif 20 <= score_sum < 30:
            for i in range(0, 10):
                if score_sum == (20 + i):
                    score1 = pygame.image.load("2.png")
                    score1_X = 570
                    score1_Y = 200

                    score11 = pygame.image.load(f"{i}.png")
                    score11_X = 640
                    score11_Y = 200

                    screen.blit(score1, (score1_X, score1_Y))
                    screen.blit(score11, (score11_X, score11_Y))

        elif 30 <= score_sum < 40:
            for i in range(0, 10):
                if score_sum == (30 + i):
                    score1 = pygame.image.load("3.png")
                    score1_X = 570
                    score1_Y = 200

                    score11 = pygame.image.load(f"{i}.png")
                    score11_X = 640
                    score11_Y = 200

                    screen.blit(score1, (score1_X, score1_Y))
                    screen.blit(score11, (score11_X, score11_Y))

        elif 40 <= score_sum < 50:
            for i in range(0, 10):
                if score_sum == (40 + i):
                    score1 = pygame.image.load("4.png")
                    score1_X = 570
                    score1_Y = 200

                    score11 = pygame.image.load(f"{i}.png")
                    score11_X = 640
                    score11_Y = 200

                    screen.blit(score1, (score1_X, score1_Y))
                    screen.blit(score11, (score11_X, score11_Y))

    elif 50 <= score_sum < 100:
        if 50 <= score_sum < 60:
            for i in range(0, 10):
                if score_sum == (50 + i):
                    score1 = pygame.image.load("5.png")
                    score1_X = 570
                    score1_Y = 200

                    score11 = pygame.image.load(f"{i}.png")
                    score11_X = 640
                    score11_Y = 200

                    screen.blit(score1, (score1_X, score1_Y))
                    screen.blit(score11, (score11_X, score11_Y))

        elif 60 <= score_sum < 70:
            for i in range(0, 10):
                if score_sum == (60 + i):
                    score1 = pygame.image.load("6.png")
                    score1_X = 570
                    score1_Y = 200

                    score11 = pygame.image.load(f"{i}.png")
                    score11_X = 640
                    score11_Y = 200

                    screen.blit(score1, (score1_X, score1_Y))
                    screen.blit(score11, (score11_X, score11_Y))

        elif 70 <= score_sum < 80:
            for i in range(0, 10):
                if score_sum == (70 + i):
                    score1 = pygame.image.load("7.png")
                    score1_X = 570
                    score1_Y = 200

                    score11 = pygame.image.load(f"{i}.png")
                    score11_X = 640
                    score11_Y = 200

                    screen.blit(score1, (score1_X, score1_Y))
                    screen.blit(score11, (score11_X, score11_Y))

        elif 80 <= score_sum < 90:
            for i in range(0, 10):
                if score_sum == (80 + i):
                    score1 = pygame.image.load("8.png")
                    score1_X = 570
                    score1_Y = 200

                    score11 = pygame.image.load(f"{i}.png")
                    score11_X = 640
                    score11_Y = 200

                    screen.blit(score1, (score1_X, score1_Y))
                    screen.blit(score11, (score11_X, score11_Y))

        elif 90 <= score_sum < 100:
            for i in range(0, 10):
                if score_sum == (90 + i):
                    score1 = pygame.image.load("9.png")
                    score1_X = 570
                    score1_Y = 200

                    score11 = pygame.image.load(f"{i}.png")
                    score11_X = 640
                    score11_Y = 200

                    screen.blit(score1, (score1_X, score1_Y))
                    screen.blit(score11, (score11_X, score11_Y))
    else:
        if score_sum >= 100:
            score1 = pygame.image.load('1.png')
            score1_X = 522
            score1_Y = 200

            score11 = pygame.image.load('0.png')
            score11_X = 592
            score11_Y = 200

            score111 = pygame.image.load('0.png')
            score111_X = 662
            score111_Y = 200

            screen.blit(score1, (score1_X, score1_Y))
            screen.blit(score11, (score11_X, score11_Y))
            screen.blit(score111, (score111_X, score111_Y))
# ----------------------------------------------------------------------------------------------------------------------


# Current score in player one turn.
def player_two_score():
    """Current score in player one turn."""
    if 0 <= score_sum < 50:
        if 0 <= score_sum < 10:
            for i in range(0, 10):
                if score_sum == i:
                    score1 = pygame.image.load(f"{i}R.png")
                    score1_X = 592
                    score1_Y = 200
                    screen.blit(score1, (score1_X, score1_Y))

        elif 10 <= score_sum < 20:
            for i in range(0, 10):
                if score_sum == (10 + i):
                    score1 = pygame.image.load("1R.png")
                    score1_X = 570
                    score1_Y = 200

                    score11 = pygame.image.load(f"{i}R.png")
                    score11_X = 640
                    score11_Y = 200

                    screen.blit(score1, (score1_X, score1_Y))
                    screen.blit(score11, (score11_X, score11_Y))

        elif 20 <= score_sum < 30:
            for i in range(0, 10):
                if score_sum == (20 + i):
                    score1 = pygame.image.load("2R.png")
                    score1_X = 570
                    score1_Y = 200

                    score11 = pygame.image.load(f"{i}R.png")
                    score11_X = 640
                    score11_Y = 200

                    screen.blit(score1, (score1_X, score1_Y))
                    screen.blit(score11, (score11_X, score11_Y))

        elif 30 <= score_sum < 40:
            for i in range(0, 10):
                if score_sum == (30 + i):
                    score1 = pygame.image.load("3R.png")
                    score1_X = 570
                    score1_Y = 200

                    score11 = pygame.image.load(f"{i}R.png")
                    score11_X = 640
                    score11_Y = 200

                    screen.blit(score1, (score1_X, score1_Y))
                    screen.blit(score11, (score11_X, score11_Y))

        elif 40 <= score_sum < 50:
            for i in range(0, 10):
                if score_sum == (40 + i):
                    score1 = pygame.image.load("4R.png")
                    score1_X = 570
                    score1_Y = 200

                    score11 = pygame.image.load(f"{i}R.png")
                    score11_X = 640
                    score11_Y = 200

                    screen.blit(score1, (score1_X, score1_Y))
                    screen.blit(score11, (score11_X, score11_Y))

    elif 50 <= score_sum < 100:
        if 50 <= score_sum < 60:
            for i in range(0, 10):
                if score_sum == (50 + i):
                    score1 = pygame.image.load("5R.png")
                    score1_X = 570
                    score1_Y = 200

                    score11 = pygame.image.load(f"{i}R.png")
                    score11_X = 640
                    score11_Y = 200

                    screen.blit(score1, (score1_X, score1_Y))
                    screen.blit(score11, (score11_X, score11_Y))

        elif 60 <= score_sum < 70:
            for i in range(0, 10):
                if score_sum == (60 + i):
                    score1 = pygame.image.load("6R.png")
                    score1_X = 570
                    score1_Y = 200

                    score11 = pygame.image.load(f"{i}R.png")
                    score11_X = 640
                    score11_Y = 200

                    screen.blit(score1, (score1_X, score1_Y))
                    screen.blit(score11, (score11_X, score11_Y))

        elif 70 <= score_sum < 80:
            for i in range(0, 10):
                if score_sum == (70 + i):
                    score1 = pygame.image.load("7R.png")
                    score1_X = 570
                    score1_Y = 200

                    score11 = pygame.image.load(f"{i}R.png")
                    score11_X = 640
                    score11_Y = 200

                    screen.blit(score1, (score1_X, score1_Y))
                    screen.blit(score11, (score11_X, score11_Y))

        elif 80 <= score_sum < 90:
            for i in range(0, 10):
                if score_sum == (80 + i):
                    score1 = pygame.image.load("8R.png")
                    score1_X = 570
                    score1_Y = 200

                    score11 = pygame.image.load(f"{i}R.png")
                    score11_X = 640
                    score11_Y = 200

                    screen.blit(score1, (score1_X, score1_Y))
                    screen.blit(score11, (score11_X, score11_Y))

        elif 90 <= score_sum < 100:
            for i in range(0, 10):
                if score_sum == (90 + i):
                    score1 = pygame.image.load("9R.png")
                    score1_X = 570
                    score1_Y = 200

                    score11 = pygame.image.load(f"{i}R.png")
                    score11_X = 640
                    score11_Y = 200

                    screen.blit(score1, (score1_X, score1_Y))
                    screen.blit(score11, (score11_X, score11_Y))
    else:
        if score_sum >= 100:
            score1 = pygame.image.load('1R.png')
            score1_X = 522
            score1_Y = 200

            score11 = pygame.image.load('0R.png')
            score11_X = 592
            score11_Y = 200

            score111 = pygame.image.load('0R.png')
            score111_X = 662
            score111_Y = 200

            screen.blit(score1, (score1_X, score1_Y))
            screen.blit(score11, (score11_X, score11_Y))
            screen.blit(score111, (score111_X, score111_Y))
# ----------------------------------------------------------------------------------------------------------------------


# Switches turns upon selecting a number.
def turns_switcher():
    """Switches turns upon selecting a number."""
    global score_sum, last_player

    if score_sum < 100:
        if last_player == 2:
            last_player = 1

        elif last_player == 1:
            last_player = 2
# ----------------------------------------------------------------------------------------------------------------------


# Congratulate the winner.
def congratulations():
    """Congratulate the winner."""
    global running, last_player

    if score_sum >= 100:
        if last_player == 2:
            congrats = pygame.image.load('congratsP1.png')
            congrats_X = 0
            congrats_Y = 0
            screen.blit(congrats, (congrats_X, congrats_Y))
            # time.sleep(10)
            # running = False

        elif last_player == 1:
            congrats = pygame.image.load('congratsP2.png')
            congrats_X = 0
            congrats_Y = 0
            screen.blit(congrats, (congrats_X, congrats_Y))
            # time.sleep(10)
            # running = False
# ----------------------------------------------------------------------------------------------------------------------


# Game loop.
while running:
    # background RGB (Red, Green, Blue)
    screen.fill((230, 220, 220))

    # Water Mark
    water_mark()

    # black divider
    black_divider()

    # Signature
    developer_signature()

    ui_printer()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    choose_numbers()

    click_on_number()
    congratulations()

    pygame.display.update()
