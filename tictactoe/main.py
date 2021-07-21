from tictactoe.Tictactoe import *
from database.connection import *
from tictactoe.database.dao.ObjectDao import ObjectDao

init_db()
ObjectDao.clear_database()
for i in range(0, 5):
    result = play_game_ttt()
    print(result)
