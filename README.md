# Whiteboard Wednesdays - Greetings

## Please Read!

Your mission is to solve a problem we'll describe below.

But your _real_ mission is to prepare to help someone else solve it.

## Help Someone Else Solve It?!

Tomorrow you'll be interviewing someone, helping them through the process of solving this problem. So as you solve this, think through your process. You'll be able to use that to, with the benefit of hindsight, guide your partner through that same process.

Also... that same person will interview you too!

## Things To Think About As You Do This

- As an interviewer, you'll have to think about how YOU solved the problem.
- Remember that you won't be solving the problem for them, but helping guide them there.
- Think about what helped get you unstuck on this problem. They may get stuck in the same places!
- This will be an amazing learning experience for YOU, as a teacher--you'll need to understand the problem enough to help someone though it.
- Don't forget that tomorrow you can give _them_ the advice below!

## When You're Getting Interviewed Tomorrow

- Talk through the problem - it's about the process, not the solution
- Don't give up
- Ask about edge cases - 0 and negative numbers and empty strings and multiple words and all that!
- Solve the problem, don't build the app
  - Don't sweat syntax
  - Pseudocode
  - Invent helper functions if necessary... you don't need to actually _write_ those functions! Just imagine a function to, say, check if a string is in another string, use it, and if you ever code it FOR REAL you could always write it then.

## The Problem You'll Be Interviewing Someone On

Make a `solution.py` that solves the following problem: given a string representing a language (we'll plan for "english", "spanish", and "french"), print out a greeting for that language (in this case: "Hello!" and "Hola!" and "Bonjour!").

## Basic Run-Through

- Ask the user running the program (using `input()`) for a language. You should NOT assume it will come in any particular case (they could enter it in uppercase or lowercase or mixed), but you CAN assume it'll only be one word.
- Include some logic to choose from the right greeting based on that input.
- Print out that greeting!

## Streeeeeetch Goal

- Did you use an `if`? What if we have 20 languages? 100? You don't want to write all those `elif`s! Think about how you could use a dictionary with keys. Each key could be a language, and each value, the... ??
