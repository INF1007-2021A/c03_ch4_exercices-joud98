#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    even_len = None 
    if len(string) % 2 == 0 :
        even_len = True
    else:
        even_len = False 
    return even_len


def remove_third_char(string: str) -> str:
    word_without_third_letter= string[0:2]+string[3:]
    return word_without_third_letter


def replace_char(string: str, old_char: str, new_char: str) -> str:
    word_with_Z = string.replace("w", "z")
    return word_with_Z


def get_nb_char(string: str, char: str) -> int:
    compteur = 0
    for letter in string :
        if letter == char:
            compteur = compteur +1
    return compteur


def get_nb_words(string: str) -> int:
    nb_mot = 1
    for letter in string :
        if letter == " " : 
            nb_mot = nb_mot + 1 
    return nb_mot 


def main() -> None:
    string = "Bonjour!"
    parity = 'pair' if is_even_len(string) else 'impair'
    print(f"Le nombre de caractère dans la chaine '{string}' est {parity}")

    string = "Sam est cool!"
    print(f"On supprime le 3e caratère dans la chaine '{string}'. Résultat: {remove_third_char(string)}")

    string = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: '{string}'. Résultat: {replace_char(string, 'w', 'z')}")

    string = "hello!"
    print(f"Le nombre d'occurrence de l dans hello est : {get_nb_char(string, 'l')}")
    
    string = "Baby shark doo doo doo doo doo doo"
    print(f"Le nombre de mots dans la chaine {string} est: {get_nb_words(string)}")


if __name__ == '__main__':
    main()
