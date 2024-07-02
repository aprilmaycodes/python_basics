# Error Handling and Conditional Statements

Hello! Welcome to entry two in the AprilMayCodes Python tutorial series! In this section, I go over an introduction to error handling, and introduce conditions with if/else statements. Let's get started!

## 1. Common Errors

First, let's talk about some errors. If you copy the following code into your editor and try to run it, you're going to have some issues.
Code:
```
name = 'April"
print(name
age = 29
print("Hello! My name is " + name + ". I am " + age + " years old.")
```
As you can probably see, there are a number of errors in the code above. When we run it, however, we don't get a list of all of them.

Instead, Python tries to run the code line by line, and when it comes to the first error it exits, telling you what the error it encountered was. We get something like this:
```
File "path/to/your/file.py", line 1
    name = 'April"
           ^
SyntaxError: unterminated string literal (detected at line 1)
```

It tells us what file gave the error, and details about the error. In this case, the bug that crashed the program is in the first line, an "unterminated string literal". We can translate that from jargon to mean a string that wasn't closed properly. If you look closer at the name variable, you'll see that it opens with a `'` but is closed with `"`. An easy fix. Our updated code is:
```
name = 'April'
print(name
age = 29
print("Hello! My name is " + name + ". I am " + age + " years old.")
```
Running it now, we get something like:
```
File "path/to/your/file.py", line 2
    print(name
         ^
SyntaxError: '(' was never closed
```

As you can see, the errors in the terminal can be pretty handy - pointing you to the location of the error and giving you information about what was wrong. Let's fix this error and run the program again.

Now we get the following error:
```
April
Traceback (most recent call last):
  File "path/to/your/file.py", line 4, in <module>
    print("Hello! My name is " + name + ". I am " + age + " years old.")
          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~
TypeError: can only concatenate str (not "int") to str
```
If you look at the bottom line, you can see the error details. We can't concatenate a string with an int, it must be another string.
But if you look at the top of the console, you can see it printed `April`. This is because python reads the files line by line.
- On line 1, we create a variable `name` and set it equal to "April".
- On line 2, we print `name`.

Neither of these lines throw an error, so the program is able to execute them and we can see our printed statement.
- On line 3, we create a variable `age` and assign it the value of 29. No errors.
- On line 4, however, it's unable to execute the print command because we're trying to concatenate a string with an int. So, it throw an error and that's the information we see at the bottom of the terminal.

As your programs get more complex so, to, will your errors. It's a good idea to get used to reading and understanding them. It will help you immensely in your projects.

## 2. Revisiting the Pokedex project

Let's revisit the pokedex project from tutorial 1. If you have your file from the last tutorial, great! If not, you can download or copy the starter code [here](02_starter.py).

Our pokedex app is pretty nice, but it doesn't handle some common errors. For instance, what happens if the user asks for 'charizard'? Let's find out!
Output:
```
Traceback (most recent call last):
  File "path/to/your/file.py", line 28, in <module>
    answer = pokedex[choice][req_info]
             ~~~~~~~^^^^^^^^
KeyError: 'charizard'
```

We get a KeyError. This means it didn't recognize the key given (charizard) as a value in the pokedex dictionary. This is because the key 'charizard' *doesn't* exist in the pokedex dictionary.

We could work around this, by adding every pokemon to our dictionary. But, obviously we aren't going to do that, lol.

Instead, we need to check if the user input is valid.

## 3. Conditional Statements

This brings us to the main topic: conditional statements!

Conditional statements allow our programs to make decisions based on certain conditions. Here's the basic structure of an if/else statement:
```
if condition:
  # code to execute if condition is true
else:
  # code to execute if condition is false
```
But what if you want to check multiple conditions? You can use `elif` (short for "else if"):

```
if condition_one:
  # code to execute if condition_one is true
elif condition_two:
  # code to execute of condition_two is true
else:
  # code to execute if both conditions are False
```
You can use more than one `elif` in a statement as well. I'll expand on all this a bit more, but before we dive into examples, let's quickly go over some different types of operators we may want to use.

The following are Comparison Operators.

