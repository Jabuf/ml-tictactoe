from datetime import datetime

from database.connection import *
from tictactoe.database.dao.ObjectDao import ObjectDao
from tictactoe.database.dao.ResultDao import ResultDao
from tictactoe.Tictactoe import *

init_db()
ObjectDao.clear_database()
now = datetime.today()
for i in range(0, 50):
    result = play_game_ttt()
print(ResultDao.get_stats_game_states(now))

# List of games won by player 1
results = ResultDao.get_results_by_game_states(PLAYER1)

now = datetime.today()
for i in range(0, 50):
    result = play_game_ttt(results)

print(ResultDao.get_stats_game_states(now))
