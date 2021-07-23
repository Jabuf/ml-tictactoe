import matplotlib.pyplot as plt

from database.connection import *
from tictactoe.database.dao.ObjectDao import ObjectDao
from tictactoe.database.dao.ResultDao import ResultDao
from tictactoe.database.dao.SessionDao import SessionDao
from tictactoe.database.entity.Session import Session
from tictactoe.Tictactoe import *

init_db()
ObjectDao.clear_database()

sample_number = 100
training_iteration = 10
winning_games = []

for i in range(0, training_iteration):
    start = datetime.today()
    session = Session(training_iteration=i, pool_successful_games=len(winning_games))
    for j in range(0, sample_number):
        play_game_ttt(session, winning_games)
    end = datetime.today()
    # winning_games = ResultDao.get_results_by_sessions_game_states(
    #     SessionDao.get_sessions_by_training_iteration(i), PLAYER2)
    session.execution_time = (end - start).microseconds / 1000
    session.save()
    winning_games = ResultDao.get_all_results_by_game_states(PLAYER2)

results = SessionDao.get_stats()
print(results)

draws = []
player1_victories = []
player2_victories = []

for i, x in enumerate(results):
    draws.append(x[1][DRAW][1])
    player1_victories.append(x[1][PLAYER1][1])
    player2_victories.append(x[1][PLAYER2][1])

plt.plot(draws, 'red', player1_victories, 'green', player2_victories, 'blue')
plt.legend(['DRAW', 'PLAYER1', 'PLAYER2'])
plt.show()
