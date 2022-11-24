import sqlite3

# connect = sqlite3.connect('informatica.db')
# c = connect.cursor()

# c.execute("CREATE TABLE historico (nome text, sobrenome text, turma text, data text, hora text)")

# connect.commit()

class Bank:
    def __init__(self, nome, sobrenome, turma, data, hora):
        
        self.nome = nome
        self.sobrenome = sobrenome
        self.turma = turma
        self.data = data
        self.hora = hora

    def config_bank(self):

        values = (self.nome, self.sobrenome, self.turma, self.data, self.hora)


        self.connect = sqlite3.connect('informatica.db')
        self.c = self.connect.cursor()

        self.c.execute('INSERT INTO historico VALUES (?, ?, ?, ?, ?)', values)

        self.connect.commit()
    
    def close_bank(self):
        self.connect.close()

