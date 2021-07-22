import matplotlib.pyplot as plt

from database.connection import *
from tictactoe.database.dao.ObjectDao import ObjectDao
from tictactoe.database.dao.ResultDao import ResultDao
from tictactoe.Tictactoe import *

init_db()
ObjectDao.clear_database()
now = datetime.today()
for i in range(0, 100):
    result = play_game_ttt()
results_1 = ResultDao.get_stats_game_states(now)

# List of games won by player 1
results = ResultDao.get_results_by_game_states(PLAYER1)

now = datetime.today()
for i in range(0, 100):
    result = play_game_ttt(results)

results_2 = ResultDao.get_stats_game_states(now)

# List of games won by player 1
results = ResultDao.get_results_by_game_states(PLAYER1)

now = datetime.today()
for i in range(0, 100):
    result = play_game_ttt(results)

results_3 = ResultDao.get_stats_game_states(now)

draw = [results_1[3][1], results_2[3][1], results_3[3][1]]
player1_victories = [results_1[1][1], results_2[1][1], results_3[1][1]]
player2_victories = [results_1[2][1], results_2[2][1], results_3[2][1]]
plt.plot(draw, 'red', player1_victories, 'green', player2_victories, 'blue')
plt.legend(['DRAW', 'PLAYER1', 'PLAYER2'])
plt.show()
