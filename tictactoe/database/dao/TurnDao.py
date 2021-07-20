from tictactoe.database.entity.Turn import Turn
from tictactoe.database.dao.ObjectDao import ObjectDao


class TurnDao(ObjectDao):
    entity = Turn

    @staticmethod
    def delete_all():
        Turn.objects.delete()
