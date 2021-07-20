from tictactoe.Tictactoe import *
from database.connection import *
from tictactoe.database.dao.TurnDao import TurnDao

init_db()
result = play_game_ttt()
print(result)
TurnDao.delete_all()
