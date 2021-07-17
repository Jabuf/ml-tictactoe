from tictactoe.Tictactoe import *
from database.connection import *

init_db()
result = play_game_ttt()
print(result)
