#Elo single player

import math
import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import norm, gaussian_kde
from scipy.stats import shapiro

# seed=123
seed = 1
np.random.seed(seed)
random.seed(seed)


K_FACTOR_PLACEMENTS = 100
K_FACTOR = 20
DIVIDER = 400
STARTING_ELO = 1500
nb_players = 1000
nb_games = 500_000
nb_placements = 30 



class Player(object):
    """
    Represents a player, its skill and its current elo points 
    """

    def __init__(
        self,
        name,
        skill,
        var,
        elo=STARTING_ELO,
        k_factor=K_FACTOR_PLACEMENTS,
    ):
        self.name = name
        self.skill = skill
        self.elo = elo
        self.var = var
        self.k_factor = k_factor
        self.elo_history = [elo]

    def __repr__(self):
        s = "Player name : {}, actual skill = {} elo rating {}".format(
            self.name, self.skill, self.elo
        )
        return s



    def expected_result(self, other):
        """Returns the ELO expected value of the match against an other player (0 means a guaranteed loss, 1 means a guaranteed win)
        
        Arguments:
            other {Player} -- The second player
        """
        return float(1) / (1 + math.pow(10, float(other.elo - self.elo) / DIVIDER))

    def real_result(self, other):
        """Returns the REAL expected value of the match against an other player (0 means a guaranteed loss, 1 means a guaranteed win)
        
        Arguments:
            other {Player} -- The second player
        """
        self_in_game_skill = np.random.normal(self.skill,self.var)
        other_in_game_skill = np.random.normal(other.skill,other.var)
        if self_in_game_skill >  other_in_game_skill:
            return 1
        else:
            return 0
    
    
    def play(self, other):
        """Returns the result (0 if loss, 1 if won) of a game against an other player 
        
        Arguments:
            other {Player} -- The second player
        """
        return self.real_result(other)
            
    
    
    def play_and_update(
        self, other, verbose=False
    ):
        """Plays against an other player and updates both elo ratings depending on the output of the match

        Arguments:
            other {Player} -- Other player

        Keyword Arguments:
            verbose {bool} -- More prints (default: {False})
        """
        if len(self.elo_history) <= nb_placements:
            self.k_factor = K_FACTOR_PLACEMENTS
        else:
            self.k_factor = K_FACTOR
        
        
        if len(other.elo_history) <= nb_placements:
            other.k_factor = K_FACTOR_PLACEMENTS
        else:
            other.k_factor = K_FACTOR
        
        expected = self.expected_result(other)
        result = self.play(other)
        
        squared_error = (result - expected)**2
        SE.append(squared_error)
        
        self_delta_points = self.k_factor * (result - expected)
        
        self.elo = self.elo + self_delta_points
        self.elo_history.append(self.elo)
        
        other_delta_points = other.k_factor * (result - expected)
        other.elo = other.elo - other_delta_points
        other.elo_history.append(other.elo)

        if verbose:
            print(
                "{} vs {}. Expected by skill={}, expected by elo={}, result={}, delta_points={} \n".format(
                    self.name,
                    other.name,
                    float(1) / (1 + math.pow(10, float(other.skill - self.skill) / DIVIDER)),
                    expected,
                    result,
                    self_delta_points,
                )
            )
    def as_dict(self, seed):
        return {'name': self.name, 'skill': self.skill, 'var': self.var,
                'elo': self.elo, "erro": self.skill - self.elo,
                "games":len(self.elo_history)-1, "seed": seed}                   

# players = []
# for i in range(nb_players):
#     skill = int(np.random.normal(1500,500))
#     var = random.randint(1,400)
#     # var = 200
#     players.append(
#             Player("Elo of PlayerSkill(" + str(skill) + ")", skill, var)
#         )

# # for games in range(nb_games):
# #     duelo = random.sample(range(nb_players), 2)
# #     players[duelo[0]].play_and_update(players[duelo[1]],False)

# d = 5 #number of divisions
# for games in range(int(nb_games/d)):
    
