from .base_dao import BaseDao
from model.produtos_classe import ProdutosClasse


class ProdutosDao(BaseDao):

    def inserir_frutas(self, frutas, preco):
        comando_sql_insert = f"""INSERT INTO produto (produto, preco, fk_tipo_produto)
        VALUES('{frutas}','{preco}',2)"""

        return super().inserir(comando_sql_insert)

    def inserir_verduras(self, verduras, preco):
        comando_sql_insert = f"""INSERT INTO produto (produto, preco, fk_tipo_produto)
        VALUES('{verduras}','{preco}',1)"""

        return super().inserir(comando_sql_insert)

    def inserir_legumes(self, legumes, preco):
        comando_sql_insert = f"""INSERT INTO produto (produto, preco, fk_tipo_produto)
        VALUES('{legumes}','{preco}',3)"""

        return super().inserir(comando_sql_insert)

    def existe_produto(self, produto_nome):
        comando_sql_buscar_id = f"""SELECT * FROM produto WHERE produto LIKE '%{produto_nome}%' LIMIT 1
        """
        verific = super().buscar_por_id(comando_sql_buscar_id)
        if verific:
            return True
        else:
            return False
