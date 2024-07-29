from peewee import *

db = SqliteDatabase('Lista_tarefas.db')

class BaseModel(Model):
    class Meta:
        database = db


class Tarefa(BaseModel):
    Nome = CharField(max_length=250)
    Prazo = DateTimeField()
    Status = CharField(default="Pendente")

def conectar_banco():
    db.connect()
    db.create_tables([Tarefa])
