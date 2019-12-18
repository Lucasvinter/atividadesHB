import MySQLdb


class BaseDao:
    def __init__(self):
        self.conexao = MySQLdb.connect(
            host="mysql.topskills.study", database="topskills05", user="topskills05", passwd="Andrei2019")
        self.cursor = self.conexao.cursor()

    def inserir(self, comando_sql_insert):
        self.cursor.execute(comando_sql_insert)
        self.conexao.commit()

    def buscar_por_id(self, comando_sql_buscar_id):
        self.cursor.execute(comando_sql_buscar_id)
        return self.cursor.fetchone()

    def listar(self, comando_sql_listar):
        self.cursor.execute(comando_sql_listar)
        for p in self.cursor.fetchall():
            print(
                f'Produto: {p[0].capitalize()} - Preço: R${p[1]} - Tipo : {p[2]}')