#     players =sorted(players, key=lambda player: player.elo) 
#     i=0
#     while i <= d-1:
        
#         duelo = random.sample(range(int(i*nb_players/d),int((i+1)*nb_players/d)  ), 2)    
#         players[duelo[0]].play_and_update(players[duelo[1]],False)
#         i+= 1
        
# players =sorted(players, key=lambda player: player.elo)

# df = pd.DataFrame([x.as_dict(seed) for x in players])


# plt.hist(df["skill"], bins=100, edgecolor="black" )
# plt.ylabel("número de jogadores")
# plt.xlabel("habilidade")
# plt.savefig('single.skill.hist.png', bbox_inches='tight', pad_inches=0)
# plt.show()

# plt.hist(df["elo"], bins=100, edgecolor="black" )
# plt.ylabel("número de jogadores")
# plt.xlabel("rating Elo")
# plt.savefig('single.elo.hist.png', bbox_inches='tight', pad_inches=0)
# plt.show()

# plt.hist(df["erro"], bins=100, edgecolor="black" )
# plt.ylabel("número de jogadores")
# plt.xlabel("erro")
# plt.savefig('single.erro.hist.png', bbox_inches='tight', pad_inches=0)
# plt.show()

# # plt.hist(df["games"], bins=100, edgecolor="black" )
# # plt.show()



# print(np.mean(df["erro"]))
# print(np.std(df["erro"]))
# print(sum(abs(df["erro"]))/nb_players)
# print(sum(df["erro"]**2)/nb_players)
# MSE = np.mean(SE)
# RMSE = MSE **(1/2)
# print(RMSE)

# # normality test
# stat, p = shapiro(df["erro"])
# print('Statistics=%.3f, p=%.3f' % (stat, p))
# # interpret
# alpha = 0.05
# if p > alpha:
#  	print('Sample looks Gaussian (fail to reject H0)')
# else:
#  	print('Sample does not look Gaussian (reject H0)')


nb_seeds = 100
column_names = ["name","skill","var","elo","erro","games","seed"]
RMSE=[]
all_df = pd.DataFrame(columns= column_names)
for seed in range(1,nb_seeds+1):
    np.random.seed(seed)
    random.seed(seed)
    SE=[]
    
    players = []
    for i in range(nb_players):
        skill = int(np.random.normal(1500,500))
        var = random.randint(1,400)
        # var = 200
        players.append(
                Player("Elo of PlayerSkill(" + str(skill) + ")", skill, var)
            )
    
    
    d = 5 #number of divisions
    for games in range(int(nb_games/d)):
        
        players =sorted(players, key=lambda player: player.elo) 
        i=0
        while i <= d-1:
            
            duelo = random.sample(range(int(i*nb_players/d),int((i+1)*nb_players/d)  ), 2)    
            players[duelo[0]].play_and_update(players[duelo[1]],False)
            i+= 1
            
    players =sorted(players, key=lambda player: player.elo)
    MSE = np.mean(SE)
    RMSE.append(MSE **(1/2))
    
    df = pd.DataFrame([x.as_dict(seed) for x in players])
    all_df = pd.concat([df,all_df])

# teste = all_df.loc[all_df["seed"]==1]

erros = []
for e in range(1,nb_seeds+1):
    df_seed = all_df.loc[all_df["seed"]==e]
    EM = sum(df_seed["erro"])/nb_players
    EMSTD = np.std(df_seed["erro"])
    EAM = sum(abs(df_seed["erro"]))/nb_players
    EQM = sum(df_seed["erro"]**2)/nb_players
    erros.append([e,EM,EMSTD,EAM,EQM,RMSE[e-1]])

error_df = pd.DataFrame(erros, columns = ["seed","EM","EMSTD","EAM","EQM","RMSE"]) 


all_df.to_csv("single.all.df.csv", sep= ";", index=False)   
error_df.to_csv("single.error.df.csv", sep= ";", index=False)    
