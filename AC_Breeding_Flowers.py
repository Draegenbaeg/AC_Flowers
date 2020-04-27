# This is a flower breeding simulator for the game Animal Crossing: New Horizons
# Here is an image link to access a visual key: https://i.redd.it/qhmplvm1tkq41.png

# A class to emulate a flower. Flower(breed, color, is_perfect)
from Flower import Flower
# A dictionary with flower breeds as the key and the possible colors for each flower as the values
breed_colors = {
    'lily':  ['red', 'yellow', 'orange', 'white', 'pink', 'black'],
    'rose': ['red', 'yellow', 'orange', 'white', 'pink', 'black', 'blue', 'gold', 'purple'],
    'cosmo': ['red', 'yellow', 'orange', 'white', 'pink', 'black'],
    'hyacinth': ['red', 'yellow', 'orange', 'white', 'pink', 'blue', 'purple'],
    'mum': ['red', 'yellow', 'white', 'pink', 'purple'],
    'tulip': ['red', 'yellow', 'orange', 'white', 'pink', 'black', 'purple'],
    'windflower': ['red', 'blue', 'white', 'pink', 'purple'],
    'pansy': ['red', 'yellow', 'orange', 'white', 'blue', 'purple']
 }
# A dictionary with flower breeds as the key and nested color combination as the values
# Each nested key is a color combination and the nested values are what color that combination makes
flower_combinations = {
    'lily': {'red_yellow': 'orange', 'yellow_red': 'orange', 'red_white': 'pink', 'white_red': 'pink', 'red_red':
             'black'},
    'rose': {'red_white': 'pink', 'white_red': 'pink', 'red_yellow': 'orange', 'yellow_red': 'orange', 'red_red':
             'black',
             'white_white': 'purple', 'white_orange': 'perfect red', 'orange_white': 'perfect red',
             'perfect_red_perfect_red': 'blue', 'black_can': 'gold', 'can_black': "gold"},
    'cosmo': {'red_yellow': 'orange', 'yellow_red': 'orange', 'red_white': 'pink', 'white_red': 'pink', 'orange_orange':
              'black'},
    'hyacinth': {'red_yellow': 'orange', 'yellow_red': 'orange', 'red_white': 'pink', 'white_white': 'blue',
                 'orange_orange': 'purple'},
    'mum': {'red_white': 'pink', 'white_red': 'pink', 'white_white': 'purple', 'purple_purple': 'yellow'},
    'tulip': {'red_yellow': 'orange', 'yellow_red': 'orange', 'red_white': 'pink', 'red_red': 'black', 'orange_orange':
              'purple'},
    'windflower': {'red_white': 'pink', 'white_red': 'pink', 'white_white': 'blue', 'blue_blue': 'purple'},
    'pansy': {'red_yellow': 'orange', 'yellow_red': 'orange', 'white_white': 'blue', 'red_blue': 'perfect red',
              'blue_red': 'perfect red', 'blue_orange': 'perfect orange', 'orange_blue': 'perfect orange',
              'perfect_red_perfect_red': 'purple', 'perfect_orange_perfect_orange': 'purple'},
}
# A dictionary for only perfect flowers. Flower breed is the key and perfect flower color combinations are the values
# The nested key are perfect flower color combinations and the nested values are the color those colors create
perfect_flowers = {
    'rose': {"red_red": 'blue'},
    'pansy': {'red_red': 'purple', 'orange_orange': 'purple', 'perfect orange_perfect red': None,
              'perfect red_perfect orange': None}
}