- `<` : Less than
- `<=` : Less than or equal to
- `>` : Greater  than
- `>=` : Greater than or equal to
- `==` : Equal to
- `!=`: Not equal to

Remember, `==` is for comparison, while `=` is for assignment. If it helps, you can remember "equals" (one word) for `=` (one equals sign) and "if equals" (two words) for `==` (two equals signs). If it's one sign, we're setting the variable on the left to be equal to the value on the right. If it's two, we're checking for equality between the two values (returns a bool; True or False).

Membership Operators include:
 - `in`: Exists in
 - `not in` : Does not exist in

 These are useful for checking if a given variable exists (or does not exist) in a list, for example.

 Arithmetic Operators are what they sound like. They allow us to do math in our code.

 - `+` : Addition
 - `-`: Subtraction
 - `*`: Multiplication
 - `/`: Division
 - `**`: Exponents
 - `//`: Floor division (divide, then round down to the nearest whole number)
 - `%`: Modulo (returns the remainder)
   - This is especially useful when checking if a number is odd or even. For example:
   - ```
      if num % 2 == 0:
        print("even number")
      else:
        print("odd number")
      # if the remainder of the number/2 is 0, it's an even number
      # there's no remainder because 2 divides into it evenly
     ```
  You can also use shorthand with arithmetic operators: `+=`, `-=`, `*=`, etc.

So if I wanted to take a variable `num` and increase it by 1, I could write:
```
num = num + 1
```
but I could also use the shorthand, and write it like this:
```
num += 1
```
Some more examples:
```
# Starting value
num = 5

# Using *=
num *= 4  # This is equivalent to: num = num * 4
print(num)  # Output: 20

# You can use it with variables too
increment = 2
num /= increment  # This is equivalent to: num = num / increment
print(num)  # Output: 10

# It works with other data types as well, like strings
greeting = "Hello"
greeting += " World"  # This is equivalent to: greeting = greeting + " World"
print(greeting)  # Output: "Hello World"
```
The shorthand performs the operation, then assigns the result back to the variable.

We can use these operators to create conditions for our conditional statements. Let's take a look at how:

```
season = input("What season is it?")
if season.lower() == 'summer':
  print("Try to stay cool!")
```
If I run this code, python will check if `season.lower()` is equal to summer, which it is. Because the if condition was True, it goes into the statement to look for the next lines to run, and executes the print statement.

What if it weren't summer? Let's run the example again, but input 'winter', or anything else, as our answer.

I gave my input, but nothing happened and the program ended. This is becasue the if condition was false, so it skipped over the indented code. There was nothing else to run, so it ended.

We can expand on this by adding elif, or else, or both.
```
season = input("What season is it?")
if season.lower() == 'summer':
  print("Try to stay cool!")
elif season.lower() == 'winter':
  print("It's a beautiful day to stay inside!")
else:
  print("Enjoy the season!")
```
It's important to note the differences between `elif` and `else`. `elif` can be used multiple times in the same if statement, you can have multiple conditions you want to check. `else` can only be used once; it's like the default if *all* of your conditions are False. It can also be omitted, if you want nothing to happen.

## 4. Working with Lists and the `in` Keyword

Now, let's explore how we can use lists and the `in` keyword to improve our code.

In Python, we can convert iterable objects, like dictionary keys, to a list using the `list()` function. For example:
```
pokemon_list = list(pokedex.keys())
print(pokemon_list)
```
This prints a list of the keys in our pokedex dictionary.

We can use the `in` keyword to check if something is in this list:
```
if 'pikachu' in pokemon_list:
    print("Pikachu is in the Pokedex!")
else:
    print("Pikachu hasn't been discovered yet.")
```
## 5. Updating the Pokedex Project
Based on what we've learned, can you update the Pokedex project to handle invalid user input? Try it on your own, and then expand the section below to compare your answer.
<details><summary>Ready to compare your answer?</summary>
We've got two user inputs we want to check the validity of. The first, choice, needs to be one of the keys in the pokedex, so we can create a list using the `list()` function, and check 
if choice in pokemon_list:

