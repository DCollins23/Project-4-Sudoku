import pygame
import sys
from buttonclass import *
from scrollclass import *
from Board import *
from sudoku_generator import *

#initializes pygame
pygame.init()

# sets neccessary variables
clock = pygame.time.Clock()
screen_width, screen_height = (700, 700)
screen = pygame.display.set_mode((screen_width, screen_height))
main_font = pygame.font.SysFont("cambria math", 50)
welcome_font = pygame.font.SysFont("cambria math", bold = True, size = 55)
little_button_font = pygame.font.SysFont("cambria math", 25)
framerate = 60
bg_speed = 100

#sets images
background = Scroll(700, "background_sudoku.png")
welcome_banner = pygame.image.load("banner.png").convert_alpha()
welcome_banner = pygame.transform.scale(welcome_banner, (650, 400))

# sets the mouse to visible and gets its position
pygame.mouse.set_visible(True)
main_menu_mouse_pos = pygame.mouse.get_pos()

# sets the caption of the game
pygame.display.set_caption(('Sudoku'))

# methods
def main_menu(): # shows main menu and prompts user to start or exit program

    while True: # while loop
        main_menu_mouse_pos = show_background()
        welcome_text()

        # buttons - sets the buttons
        start_button = Button(image=pygame.image.load("rect.png"), pos=(350, 350), text_input="Start!", font=main_font,
                              base_color="Black", hovering_color="White")
        exit_button = Button(image=pygame.image.load("rect.png"), pos=(350, 450), text_input="Exit", font=main_font,
                             base_color="Black", hovering_color="White")
        # updates the button when they are hovered over
        for button in [start_button, exit_button]:
            button.change_btn_color(main_menu_mouse_pos)
            button.update(screen)
        # user interaction with the buttons
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # exit through the traditional way
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.input_checker(main_menu_mouse_pos): # starts the game and brings the user to the difficulty screen
                    difficulty()
                    break
                if exit_button.input_checker(main_menu_mouse_pos): # exits the program through the exit button
                    pygame.quit()
                    sys.exit()
                    break
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()

def difficulty(): # difficulty screen

    while True:
        main_menu_mouse_pos = show_background()
        welcome_text()
        gamemode_txt = main_font.render("Select Game Mode:", True, 'black')# sets the gamemode text
        gamemode_txt_rect = gamemode_txt.get_rect(center=(350, 350))# sets the gamemode text into a rectangle
        screen.blit(gamemode_txt, gamemode_txt_rect) # shows gamemode text on screen

        # difficulty buttons - sets the buttons
        easy_button = Button(image=pygame.image.load("rect.png"), pos=(350, 450), text_input="Easy", font=main_font,
                              base_color="Black", hovering_color="White")
        medium_button = Button(image=pygame.image.load("rect.png"), pos=(350, 550), text_input="Medium", font=main_font,
                             base_color="Black", hovering_color="White")
        hard_button = Button(image=pygame.image.load("rect.png"), pos=(350, 650), text_input="Hard", font=main_font,
                               base_color="Black", hovering_color="White")
        # updates the button when they are hovered over
        for button in [easy_button, medium_button, hard_button]:
            button.change_btn_color(main_menu_mouse_pos)
            button.update(screen)
        # user interaction with the buttons
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.input_checker(main_menu_mouse_pos): # if the user clicks easy gamemode
                    game("easy")
                    break
                if medium_button.input_checker(main_menu_mouse_pos): # if the user clicks medium gamemode
                    game("medium")
                    break
                if hard_button.input_checker(main_menu_mouse_pos): # if the user clicks hard gamemode
                    game("hard")
                    break
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
def game(difficulty):
    main_menu_mouse_pos = pygame.mouse.get_pos() # position of mouse
    screen_color = (173, 216, 230)
    screen.fill(screen_color)
    pygame.display.flip()
    if (difficulty == "easy"):
        initiate_board = generate_sudoku(9, 30)
    elif(difficulty == "medium"):
        initiate_board = generate_sudoku(9, 40)
    elif(difficulty == "hard"):
        initiate_board = generate_sudoku(9, 50)
    board = Board(screen_width, screen_height - 100, screen, initiate_board[0])
    board.set_initial_board()
    board.draw()
    pygame.display.update()
    value = 0
    while(True):
        main_menu_mouse_pos = pygame.mouse.get_pos()
        #buttons - sets buttons
        reset_button = Button(image=pygame.image.load("rect.png"), pos=(200, 650), text_input="Reset", font=little_button_font, base_color="Black", hovering_color="White", scale=0.5)
        restart_button = Button(image=pygame.image.load("rect.png"), pos=(350, 650), text_input="Restart?", font=little_button_font, base_color="Black", hovering_color="White", scale=0.5)
        exit_button = Button(image=pygame.image.load("rect.png"), pos=(500, 650), text_input="Exit?", font=little_button_font, base_color="Black", hovering_color="White", scale=0.5)
        #updates the buttons when they are hovered over
        for button in [reset_button, restart_button, exit_button]:
            button.change_btn_color(main_menu_mouse_pos)
            button.update(screen)
            # user interaction with the buttons
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                good_click = board.click(main_menu_mouse_pos[0],main_menu_mouse_pos[1])
                if (good_click != None):
                    board.draw()
                    valid_cell = board.select(good_click[0],good_click[1])
                else:
                    pass
                if reset_button.input_checker(main_menu_mouse_pos):
                    board.reset_to_original()
                    screen.fill(screen_color)
                    board.draw()
                if restart_button.input_checker(main_menu_mouse_pos):  # if the user picks restart button goes to main menu
                    main_menu()
                    print("clicked")
                    break
                if exit_button.input_checker(main_menu_mouse_pos):  # if the user picks exit button exits program
                    print("clicked")
                    pygame.quit()
                    sys.exit()
                    break
            if event.type == pygame.KEYDOWN:
                if (good_click!=None and (good_click[0] >= 0 and good_click[0] < 10) and (good_click[1] > 0 and good_click[1] < 10)):
                    if (good_click[0] < 9):
                        if event.key == pygame.K_DOWN:
                            good_click = (good_click[0]+1,good_click[1])
                            board.draw()
                            valid_cell = board.select(good_click[0],good_click[1])
                    if (good_click[0] > 1):
                        if event.key == pygame.K_UP:
                            good_click = (good_click[0]-1,good_click[1])
                            board.draw()
                            valid_cell = board.select(good_click[0],good_click[1])
                    if (good_click[1] < 9):
                        if event.key == pygame.K_RIGHT:
                            good_click = (good_click[0],good_click[1]+1)
                            board.draw()
                            valid_cell = board.select(good_click[0],good_click[1])
                    if (good_click[1] > 1):
                        if event.key == pygame.K_LEFT:
                            good_click = (good_click[0],good_click[1]-1)
                            board.draw()
                            valid_cell = board.select(good_click[0],good_click[1])
                if(good_click!= None and valid_cell == 0):
                    event_key_list = [pygame.K_1, pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5,pygame.K_6,pygame.K_7,pygame.K_8,pygame.K_9]
                    for i in range(0,9):
                        if event.key == event_key_list[i]:
                            value = i+1
                            screen.fill(screen_color)
                            board.sketch(value)
                            board.draw()
                            board.select(good_click[0], good_click[1])
                    if event.key == pygame.K_BACKSPACE:
                        board.clear()
                        screen.fill(screen_color)
                        board.draw()
                        board.select(good_click[0], good_click[1])
                    if value == None:
                        warning_font = pygame.font.SysFont("cambria math", bold=True, size=20)
                        warning_txt = warning_font.render("INCLUDE VALUE BEFORE YOU PRESS ENTER!", True, 'black')  # sets the welcome text
                        warning_text_rect = warning_txt.get_rect(center=(350,625))
                        screen.blit(warning_txt, warning_text_rect)  # shows welcome text on screen
                    elif value > 0:
                        if event.key == pygame.K_RETURN:
                            screen.fill(screen_color)
                            value = board.selected_cell.get_sketched_value()
                            board.place_number(value)
                            board.draw()
                            board.select(good_click[0], good_click[1])
                            if (board.is_full()):
                                print("full")
                                if(board.check_board(initiate_board[1])):
                                    game_won()
                                else:
                                    game_over()
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()

