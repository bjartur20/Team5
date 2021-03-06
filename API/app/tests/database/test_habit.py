import pytest

from main.services.db_api import DBapi
from main.util.mappers.habitmapper import HabitMapper
from tests.database.test_base import TestBase

class TestHabitDB(TestBase):
    def test_get_single_habit(self):
        assert len(DBapi.habits.get(1)) == 1

    def test_get_habit_list(self):
        assert len(DBapi.habits.get()) == 4
    
    def test_get_habit_by_user(self):
        assert len(DBapi.habits.get(user_id=2)) == 1

    def test_post_habit(self):
        self.begin()
        new_habit = HabitMapper(userid=1, name="Test habit", description="My test habit", measurementid=4)
        DBapi.habits.post(new_habit)
        assert len(DBapi.habits.get()) == 5
        self.rollback()

    def test_put_habit(self):
        self.begin()
        updated_habit = HabitMapper(name="TEST")
        DBapi.habits.put(1, updated_habit)
        assert DBapi.habits.get(1)[0].name == "TEST"
        self.rollback()

    def test_delete_habit(self):
        self.begin()
        DBapi.habits.delete(2)
        assert len(DBapi.habits.get()) == 3
        self.rollback()

    """
    def test_exceptions_type(self):
        with pytest.raises(Exception, match="Missing data"):
            DBapi.habits("POST")
        with pytest.raises(Exception, match="Missing data"):
            DBapi.habits("PUT", 1)
        with pytest.raises(Exception, match="Missing id"):
            DBapi.habits("PUT")
        with pytest.raises(Exception, match="Missing id"):
            DBapi.habits("DELETE")
        with pytest.raises(Exception, match="Method not in list of approved methods: GET, POST, PUT, DELETE"):
            DBapi.habits("test")"""
