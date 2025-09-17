"""Alexej, Jakob
View:1.
-  Greet (ask user name)
- def show_greeting(name)2.
- def show_rules()
3.
- def show_character_list()
- def show_title_list(title_list) (start with 0. )
- Show Snake (init, growing/move, biting)
4.
- Show initial article and links
- Show llist of characters (hidden / revealed)
- Let user pick article and index in title
- Ask if user wants to continue/abort game
"""
import random
import re
import time

from rich.console import Console
from rich.markdown import Markdown
console = Console()


def view_greet_user(data) -> str: # <- Sollte von 'controller' zu Spielstart aufgerufen werden!
    """Haupteinstiegspunkt - Bootvorgang und Menü"""
    view_show_boot_sequence()

    while True:
        choice = view_show_main_menu().lower()
        data["choice"] = choice

        if choice in ['1', 'regeln']:
            console.clear()
            view_show_rules()
            console.clear()
            view_show_game_title()  # Titel wieder anzeigen

        elif choice in ['2', 'start']:
            console.clear()
            user_name = view_ask_user_name()
            # Hier würde das eigentliche Spiel starten
            # State hier verändern oder in controller?
            # ...
            return choice

        elif choice in ['3', 'exit', 'beenden']:
            typo_typewriter("Auf Wiedersehen! Bis zum nächsten Mal!\n")
            break

        else:
            console.print("\n[red]Ungültige Eingabe! Bitte wähle 1(regeln), 2(start) oder 3(exit).[/red]")
            time.sleep(1)
    return


def view_show_boot_sequence():
    """Bootvorgang-ähnlicher Titel"""
    console.print("\n[dim]Initialisiere Spiel...[/dim]")
    time.sleep(1.8)
    console.print("[dim]Lade Spielregeln...[/dim]")
    time.sleep(0.4)
    console.print("[dim]Bereite Umgebung vor...[/dim]")
    time.sleep(1.3)
    console.print("[bold green]Bereit![/bold green]\n")
    time.sleep(0.7)
    console.clear()
    view_show_game_title()


def view_show_game_title():
    # ASCII-Gametitel
    game_title_border = "*" * 64
    game_title_lines = [
        "  _____ _____ _____  ",
        " |  ___|_   _|  _  | ",
        " | |__   | | | |_| | ",
        " |  __|  | | |  ___/ ",
        " | |___  | | | |     ",
        " |_____|_|_|_|_|     ",
        " Escape The Python   ",
    ]

    # Titel langsam aufbauen
    console.clear()
    console.print(game_title_border, style="bold green", justify="center")
    for line in game_title_lines:
        console.print("*" + line.center(62) + "*", style="bold green", justify="center")
        time.sleep(0.2)
    console.print(game_title_border, style="bold green", justify="center")
    time.sleep(1.5)


def view_show_main_menu():
    """Hauptmenü mit Verschreiber-Animation"""
    menu_text = """
╔═══════════════════════════════════════════╗
║                 HAUPTMENÜ                 ║
╠═══════════════════════════════════════════╣
║     1. Regeln anzeigen | (1 or regeln)    ║
║     2. Spiel starten   | (2 or start)     ║
║     3. Spiel beenden   | (3 or exit)      ║
╚═══════════════════════════════════════════╝

Deine Wahl: """

    typo_typewriter(menu_text, None, 0.05, 0.02)
    return console.input()


def typo_typewriter(text, user_name=None, typo_chance=0.10, delay=0.05):
    """
    Schreibt Text mit gelegentlichen Verschreibern, die korrigiert werden.
    """
    typos = {
        'e': ['3', 'w', 'r'],
        'o': ['9', '0', 'p'],
        'i': ['8', 'u', 'o'],
        'a': ['s', 'q'],
        'l': ['k', ';', 'ö'],
        't': ['r', 'y', '6'],
        'n': ['m', 'b'],
        'r': ['e', 't', '4'],
        's': ['a', 'd'],
        'u': ['y', 'i', '7'],
        'k': ['j', 'l'],
        'm': ['n', ',']
    }

    if user_name and user_name in text:
        # Text mit Namen aufteilen
        parts = text.split(user_name)

        def type_with_typos(part, style="bold cyan"):
            for char in part:
                if char.lower() in typos and random.random() < typo_chance:
                    wrong_char = random.choice(typos[char.lower()])
                    console.print(wrong_char, style=style, end="")
                    time.sleep(delay * 2)
                    print("\b \b", end="")
                    time.sleep(delay)
                console.print(char, style=style, end="")
                time.sleep(delay)

        type_with_typos(parts[0], "bold cyan")
        type_with_typos(user_name, "bold yellow")
        if len(parts) > 1:
            type_with_typos(parts[1], "bold cyan")
    else:
        # Normaler Text ohne Namen
        for char in text:
            if char.lower() in typos and random.random() < typo_chance:
                wrong_char = random.choice(typos[char.lower()])
                console.print(wrong_char, style="bold cyan", end="")
                time.sleep(delay * 2)
                print("\b \b", end="")
                time.sleep(delay)
            console.print(char, style="bold cyan", end="")
            time.sleep(delay)


# Version mit Formatierung der .md
def view_show_rules() -> None:
    with open('regeln.md', 'r', encoding='utf-8') as f:
        text = f.read()

    def repl(match):
        content = match.group(1)
        return f"\033[4;34m{content}\033[0m"

    text = re.sub(r"\*\*(.+?):\*\*", repl, text)
    md = Markdown(text, code_theme="monokai")

    console.print(md)

    # Zurück-Menü
    while True:
        console.print("\n" + "=" * 50)
        choice = console.input("\n[bold cyan]Zurück ins Menü? (zurück/back/exit): [/bold cyan]").lower()
        if choice in ['zurück', 'back', 'exit', 'ende']:
            break


