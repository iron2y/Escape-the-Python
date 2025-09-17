"""Main Function
Interaction between model and view
Interaction with user
Processing user inputs (validation of inputs)
toggles model
toolges view"""


import model
import view
from view import display_side_by_side


# TO DOs:
# VIEW integrieren
# Kommentare für functions
# Error-Handling >>> controller
# Testing
# Controller ausbauen


def get_user_guess_of_letter(data): # >>> Controller
    view.show_titles(data)
    view.show_char_list_and_trials(data)
    while True:
        row_titles = view.input_from_user(data, "\nBitte wähle eine Zeile: ")
        print()
        if is_valid_user_input(data, "row_titles", row_titles, "int", [0, len(data["titles"])]):
            break
    view.show_title_with_indices(data)
    while True:
        pos_letter = view.input_from_user(data, "\nBitte wähle den Index für den gewünschten Buchstaben: ")
        print()
        if is_valid_user_input(data, "pos_letter", pos_letter, "int", [0, len(data["titles"][data["row_titles"]])]):
            break
    error_msg = model.process_guess_of_letter(data)
    if error_msg:
        view.show_error_message(error_msg)
    return


def is_valid_user_input(data, data_key, input_to_validate, input_type, input_limits): # >>> Controller
    if input_type == "int":
        if input_to_validate.isdigit():
            if input_limits[0] <= int(input_to_validate) < input_limits[1]:
                data[data_key] = int(input_to_validate)
                return True
            else:
                view.show_error_message("Da sind doch Zahlen vorgegeben, wähle diese doch aus.🫠(Dummkopf)")
        else:
            view.show_error_message("Hättest mal die Regeln gelesen.🤦🏻‍")
    return False


def main():
    # Start Game
    game_data = model._reset_game_data()
    while game_data["choice"] not in ['3', 'exit', 'beenden']:
        view.view_greet_user(game_data)
        if game_data["choice"] in ['2', 'start']:
            game_data = model.game_start()
            # Run Game
            while True:
                get_user_guess_of_letter(game_data)
                model.game_run(game_data)
                if game_data["trials"] >= 3 and game_data["state"] not in ["win"]:
                    display_side_by_side("snake_distance_good")
                elif game_data["trials"] == 2:
                    display_side_by_side("snake_distance_bad")
                elif game_data["trials"] == 1:
                    display_side_by_side("snake_distance_worse")
                if game_data["state"] in ["win", "lose"]:
                    break
            # End Game: win or lose
            model.game_end(game_data)
            if game_data["state"] == "win":
                view.show_char_list_after_win(game_data)
                print()
                display_side_by_side("snake_distance_won")
                view.show_win_message()
            elif game_data["state"] == "lose":
                display_side_by_side("snake_distance_loose")
                print()
                view.show_lose_message()
        if game_data["choice"] not in ['3', 'exit', 'beenden']:
            input("Drücke Enter um neu zu starten.")


if __name__ == "__main__":
    main()
