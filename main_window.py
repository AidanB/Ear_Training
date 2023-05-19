import pygame
import sys
from midi_fxns import *
import random

# Initialize Pygame
pygame.init()

# Set the window dimensions
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

# Create the Pygame window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
screen.fill((255,255,255))

font = pygame.font.SysFont("Arial", 24)

maj_min = {"up":"Major", "down":"Minor", "left":"Perfect", "right":"Perfect", "space":"Perfect"}
notes = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8
}
interval_names = {
    1: "Unison",
    2: "Second",
    3: "Third",
    4: "Fourth",
    5: "Fifth",
    6: "Sixth",
    7: "Seventh",
    8: "Octave"
}
def calc_interval(note1,note2,in_qual,in_name):
    interval = abs(note2 - note1)
    in_name = interval_names[in_name]

    interval_quality_map = {
        0: "Perfect",
        1: "Minor",
        2: "Major",
        3: "Minor",
        4: "Major",
        5: "Perfect",
        6: "Tritone",
        7: "Perfect",
        8: "Minor",
        9: "Major",
        10: "Minor",
        11: "Major",
        12: "Perfect"
    }

    interval_name_map = {
        0: "Unison",
        1: "Second",
        2: "Second",
        3: "Third",
        4: "Third",
        5: "Fourth",
        6: "Tritone",
        7: "Fifth",
        8: "Sixth",
        9: "Sixth",
        10: "Seventh",
        11: "Seventh",
        12: "Octave"
    }

    true_qual = interval_quality_map[interval]
    true_name = interval_name_map[interval]

    if interval_quality_map[interval] == "Tritone":
        if in_qual == "Major" and in_name == "Fourth":
            return (True,"Tritone")
        if in_qual == "Minor" and in_name == "Fifth":
            return (True,"Tritone")
        else:
            return (False,"Tritone")
    else:
        if in_qual == true_qual and in_name == true_name:
            return (True,f"{true_qual} {true_name}")
        else:
            return (False,f"{true_qual} {true_name}")



def play_notes_game():
    # Set the range of playable notes
    LOW_NOTE = 48  # C3
    HIGH_NOTE = 96  # C7

    # Generate two random notes within an octave of each other
    note1 = 48#random.randint(LOW_NOTE, HIGH_NOTE)
    note2 = 54#note1 + random.randint(-12,12)

    # Play the two notes back to back
    play_notes([note1])
    play_notes([note2])

    # Wait for the player to press the keys
    maj_min_pressed = None
    num_pressed = None
    while not (maj_min_pressed and num_pressed):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)
                if key in maj_min:
                    maj_min_pressed = maj_min[key]
                    print(maj_min_pressed)
                elif key in notes:
                    num_pressed = notes[key]
                    print(num_pressed)

            # Check for quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    result = calc_interval(note1,note2,maj_min_pressed,num_pressed)
    if result[0] == True:
        play_notes([note1,note2])
        text_surface = font.render(result[1], True, (0, 0, 0))
        screen.blit(text_surface, (100, 100))
        pygame.display.update()
    else:
        bad_int = f"{maj_min_pressed} {interval_names[num_pressed]}"
        #bad_int = '\u0336' + '\u0336'.join(bad_int)
        #font.set_strikethrough(True)
        text_surface1 = font.render(bad_int, True, (255, 0, 0))
        #font.set_strikethrough(False)
        text_surface2 = font.render(result[1], True, (0, 0, 0))
        screen.blit(text_surface1, (100, 100))
        screen.blit(text_surface2, (100, 200))







# Run the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill((255, 255, 255))

    play_notes_game()

    # Update the screen
    pygame.display.flip()