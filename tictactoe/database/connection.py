import mongoengine


def init_db():
    mongoengine.connect(host="mongodb://127.0.0.1:27017/ml_tictactoe")
