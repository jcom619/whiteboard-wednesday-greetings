# # The Problem You'll Be Interviewing Someone On

# Make a `solution.py` that solves the following problem: given a string representing a language (we'll plan for "english", "spanish", and "french"), print out a greeting for that language (in this case: "Hello!" and "Hola!" and "Bonjour!").

# # Basic Run-Through

# - Ask the user running the program(using `input()`) for a language. You should NOT assume it will come in any particular case(they could enter it in uppercase or lowercase or mixed), but you CAN assume it'll only be one word.
# - Include some logic to choose from the right greeting based on that input.
# - Print out that greeting!

# # Streeeeeetch Goal

# - Did you use an `if`? What if we have 20 languages? 100? You don't want to write all those `elif`s! Think about how you could use a dictionary with keys. Each key could be a language, and each value, the... ??

# todo USED DICTIONARY TO SIMPLIFY SELECTION OF LANGUAGE
greeting_lang = {
    "e_greet": "Hello!",

    "s_greet": "Hola!",

    "f_greet": "Bonjour!"
}

# todo VARS ASSIGNED TO SELECT DICT. ITEMS EASILY
e = greeting_lang['e_greet']
s = greeting_lang['s_greet']
f = greeting_lang['f_greet']

# tod CHOSE NUMBERS AS A TEMPORARY BRUTEFORCE RESPONSE FOR AVOIDING ANY POSSIBLE CAPS PROBLEMS

make_selection = input("\ntype your language and press return:\n")


def greet_response(make_selection):
    if(make_selection.lower() == "english"):
        print(e)
    elif(make_selection.lower() == "spanish"):
        print(s)
    elif(make_selection.lower() == "french"):
        print(f)
    else:
        print("make sure your selection is within the parameters of 1, 2 or 3!")


greet_response(make_selection)
