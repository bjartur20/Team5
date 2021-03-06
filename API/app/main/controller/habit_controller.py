from flask import request
from flask_restplus import Resource
from werkzeug.exceptions import BadRequest, NotFound

from main.util.DTO.error_message import error_message
from main.util.mappers.habitmapper import HabitMapper
from main.util.DTO.habit_dto import HabitDTO
from main.util.DTO.record_dto import RecordDTO
from main.services.db_api import DBapi

api = HabitDTO.api
_expect = HabitDTO.expect_model
_habit = HabitDTO.model
_record = RecordDTO.model


@api.route('')
class HabitList(Resource):
    @api.doc('List all habits')
    @api.marshal_list_with(_habit, envelope='habits')
    def get(self):
        data = DBapi.habits.get()

        habit_list = []
        for habit in data:
            habit_list.append(habit.to_dict())

        return habit_list

    @api.response(201, 'Habit successfully created.')
    @api.doc('create a new Habit')
    @api.expect(_expect, validate=True)
    def post(self):
        data = request.json
        habit = HabitMapper()
        habit.set_dict(data)
        return DBapi.habits.post(habit)


@api.route('/<int:habit_id>')
@api.response(400, "BadRequest", error_message)
@api.response(404, 'Habit not found.', error_message)
class SingleHabit(Resource):
    @api.doc('Get a single habit')
    @api.marshal_with(_habit)
    def get(self, habit_id):
        check_id(habit_id)

        data = DBapi.habits.get(habit_id)
        habit_dict = data[0].to_dict()
        return habit_dict

    @api.response(201, 'Habit successfully updated.')
    @api.doc('Edit a habit')
    @api.expect(_expect, validate=True)
    def put(self, habit_id):
        check_id(habit_id)

        data = request.json
        habit = HabitMapper()
        habit.set_dict(data)
        DBapi.habits.put(habit_id, habit)

        return DBapi.habits.get(habit_id)[0].to_dict(), 201

    @api.doc('Delete a habit')
    @api.response(200, 'Habit successfully deleted.')
    def delete(self, habit_id):
        check_id(habit_id)

        DBapi.habits.delete(habit_id)
        return "", 200


@api.route("/<int:habit_id>/record")
@api.response(400, "BadRequest", error_message)
@api.response(404, 'Habit not found.', error_message)
class UserRecords(Resource):

    @api.marshal_list_with(_record, envelope='records')
    def get(self, habit_id):
        check_id(habit_id)

        data = DBapi.records.get(habit_id=habit_id)

        record_list = []
        for record in data:
            record_list.append(record.to_dict())

        return record_list


def check_id(habit_id):
    if habit_id <= 0:
        raise BadRequest("Habit id must be higher than 0")
    if not DBapi.habits.get(habit_id):
        raise NotFound(f"Habit with id {habit_id} not found")
