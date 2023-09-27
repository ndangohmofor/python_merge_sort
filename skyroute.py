from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices

landmark_string = ''
for letter, landmark in landmark_choices.items():
    landmark_string += "{0} - {1}".format(letter, landmark)


def greet():
    print("Hi there and welcome to SkyRoute!")
    print("We'll help you find the shortest route between the following Vancouver landmarks:\n" + landmark_string)


def skyroute():
    greet()


def set_start_and_end(start_point, end_point):
    if start_point is not None:
        change_point = input("What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', "
                             "or 'b' for both: ")
        if change_point == 'b':
            start_point = get_start()
            end_point = get_end()

        elif change_point == 'o':
            start_point = get_start()

        elif change_point == 'd':
            end_point = get_end()

        else:
            print("Oops, that isn't 'o', 'd' or 'b' ...")
            set_start_and_end(start_point, end_point)


def get_start():
    start_point_letter = input("Where are you coming from? Type in the corresponding letter: ")
    if start_point_letter in landmark_choices:
        start_point = landmark_choices[start_point_letter]
        return start_point
    else:
        print("Sorry, that's not a landmark we have data on. Let's try this again...")
        get_start()


def get_end():
    pass
