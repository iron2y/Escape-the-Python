"""
Model for Escape the Python
Author: Ronny Borries
"""

import faker
import random
import wikipedia

"""from enum import Enum
class GameState(Enum):
    START = 0
    RUN = 1
    WIN = 2
    LOSE = 3"""

data = None


def _reset_game_data(): # "_" do not use after import
    return {
        "state": "start",  # start, run, win, lose #
        "trials": 3,#
        "solution_word": "",  # only upper case letters #
        "char_list": [], #
        "guessed_letters": [],  # only upper case letters #
        "is_guessed_letter_right": False,
        "start_title": "Python_(genus)",
        "titles": [], #
        "row_titles": 0,  # user choice row of titles
        "pos_letter": 0,  # user choice position of a letter
        "is_letter_in_guessed_letters": False,
        "is_unsolvable": False,
        "choice" : "0"
    }


# TO DOs:
# VIEW integrieren
# Kommentare für functions
# Error-Handling
# Testing
# User Inputs & Prints in View verschieben

def game_start():
    data = _reset_game_data()
    data["solution_word"] = get_solution_word(
        8, 10)
    data["char_list"] = create_char_list(data)
    create_urls_and_titles_from_wikipedia(data, 10)
    data["state"] = "run"
    return data


def game_run(data):
    if data["state"] != "run":
        return
    add_or_sub_trials(data)
    data["char_list"] = create_char_list(data)
    data["state"] = set_new_state(data)
    is_unsolvable(data)
    create_urls_and_titles_from_wikipedia(data, 10)
    return


def game_end(data):
    if data["state"] not in ["win", "lose"]:
        return
    data["char_list"] = create_char_list(data)
    return


def is_letter_in_guessed_letters(data, letter):
    data["is_letter_in_guessed_letters"] = letter in data["guessed_letters"]
    return


def check_if_letter_in_solution(data, letter):
    data["is_guessed_letter_right"] = letter in data["solution_word"]


def convert_row_and_pos_to_letter(data):
    letter = data["titles"][data["row_titles"]][data["pos_letter"]]
    return letter.upper()


def add_or_sub_trials(data):
    trials = data["trials"]
    if data["is_guessed_letter_right"] and not data["is_letter_in_guessed_letters"]:
        if trials <= 5:
            trials += 1
    elif not data["is_guessed_letter_right"] or data["is_letter_in_guessed_letters"]:
        trials -= 1
    data["trials"] = trials
    return


def set_new_state(data):
    if is_solved(data):
        return "win"
    elif not has_trials(data):
        return "lose"
    return "run"


def is_solved(data):
    return data["char_list"].count("_") == 0


def has_trials(data):
    return data["trials"] > 0


def create_char_list(data):
    char_list = []
    if data["state"] == "start":
        # only hidden letters
        for _ in range(len(data["solution_word"])):
            char_list.append("_")
    elif data["state"] == "run":
        char_list = data["char_list"]
        # partly revealed letters
        for letter in data["guessed_letters"]:
            if letter in data["solution_word"]:
                for index in range(len(data["solution_word"])):
                    if data["solution_word"][index] == letter:
                        char_list[index] = letter
    elif data["state"] in ["win", "lose"]:
        # no hidden letter
        for char in data["solution_word"]:
            char_list.append(char)
    return char_list


def get_solution_word(max_length_of_word=10, max_length_of_selection_list=10):
    german_cities = [
    "Berlin",
    "Hamburg",
    "München",
    "Köln",
    "Frankfurt am Main",
    "Stuttgart",
    "Düsseldorf",
    "Dortmund",
    "Essen",
    "Leipzig",
    "Bremen",
    "Dresden",
    "Hannover",
    "Nürnberg",
    "Duisburg",
    "Bochum",
    "Wuppertal",
    "Bielefeld",
    "Bonn",
    "Münster",
    "Karlsruhe",
    "Mannheim",
    "Augsburg",
    "Wiesbaden",
    "Gelsenkirchen",
    "Mönchengladbach",
    "Braunschweig",
    "Chemnitz",
    "Kiel",
    "Aachen",
    "Halle (Saale)",
    "Magdeburg",
    "Freiburg im Breisgau",
    "Krefeld",
    "Lübeck",
    "Oberhausen",
    "Erfurt",
    "Mainz",
    "Rostock",
    "Kassel",
    "Hagen",
    "Saarbrücken",
    "Hamm",
    "Potsdam",
    "Ludwigshafen am Rhein",
    "Oldenburg",
    "Leverkusen",
    "Osnabrück",
    "Solingen",
    "Heidelberg",
    "Herne",
    "Neuss",
    "Darmstadt",
    "Paderborn",
    "Regensburg",
    "Ingolstadt",
    "Würzburg",
    "Fürth",
    "Heilbronn",
    "Pforzheim",
    "Wolfsburg",
    "Göttingen",
    "Bottrop",
    "Reutlingen",
    "Koblenz",
    "Bremerhaven",
    "Recklinghausen",
    "Bergisch Gladbach",
    "Erlangen",
    "Remscheid",
    "Jena",
    "Trier",
    "Moers",
    "Siegen",
    "Hildesheim",
    "Salzgitter",
    "Cottbus",
    "Zwickau",
    "Gera",
    "Kaiserslautern",
    "Witten",
    "Stralsund",
    "Gütersloh",
    "Iserlohn",
    "Schwäbisch Gmünd",
    "Hanau",
    "Esslingen am Neckar",
    "Ludwigsburg",
    "Landshut",
    "Tübingen",
    "Villingen-Schwenningen",
    "Konstanz",
    "Flensburg",
    "Passau",
    "Lüneburg",
    "Rosenheim",
    "Gladbeck",
    "Worms",
    "Neumünster"
    ]
    list_of_words = [city for city in german_cities if len(city) <= max_length_of_word]
    solution_word_with_umlauts = random.choice(list(list_of_words)).upper()
    solution_word = exchange_umlauts(solution_word_with_umlauts)
    return solution_word


def exchange_umlauts(word):
    umlauts_exchange= {"Ä": "AE", "Ö": "OE", "Ü": "UE"}
    word_no_umlauts = word
    for umlaut, exchange in umlauts_exchange.items():
        word_no_umlauts = word_no_umlauts.replace(umlaut, exchange)
    return word_no_umlauts


def create_urls_and_titles_from_wikipedia(data, max_number_of_titles=20):
    if data["state"] in ["win", "lose"]:
        data["titles"] = []
    elif data["state"] == "start":
        data["titles"] = wikipedia.search(data["start_title"], results=max_number_of_titles)
    elif data["state"] == "run" and data["is_guessed_letter_right"]:
        data["titles"] = wikipedia.search(data["titles"][data["row_titles"]], results=max_number_of_titles)
    elif data["state"] == "run" and data["is_unsolvable"]:
        data["titles"] = wikipedia.search(data["titles"][data["row_titles"]], results=max_number_of_titles)
    return


def is_unsolvable(data):
    for char in data["solution_word"]:
        if char not in data["titles"]:
            data["is_unsolvable"] = True
            return
    data["is_unsolvable"] = False
    return


def process_guess_of_letter(data): # >>> model
    guessed_letter = convert_row_and_pos_to_letter(data)
    check_if_letter_in_solution(data, guessed_letter)
    is_letter_in_guessed_letters(data, guessed_letter)
    if not data["is_letter_in_guessed_letters"]:
        data["guessed_letters"].append(guessed_letter)
        return
    return "Buchstabe wurde schon geraten, konzentrier dich!"