```
pokemon_list = list(pokedex.keys())
choice = input("Which Pokémon would you like to learn about? ").lower()

if choice in pokemon_list:
```
Now we come to our second input, req_info. This we need to compare to the keys in the `pokedex[choice]` dictionary. We ca do this using the same process:
```
    options = list(pokedex[choice].keys())
    req_info = input("Which info would you like to know? (name type, hp, evolution): ").lower()
    if req_info in options:
```
Now we just need to put it all together and handle our `else` statements.
```
pokemon_list = list(pokedex.keys())
choice = input("Which Pokémon would you like to learn about? ").lower()

if choice in pokemon_list:
  options = list(pokedex[choice].keys())
  req_info = input("Which info would you like to know? (type, hp, attack, defense): ").lower()
  if req_info in options:
      print(f"{req_info} for {choice.capitalize()} is: {pokedex[choice][req_info]}")
  else:
      print(f"I don't have information about {req_info} for {choice.capitalize()}.")
else:
    print(f"Oops! Looks like {choice.capitalize()} has not been discovered yet.")
```
Notice the indentation for the else statements. The innermost one, on the 9th line, is paired with the line `if req_info in options`, while the final `else` statement, on line 11 is paired with the line `if choice in pokemon_list`.

Proper indentation is crucial to ensuring your projects run correctly
</details>

Did you do all right? Let's apply the what we've learned to a slighly bigger project: a Pokemon twist on the classic Rock Paper Scissors!

## 6. Fire, Grass, Water Game

The rules are simple. The user plays against the computer. Fire beats Grass, Grass beats Water, and Water beats Fire.

Before you start, one last thing you'll need for this: the random module.

Modules are a way to organize and reuse code. Python comes with several built-in modules, including random. Here's how to use it:
```
import random

# Create a list of choices
choices = ['fire', 'grass', 'water']

# Get a random choice for the computer
computer_choice = random.choice(choices)
```

Now, you should have all the tools you need to create this project!
<details><summary>Check here to see how I did it!</summary>
We've imported random, created a list of choices, and gotten the computers choise. Now we need the user to choose.

```
user_choice = input("Enter your choice (fire, water, or grass): ").lower()
```

Next, we need to check if the users choice is valid:
```
if user_choice in choices:
  pass
else:
  print("That is not a valid choice.")
```

Now we can handle the rest with `elif` and nested if/else statements.
Here's what that looks like:

```
if user_choice in choices:
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 'water':
        if computer_choice == 'fire':
            print("Water beats fire. You win!")
        else:
            print("Grass beats water. You lose!")
    elif user_choice == 'fire':
        if computer_choice == 'water':
            print("Water beats fire. You lose!")
        else:
            print("Fire beats grass. You win!")
    elif user_choice == 'grass':
        if computer_choice == 'fire':
            print("Fire beats grass. You lose!")
        else:
            print("Grass beats water. You win!")
else:
    print("That is not a valid choice.")
```

Notice for each possible user answer, we're only checking for two computer_choice possibilities. This is because we *first* check `if user_choice == computer_choice`. If that condition were met, it would print that it's a tie and not even check for the following `elif` statements, so there's no need to code for that possibility a second time.
</details>

<details><summary>Complete project solution</summary>

```
import random

choices = ['fire', 'grass', 'water']

computer_choice = random.choice(choices)
user_choice = input("Enter your choice (fire, water, or grass): ").lower()

if user_choice in choices:
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 'water':
        if computer_choice == 'fire':
            print("Water beats fire. You win!")
        else:
            print("Grass beats water. You lose!")
    elif user_choice == 'fire':
        if computer_choice == 'water':
            print("Water beats fire. You lose!")
        else:
            print("Fire beats grass. You win!")
    elif user_choice == 'grass':
        if computer_choice == 'fire':
            print("Fire beats grass. You lose!")
        else:
            print("Grass beats water. You win!")
else:
    print("That is not a valid choice.")
```

</details>

## Conclusion
And there you have it! A pokemon-style Rock Paper Scissors game and a better understanding of error handling and conditional statements in Python. I hope this was helpful and fun!

That's all for this lesson, but remember; practice is key in programming. Try modifying the Pokedex or the Fire, Grass, Water game to add new features or handle different scenarios.
If you have any questions, suggestions, or feedback feel free to reach out! Until next time, Happy Coding!