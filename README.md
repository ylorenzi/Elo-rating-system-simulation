# Elo-rating-system-simulation

> This code was developed for my dissertation for obtaining the title of Master in Economics for the University of Santa Catarina.

## 1 - Introduction

The Elo rating system is a statistical method that aims to estimate player ability. It was developed by the physicist Arpad Elo for chess, and nowadays it´s widely used in sports and multiplayer online games. One of the main advantages from Elo is that it is very intuitive. If you win you gain rating points and if you lose you lose rating points.

However, in online games, some players perceive the Elo system as unfair because it's increadible hard to increase their rating. At first glance, it may seem ilogical, since if your rating is below what is should've been, you should be winning (on average) most of your games until your rating converges to it's "true" value. But since this perception is so widespread, it motivated me to develop this project and test if the hypotesis of a player being stuck with a rating lower than his skill could be explained by behavorial economics.  

## Elo rating system formulas

If you ever played an competitive online game you might have heard about the Elo rating system. It's a statistical method that aims to estimate player ability. It was originally developed for chess and has become one of the main methods of estimating competitor skills in various sports.

The Elo system consists of two formulas. The first one is the expected score of player A (with rating ra)  against player B (with rating rb):

<a href="https://www.codecogs.com/eqnedit.php?latex=\huge&space;S_{exp}&space;=\frac{1}{1&plus;10^{-(r_a-r_b)/400}}." target="_blank"><img src="https://latex.codecogs.com/gif.latex?\huge&space;S_{exp}&space;=\frac{1}{1&plus;10^{-(r_a-r_b)/400}}." title="\huge S_{exp} =\frac{1}{1+10^{-(r_a-r_b)/400}}." /></a>

This is a probability so it´s value is between 0 and 1. Also, the expected score of player A plus the expected score of player B is always equals to 1. The higher the rating of player A, the higher is the expected score.

When two players face each other, the winner has a Score S=1 and the looser's score is S=0. In the case of a tie both players's score is S = 0.5

The second formula of the system is the following:

<a href="https://www.codecogs.com/eqnedit.php?latex=\huge&space;r_{post}&space;=r_{pre}&space;&plus;&space;K(S-&space;S_{exp})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\huge&space;r_{post}&space;=r_{pre}&space;&plus;&space;K(S-&space;S_{exp})" title="\huge r_{post} =r_{pre} + K(S- S_{exp})" /></a>

where rpost is the rating after the game, rpre is the rating before the game and S is the score of the game.