def game_over():
    while(True):
        main_menu_mouse_pos = show_background()
        gameover_txt = main_font.render("Game Over :(", True, 'black') # sets gameover text
        show_result(main_menu_mouse_pos,gameover_txt)


def game_won():
    while(True):
        main_menu_mouse_pos = show_background()
        gameover_txt = main_font.render("Game Won!", True, 'black') # sets gamewon text
        show_result(main_menu_mouse_pos,gameover_txt)
def show_background():
    pygame.mouse.set_visible(True)  # sets the mouse to visible
    time = clock.tick(framerate) / 1000.0  # for scrolling background
    background.update_coords(bg_speed, time)  # updates coords for scrolling background
    background.show(screen)  # shows background
    return pygame.mouse.get_pos()  # gets mouse position
def show_result(main_menu_mouse_pos,gameover_txt):
    gameover_txt_rect = gameover_txt.get_rect(center=(350, 150))
    screen.blit(gameover_txt, gameover_txt_rect)  # sets gamewon text into a rectangle
    # buttons - sets the buttons
    restart_button = Button(image=pygame.image.load("rect.png"), pos=(350, 450), text_input="Restart?", font=main_font,
                            base_color="Black", hovering_color="White")
    exit_button = Button(image=pygame.image.load("rect.png"), pos=(350, 550), text_input="Exit?", font=main_font,
                         base_color="Black", hovering_color="White")
    # updates the buttons when they are hovered over
    for button in [restart_button, exit_button]:
        button.change_btn_color(main_menu_mouse_pos)
        button.update(screen)
    # user interaction with the buttons
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if restart_button.input_checker(main_menu_mouse_pos):  # if the user picks restart button goes to main menu
                main_menu()
                break
            if exit_button.input_checker(main_menu_mouse_pos):  # if the user picks exit button exits program
                pygame.quit()
                sys.exit()
                break
                # quits the program the traditional way
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
def welcome_text():
    welcome_txt = welcome_font.render("Welcome to Sudoku!", True, 'black')  # sets the welcome text
    welcome_txt_rect = welcome_txt.get_rect(center=(350, 200))  # sets the welcome text into a rectangle
    welcome_banner_rect = welcome_banner.get_rect(center=(350, 200))  # sets the banner into a rectangle
    screen.blit(welcome_banner, welcome_banner_rect)  # shows banner on the screen
    screen.blit(welcome_txt, welcome_txt_rect)  # shows welcome text on screen
# main driver
def main():
    running = True
    while running:
        main_menu()

        for event in pygame.event.get(): # quits the program the traditional way
            if event.type == pygame.QUIT:
                sys.exit()
                running = False

if __name__ == "__main__":
    main()
