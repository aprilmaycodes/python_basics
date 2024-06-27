# Error Handling and Conditional Statements
# --In Progress--

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

Instead, Python tries to run the code line by line, and when it comes to the first error it exits, telling you what the error it encountered what. So if we run it now, we get something like this:
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
But if you look at the top of the error, you can see it printed `April`. This is because python reads the files line by line.
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

We could work around this, by adding every pokemon to our dictionary. But, obviously we aren't going to do that lol.

Instead, we need to check if the user input is valid.

## 3. Conditional Statements

