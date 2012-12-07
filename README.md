ninjaGame
=========

A game written in python 2.x

You are a Ninja in a city, run and kill your ennemies to get points

To play the game, you need to download python and the pygame library

pip install pygame should do the trick

A description of which file is used for :
	
enemy.py : handle enemy class, we can choose the speed of the enemy and its
position. The trajectory of the player seems to have only two solutions. The
enemy will never hit the player. His only way to die will in case he falls from
the platform

player.py : handle player class, we can retrieve informations such as :
		- the position of the player
		- if it is still on the platform
		- if he is jumping
		- if he is throwing a projectile or not

game.py : inherite from state class, it is the model of the application
		  You can know if the player is currently jumping or not
		  if he is throwing a shuriken.

projectile.py : handle player class, basically load the image, choose a velocity
and a position and handle the update

HighScore : handle highscore with a class where we have a static attribute,
which is a list of highscores
for HighScore.txt use json file

hud : handle informations that are displayed during the game such as :
	- fps information
	- score information
	- number of shuriken left
	- also handle combo elements

main : main file of the application, it launchs the thread loop of the state
		machine

platform : allow to create a new platform while the game keeps going

powerup : allow to create bonus image that you need to catch to get an extra
bonus. It is here only done with shiruken.

state : the main class, lots of others inherited from it. Here to handle
multiple states

surface_manager : manage surfaces

title : manage the menu of the game
