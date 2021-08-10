# Elo-rating-system-simulation 

$x^2 +10$
  

> This code was developed for my dissertation for obtaining the title of Master in Economics from the University of Santa Catarina. 

  

Table of contents: 

  

- [1- Introduction](#1--introduction) 

  * [1.1- The math behind the Elo system](#11--the-math-behind-the-elo-system) 

  * [1.2- Elo rating system formulas](#12--elo-rating-system-formulas) 

  

- [2- Simulation](#2--simulation) 

  

## 1- Introduction 

  

The Elo rating system is a statistical method that aims to estimate player ability. It was developed by the physicist Arpad Elo for chess, and nowadays it´s widely used in sports and multiplayer online games. One of the main advantages from Elo is that it is very intuitive. If you win you gain rating points and if you lose you lose rating points. 

Beating higher rated opponents rewards more points than lower rated ones. And losing to lower rated opponents subtracts more points than losing to higher rated ones.  

  

However, in online games, some players perceive the Elo system as unfair because it's incredibly hard to increase their rating. At first glance, it may seem illogical, since if your rating is below what is should've been, you should be winning (on average) most of your games until your rating converges to its "true" value. But since this perception is so widespread, it motivated me to develop this project and test if the hypothesis of a player being stuck with a rating lower than his skill could be explained by behavioral economics.   

  

## 1.1- The math behind the Elo system 

  

Glickman (1995) presents an intuitive explanation of what is the logic behind the Elo system. Suppose that in a game of chess, instead of the two players actually playing the game, both of them bring boxes with pieces of papers, each one with a number written on them. Both players randomly draw a piece from their boxes and the player with the highest number wins. 

  

## 1.2- Elo rating system formulas 

  

If you ever played a competitive online game, you might have heard about the Elo rating system. It's a statistical method that aims to estimate player ability. It was originally developed for chess and has become one of the main methods of estimating competitor skills in various sports. 

  

The Elo system consists of two formulas. The first one is the expected score of player A (with rating ra) against player B (with rating rb): 

  

<a href="https://www.codecogs.com/eqnedit.php?latex=\huge&space;S_{exp}&space;=\frac{1}{1&plus;10^{-(r_a-r_b)/400}}." target="_blank"><img src="https://latex.codecogs.com/gif.latex?\huge&space;S_{exp}&space;=\frac{1}{1&plus;10^{-(r_a-r_b)/400}}." title="\huge S_{exp} =\frac{1}{1+10^{-(r_a-r_b)/400}}." /></a> 

  

This is a probability so it´s value is between 0 and 1. Also, the expected score of player A plus the expected score of player B is always equals to 1. The higher the rating of player A, the higher is the expected score. 

  

When two players face each other, the winner has a Score S=1 and the loser's score is S=0. In the case of a tie both players's score is S = 0.5 

  

The second formula of the system is the following: 

  

<a href="https://www.codecogs.com/eqnedit.php?latex=\huge&space;r_{post}&space;=r_{pre}&space;&plus;&space;K(S-&space;S_{exp})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\huge&space;r_{post}&space;=r_{pre}&space;&plus;&space;K(S-&space;S_{exp})" title="\huge r_{post} =r_{pre} + K(S- S_{exp})" /></a> 

  

where rpost is the rating after the game, rpre is the rating before the game and S is the score of the game. 

  

### An example of rating change 

  

- Player A has a rating of 1700 

- Player B has a rating of 1500 

- Suppose K=100 in order to facilitate the calculation 

  

Their expected scores are: 

  

<a href="https://www.codecogs.com/eqnedit.php?latex=\huge&space;S^a_{exp}&space;=\frac{1}{1&plus;10^{-(1700-1500)/400}}&space;\approx&space;0.76" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\huge&space;S^a_{exp}&space;=\frac{1}{1&plus;10^{-(1700-1500)/400}}&space;\approx&space;0.76" title="\huge S^a_{exp} =\frac{1}{1+10^{-(1700-1500)/400}} \approx 0.76" /></a> 

  

<a href="https://www.codecogs.com/eqnedit.php?latex=\huge&space;S^b_{exp}&space;=\frac{1}{1&plus;10^{-(1500-1700)/400}}&space;\approx&space;0.24" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\huge&space;S^b_{exp}&space;=\frac{1}{1&plus;10^{-(1500-1700)/400}}&space;\approx&space;0.24" title="\huge S^b_{exp} =\frac{1}{1+10^{-(1500-1700)/400}} \approx 0.24" /></a> 

  

If Player A wins the the new rating will be: 

- Player A = 1700 + 100 x (1 - 0.76) = 1724 

- Player B = 1500 + 100 x (0 - 0.24) = 1476 

  

If Player B wins the the new rating will be: 

- Player A = 1700 + 100 x (0 - 0.76) = 1624 

- Player B = 1500 + 100 x (1 - 0.24) = 1576 

  

## 2- Simulation 

  

The first step of the simulation is determining how is the simulation of a single match. It was chosen a very simple method. Following the Glickman (1995) analogy, in a match, the performance of a player is a randomly generated number. The player with the highest number is declared the winner. The distribution from which the number is generated is a Normal distribution, with mean equal the skill of the player and variance equal to the player variance. This means that players with higher skill will, on average, generate higher numbers, and consequently, win more games.  

Mathematically, the performance of player i in match j  is: 

<a href="https://www.codecogs.com/eqnedit.php?latex=\huge&space;P_{ij}&space;\sim&space;N(H_i,\sigma_i^2)." target="_blank"><img src="https://latex.codecogs.com/gif.latex?\huge&space;P_{ij}&space;\sim&space;N(H_i,\sigma_i^2)." title="\huge P_{ij} \sim N(H_i,\sigma_i^2)." /></a> 

In the simulated environment there are N players with normally distributed skill. The players have different variances, which come from a uniform distribution. The players are separated in d divisions accordingly to their rating. Suppose 1000 players and 5 divisions. The first division will have de 200 highest rated players, the second division will have the following 200 and so on. The division system prevents having the best players having to face the bottom players, which is a common practice to avoid completely one-sided matches.  

## 2.1- Measuring errors 

The whole point of the simulation is to find out if the Elo system is an efficient way of classifying players according to skill. The used to measure the error of rating is the following: 

<a href="https://www.codecogs.com/eqnedit.php?latex=\huge&space;error_i&space;=&space;A_i&space;-&space;r_i" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\huge&space;error_i&space;=&space;A_i&space;-&space;r_i" title="\huge error_i = A_i - r_i" /></a> 

where Ai and ri are the ability (skill) and rating of player i. So, the closer the rating to the true ability of the player, the better is the estimate the Elo estimate.  

Now that we presented the error of a single player, we can show the metrics to evaluate the Elo system as a whole. To do so, we use some equations. Firstly, the mean error: 

<a href="https://www.codecogs.com/eqnedit.php?latex=\huge&space;ME&space;=&space;\frac{1}{N}&space;\sum_{i=1}^{N}&space;error_i." target="_blank"><img src="https://latex.codecogs.com/gif.latex?\huge&space;ME&space;=&space;\frac{1}{N}&space;\sum_{i=1}^{N}&space;error_i." title="\huge ME = \frac{1}{N} \sum_{i=1}^{N} error_i." /></a>   

It’s not a good way to measure errors since positive error will cancel out negative ones, but it can indicate if there are, on average, more of one kind of errors.  

The second metric to evaluate the model is the mean absolute error: 

<a href="https://www.codecogs.com/eqnedit.php?latex=\huge&space;MAE&space;=&space;\frac{1}{N}&space;\sum_{i=1}^{N}&space;|error_i|." target="_blank"><img src="https://latex.codecogs.com/gif.latex?\huge&space;MAE&space;=&space;\frac{1}{N}&space;\sum_{i=1}^{N}&space;|error_i|." title="\huge MAE = \frac{1}{N} \sum_{i=1}^{N} |error_i|." /></a> 

Which solves the cancel out problem of the previous metric.  

