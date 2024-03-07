import random
from art import logo, vs, clear
from game_data import data
import os

# Print art logo


# get the length of the game data
size_of_game_data = len(data)


def get_random_figure():
    """Get data from random account"""
    return random.choice(data)


def format_figure_personal_info(personal_info):
    name = personal_info["name"]
    description = personal_info["description"]
    country = personal_info["country"]
    return f"{name}, a {description}, from {country}."


def check_player_answer(player_guess, figure_a_followers, figure_b_followers):
    if figure_a_followers > figure_b_followers:
        return player_guess == "A"
    else:
        return player_guess == "B"


def play_game():
    print(logo)
    current_score = 0
    game_should_continue = True
    figure_a_info = get_random_figure()
    figure_b_info = get_random_figure()
    while game_should_continue:
        figure_a_info = figure_b_info
        figure_b_info = get_random_figure()
        while figure_a_info == figure_b_info:
            figure_b_info = get_random_figure()
        print(f"Compare A: {format_figure_personal_info(figure_a_info)}.")
        print(vs)
        print(f"Against B: {format_figure_personal_info(figure_b_info)}")
        player_guess = input("Who has more followers? Type 'A' or 'B'")
        figure_a_follower_count = figure_a_info["follower_count"]
        figure_b_follower_count = figure_b_info["follower_count"]
        is_true = check_player_answer(player_guess, figure_a_follower_count, figure_b_follower_count)
        clear()
        print(logo)
        if is_true:
            current_score += 1
            print(f"You're right! Current score: {current_score}")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {current_score}")


play_game()

# # based on the len of the game data generate random number range
# def generate_fig_a():
#     RAND_NUMBER_FOR_A = randint(1, size_of_game_data)
#     return data[RAND_NUMBER_FOR_A]
#
#
# def display_figur_a():
#     print(logo)
#     new_figure = generate_fig_a()
#     arr = []
#     A_FOLLOWER = 0
#     for i in new_figure:
#         if i == "follower_count":
#             A_FOLLOWER = new_figure[i]
#         else:
#             arr.append(new_figure[i])
#     print(f"Compare A: {arr[0]}, a {arr[1]}, from {arr[2]}.")
#     print(vs)
#     new_figure1 = generate_fig_a()
#     arr_b = []
#     B_FOLLOWER = 0
#     for i in new_figure1:
#         if i == "follower_count":
#             B_FOLLOWER = new_figure1[i]
#         else:
#             arr_b.append(new_figure1[i])
#
#     print(f"Against B: {arr_b[0]}, a {arr_b[1]}, from {arr_b[2]}.")
#     choice = False
#     score = 0
#     while not choice:
#         option = input("Who has more follower? Type 'A' or 'B':")
#         if option == "A":
#
#             if A_FOLLOWER > B_FOLLOWER:
#                 arr = arr
#                 score += 1
#                 print(f"Your're right! Current score {score}")
#             else:
#                 print(f"Sorry, that's wrong. Final score: {score}")
#                 choice = True
#         if option == "B":
#
#             if A_FOLLOWER < B_FOLLOWER:
#                 arr = arr_b
#                 score += 1
#                 print(f"Your're right! Current score {score}")
#             else:
#                 print(f"Sorry, that's wrong. Final score: {score}")
#                 choice = True
#
#
# display_figur_a()
# print(A_FOLLOWER_COUNT)
# def generate_fig_b():
#     RAND_NUMBER_FOR_B = randint(1, size_of_game_data)
#     return data[RAND_NUMBER_FOR_B]
#
#
#
# B_FOLLOWER_COUNT = generate_fig_b()["follower_count"]
# def display_figur_b():
#     new_figure = generate_fig_b()
#     arr = []
#     for i in new_figure:
#         if i == "follower_count":
#             B_FOLLOWER_COUNT = (new_figure[i])
#         else:
#             arr.append(new_figure[i])
#     print(f"Against B: {arr[0]}, a {arr[1]}, from {arr[2]}.")
# display_figur_b()
# def compare_a_with_b():
#     print(f"Who has more followers? Type 'A' or 'B':")
#     if A_FOLLOWER_COUNT > B_FOLLOWER_COUNT
#


# randomly generate the A figure

# randomly generate B figure

# compare A with B

# calculate the score
