import matplotlib.pyplot as plt

from database.connection import *
from tictactoe.database.dao.ObjectDao import ObjectDao
from tictactoe.database.dao.ResultDao import ResultDao
from tictactoe.Tictactoe import *

init_db()
ObjectDao.clear_database()

sample_number = 100
iteration_number = 5
winning_games = None
results = []

for i in range(1, iteration_number):
    now = datetime.today()
    for j in range(0, sample_number):
        result = play_game_ttt(winning_games, iteration_number)
    winning_games = ResultDao.get_results_by_game_states(PLAYER1, iteration_number)
    results += [ResultDao.get_stats_game_states(now)]

print(results)

draws = []
player1_victories = []
player2_victories = []

for i, x in enumerate(results):
    draws.append(x[DRAW][1])
    player1_victories.append(x[PLAYER1][1])
    player2_victories.append(x[PLAYER2][1])

plt.plot(draws, 'red', player1_victories, 'green', player2_victories, 'blue')
plt.legend(['DRAW', 'PLAYER1', 'PLAYER2'])
plt.show()
