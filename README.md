# RPG Tools

A set of tools to keep track of character information for Tabletop Roleplaying
Games. Also includes a dice roller!

Made as my final project for Harvard's CS50

### Video Demo 

[RPG Tools](https://youtu.be/x9eLf6_0TF4)

## Features

* Dice Roller
* User Accounts
* HP Tracker

## Description

### Dice Roller

The site includes a simple dice roller, which does not need an account to use.
Originally I made a dice rolling app in Python, which worked perfectly via the
command line. However, I realized quickly that it was not the most practical
implementation when trying to integrate it into this web app. I rewrote the
program in Javascript in order to increase performance, and reduce the need for
multiple requests.

### User Accounts

I made user accounts because I wanted to make something that my friends with
whom I played these games could use in addition to me. I designed the database
(rpg\_tools.db) so that multiple users could have characters with the same name.

### HP Tracker

The HP Tracker requires a login because the characters are tied to user accounts
in the database. The HP Tracker allows the user to keep track of all their
characters' health levels in between game sessions. It also provides a tool for
the user to adjust their characters' health more easily, taking the damage or
healing value as an input. Instead of needing to do mental math to find the new
current hp of the character, a user can instead input the damage or healing
received and their character's HP will be updated.

#### Adding Characters

Users can add a character to the account, and will be prompted to provide a
maximum HP for that characters. The tool will only accept a minimum of 1 for the
maximum HP.

#### Removing Characters

Users can remove characters from their accounts on this page. Again, the program
will ask the user to confirm the removal of the character. One feature that I
want to add in the future would be a more robust confirmation. For example,
asking the user to type the name of the character they wish to remove as a
confirmation.

#### Editing Maximum HP

Users can edit the maximum HP of their characters (if, for example, the
character's level increases).

### Styling and Color Palette

In order to come up with the color scheme for the site I used the wonderful
tool at [colormind.io](http://colormind.io), which generates color palettes based
on the machine learning algorithm the developer came up with. I then made some
tweaks to [Bootstrap](https://getbootstrap.com) to make the buttons, cards, and
headers all look like I wanted. I also added a little dice icon to display in
the tab corner.

#### Buttons

I made the buttons on the HP Tracker very big because I wanted it to translate
well to a mobile format. While playing TTRPGs online it is easy to access
websites and all kinds of tools, but in person sometimes the easiest thing is to
use a phone or tablet. Having quick access to the HP Tracker and being able to
add remove and edit characters easily was something I thought was important.

#### Navbar

I started with a Bootstrap navbar, and tweaked the colors and placement of some
elements to make it look how I wanted. I also made it dynamically display
options available to the user based on whether or not they were logged in.
Because the Dice Roller is available without a user account, that is always on
the navbar. The HP Tracker, on the other, needs an account, so that is only
present when a user is logged in.