def view_ask_user_name() -> str:
    # Spielername abfragen
    user_name = console.input("\n[bold cyan]Wie heißt du, mutiger Spieler? [/bold cyan]")
    # Welcome Nachricht mit realtime Verschreiber-Animation
    welcome_message = f"\nWillkommen, {user_name}! Viel Erfolg beim Entkommen!\n"

    typo_typewriter(welcome_message, user_name)
    return user_name


def show_titles(data):
    print("\n\n")
    for number, title in enumerate(data["titles"]):
        print(f"{number}. {title}")
    print()


def show_title_with_indices(data):
    title = data["titles"][data["row_titles"]]
    width = 2
    for i, char in enumerate(title):
        if i <= 9:
            print(f" {char:<{width - 1}}", end="")
        else:
            print(f" {char:<{width}}", end="")
    print()
    for i in range(len(title)):
        if i <= 9:
            print(f"{i:>{width}}", end="")
        else:
            print(f" {i:>{width}}", end="")
    print()


def show_char_list_and_trials(data):
    console.print(f"[bold cyan]Trials:[/bold cyan] [bold red]{data["trials"]}[/bold red]")
    console.print("Das Lösungswort ist: ", style="bold cyan", end="")
    for char in data["char_list"]:
        print(char, end=" ")
    print()


def show_char_list_after_win(data):
    console.print(f"[bold cyan]Du hast nur[/ bold cyan] [bold red]{data['trials']}[/ bold red] [bold cyan]gebraucht![/ bold cyan]")
    searched_word = ""
    for char in data["char_list"]:
        searched_word += char
    console.print(f"[bold cyan]Du hast das Wort[/ bold cyan] `[bold red]{searched_word}[/ bold red]` [bold cyan]erfolgreich gefunden und bist der Python entkommen![/ bold cyan]")


def input_from_user(data, string_to_print):
    # call: row_titles = input_from_user(data, "Bitte wähle eine Zeile: ")
    # call: pos_letter = input_from_user(data, "Bitte wähle den Index für den gewünschten Buchstaben: ")
    return input(string_to_print)


def show_error_message(string_to_print):
    console.print(string_to_print, style="bold red")


def show_win_message():
    win_messages = [
        "Tja, du hängst – ich denk.",
        "Schon wieder gerettet – Sherlock wäre stolz.",
        "Du brauchst keine Buchstaben – du hast Instinkt!",
        "Erraten, bevor es peinlich wurde. You're welcome."
    ]
    console.print(random.choice(win_messages), style="bold yellow")


def show_lose_message():
    lose_messages = [
        "„A… B… C… oh nein… R.I.P.",
        "Buchstabensuppe war wohl nie dein Ding!",
        "Du hängst hier nur rum – wortwörtlich.",
        "Hangman? Eher Failman.",
        "Du hast das Wort fast – also… bis auf alle Buchstaben.",
        "Du hast schwach angefangen und stark nachgelassen."
    ]
    console.print(random.choice(lose_messages), style="bold red")

#show_win_message()
#print("====== TRENNLINIE ======")
#show_lose_message()











# IDEEN FÜR MÄNNCHEN & SCHLANGE !!

snake_variants = {
    "snake_distance_loose": [
        r"                                 /^\/^\                       ",
        r"                               /|0_ |0_|_                     ",
        r"                            __//     ~\   \   \/              ",
        r"                           / \________|___/___/               ",
        r"                          /     ______/                       ",
        r"~-__       _-~ ~-__      /    _/                              ",
        r"    ~_-_-~        ~-____-   _/                                ",
        r"                           /                                  ",
        r"__-_-~___-~-~--______-~-~_/             🦴💀🦴               "
    ],
    "snake_distance_worse": [
        r"                                 /^\/^\                       ",
        r"                               /|0_ |0_|_                     ",
        r"                            __//     ~\   \   \/              ",
        r"                           / \________|___/___/               ",
        r"                          /     ______/                       ",
        r"~-__       _-~ ~-__      /    _/                     ◉!!      ",
        r"    ~_-_-~        ~-____-   _/                      \|/       ",
        r"                           /                         |        ",
        r"__-_-~___-~-~--______-~-~_/                         ╱ ╲       "
    ],
    "snake_distance_bad": [
        r"                                                             ",
        r"                       /^\/^\                                ",
        r"                     /|0_ |0_|_                              ",
        r"                  __//     ~\   \   \/                       ",
        r"                 / \________|___/___/                        ",
        r"_-~ ~-__        /     ______/                       ◉!!      ",
        r"       ~-____-   _/                                \|/       ",
        r"                /                                   |        ",
        r"-~--______-~-~_/                                   ╱ ╲       "
    ],
    "snake_distance_good": [
        r"                                                            ",
        r"         /^\/^\                                             ",
        r"       /|0_ |0_|_                                           ",
        r"    __//     ~\   \   \/                            ◉       ",
        r"   / \________|___/___/                            /|\      ",
        r"  /     ______/                                     |       ",
        r"_/     /                                           ╱ ╲      "
    ],
    "snake_distance_won": [
        r"                    🎉   🎈                                 ",
        r"                     \ ◉ /                                  ",
        r"                      \|/                                   ",
        r"                       |                                    ",
        r"                      ╱ ╲                                   ",
        r"                                                            "
    ],
}


def display_side_by_side(snake_type):
    # Zeile für Zeile nebeneinander ausgeben
    if snake_type in snake_variants:
        for i in snake_variants[snake_type]:
            print(i)


#print("=== BEISPIEL 1: Realistische Schlange mit stehendem Männchen ===")
#display_side_by_side("snake_distance_bad")

