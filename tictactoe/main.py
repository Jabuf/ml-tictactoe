from database.connection import *
from tictactoe.database.dao.ObjectDao import ObjectDao
from tictactoe.database.dao.ResultDao import ResultDao
from tictactoe.Tictactoe import *

init_db()
ObjectDao.clear_database()
for i in range(0, 500):
    result = play_game_ttt()
print(ResultDao.get_stats_game_states())