# A function to create a flower within the Flower Class
def create_flower():
    # Asks for user input on all attributed of the Flower Class
    user_breed = input(f"What is the flower's breed?: ({', '.join(breed_colors.keys())}): ")
    while user_breed.lower() not in breed_colors:
        user_breed = input(f"Please input a valid response: ({', '.join(breed_colors.keys())}): ")
    user_color = input(f"What is the flower's color?: ({', '.join(breed_colors.get(user_breed.lower()))}): ")
    while user_color.lower() not in breed_colors[user_breed.lower()]:
        user_color = input(f"Please input a valid response ({', '.join(breed_colors.get(user_breed.lower()))}): ")
    user_is_perfect = 0
    # Looks for special cases involving a perfect flower
    if user_breed.lower() in ["rose"] and user_color.lower() in ["red"] \
            or user_breed.lower() in ["pansy"] and user_color.lower() in ["red", "orange"]:
        user_is_perfect = input("Is the flower perfect? (enter yes or no): ")
        while True:
            if user_is_perfect.lower() == "yes":
                user_is_perfect = True
                break
            elif user_is_perfect.lower() == "no":
                user_is_perfect = False
                break
            else:
                user_is_perfect = input("Please input a valid response: ")
    return Flower(user_breed, user_color, user_is_perfect)


# A function that takes 2 user inputted flowers and breeds them
def flower_breeding():
    input("\nWhat two flowers would you like to breed?"
          "\nPlease enter the breed, color, and if it's perfect (if applicable)."
          "\nHit enter to start:")
    # Asks for a golden watering can special case
    user_can = input("Would you like to use a golden watering can instead of a flower? (yes or no): ")
    while user_can.lower() not in ("yes", "no"):
        user_can = input("Please input a valid response (yes or no) : ")
    if user_can.lower() == "yes":
        flower1 = create_flower()
        if flower1.breed.lower() == "rose" and flower1.color.lower() == "black":
            print(f"\nYou will get a chance at a golden rose.")
            return
        elif flower1.is_perfect is True:
            print(f"\nYou will get a perfect {flower1.color.lower()} {flower1.breed.lower()}.")
            return
        elif flower1.color[0].lower() in 'aeiou':
            print(f"\nYou will get an {flower1.color.lower()} {flower1.breed.lower()}.")
            return
        else:
            print(f"\nYou will get a {flower1.color.lower()} {flower1.breed.lower()}.")
            return
    # All possible non golden watering can cases
    if user_can.lower() == "no":
        flower1 = create_flower()
        print("\nPlease enter your second flower")
        flower2 = create_flower()
        while flower2.breed.lower() not in flower1.breed.lower():
            print('\nFlowers must be the same breed. Please reenter your second flower.')
            flower2 = create_flower()
        final_color = 0
        if flower1.is_perfect is True and flower2.is_perfect is False:
            print(f"\nYour flower has a 50/50 chance of being either perfect"
                  f" {flower1.color.lower()} or {flower2.color.lower()}.")
            return
        if flower1.is_perfect is False and flower2.is_perfect is True:
            print(f"\nYour flower has a 50/50 chance of being either {flower1.color.lower()}"
                  f" or perfect {flower2.color.lower()}.")
            return
        if flower1.is_perfect is True and flower2.is_perfect is True:
            final_color = perfect_flowers[flower1.breed.lower()].get(f"{flower1.color.lower()}_{flower2.color.lower()}")
        else:
            final_color = flower_combinations[flower1.breed.lower()]\
                .get(f"{flower1.color.lower()}_{flower2.color.lower()}")
        if final_color is None and flower1.is_perfect is True and flower2.is_perfect is True:
            print(f"\nYour flower has a 50/50 chance of being either perfect "
                  f"{flower1.color.lower()} or perfect {flower2.color.lower()}.")
            return
        if final_color is None:
            print(f"\nYour flower has a 50/50 chance of being either"
                  f" {flower1.color.lower()} or {flower2.color.lower()}.")
            return
        if final_color[0] in 'aeiou':
            print(f"\nYou will get a chance at an {final_color} {flower1.breed.lower()}.")
        else:
            print(f"\nYou will get a chance at a {final_color} {flower1.breed.lower()}.")
        return


def run_program():
    print("This is an Animal Crossing: New Horizons flower breeding simulator.")
    while True:
        flower_breeding()
        user_exit = input("\nWould you like to enter another breeding? (yes or no): ")
        while user_exit.lower() not in ('yes', 'no'):
            user_exit = input("Please input a valid response (yes or no): ")
        if user_exit.lower() == 'no':
            return


run_program()

