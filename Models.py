import Connector
from peewee import CharField


class Groups(Connector.migrator):
    group_id = CharField()
    group_name = CharField()
    user_name = CharField()

    class Meta:
        order_by = 'id'
        db_table = 'Groups_main'


class subgroups(Connector.migrator):
    subgroup_id = CharField()
    subgroup_name = CharField()
    group_name = CharField()
    user_name = CharField()

    class Meta:
        order_by = 'id'
        db_table = 'subgroups'


class cases(Connector.migrator):
    case_id = CharField()
    case_name = CharField()
    case_text = CharField()
    group_name = CharField()
    subgroup_name = CharField()
    user_name = CharField()
    datetime = CharField()

    class Meta:
        order_by = 'id'
        db_table = 'Cases'


class notes(Connector.migrator):
    note_id = CharField()
    case_text = CharField()
    user_name = CharField()
    datetime = CharField()

    class Meta:
        order_by = 'id'
        db_table = 'Notes'


class Users(Connector.migrator):
    username = CharField()

    class Meta:
        order_by = 'id'
        db_table = 'Users'


def connect_to_db():
    if not Users.table_exists():
        Users.create_table()
    if not cases.table_exists():
        cases.create_table()
    if not Groups.table_exists():
        Groups.create_table()
    if not notes.table_exists():
        notes.create_table()
    if not subgroups.table_exists():
        subgroups.create_table()
