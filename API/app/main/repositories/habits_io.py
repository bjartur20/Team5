from main.repositories.abc_table import AbcTable
from main.util.mappers.habit import Habit
from psycopg2.extensions import AsIs  # Used to remove '' from SQL strings I insert


class Habitsio(AbcTable):
    """
        An input-output class for the habits table in the Habit tracker database.
        Contains methods for each CRUD operation [GET, POST, PUT, DELETE]
    """

    @classmethod
    def get(cls, habit_id):
        """ Takes in an int. Returns row from habits with set id or all rows if id=None as list of Habit objects"""
        if habit_id:
            super()._cur.execute("SELECT * FROM habits WHERE habitid = %s;", (habit_id,))
        else:
            super()._cur.execute("SELECT * FROM habits;")

        habits_list = []
        for habit_info in super()._cur.fetchall():
            habit = Habit(*habit_info)
            habits_list.append(habit)

        return habits_list

    @classmethod
    def post(cls, data):
        """ Takes in a Habit object and saves it to the database. Returns nothing """
        habit_tuple = data.to_sql_insert()
        super()._cur.execute("INSERT INTO habits %s VALUES %s;", (AsIs(habit_tuple[0]), AsIs(habit_tuple[1])))

    @classmethod
    def put(cls, habit_id, data):
        """
        Takes in an int and a Habit object with changes and updates
        those columns in the database. Returns nothing
        """
        habit_str = data.to_sql_update()
        super()._cur.execute("UPDATE habits SET %s WHERE habitid = %s", (AsIs(habit_str), habit_id))

    @classmethod
    def delete(cls, habit_id):
        """ Takes in an int. Deletes row with that id from the database. Returns nothing """
        super()._cur.execute("DELETE FROM habits WHERE habitid = %s;", (habit_id,))
