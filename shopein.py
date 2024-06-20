# Importando o conector MySQL para Python
import mysql.connector

# Definição da classe Produto para representar um produto
class Produto:
    def __init__(self, nome, codigobar, preco, descricao):
        self.nome = nome              # Atributo: nome do produto
        self.codigobar = codigobar    # Atributo: código de barras do produto
        self.preco = preco            # Atributo: preço do produto
        self.descricao = descricao    # Atributo: descrição do produto

class pedidos:
    def _init_(self,codigobar):
        self.codigobar=codigobar
        

# Definição da classe Cliente para representar um cliente
class Cliente:
    def __init__(self, nome, email, endereco, telefone):
        self.nome = nome          # Atributo: nome do cliente
        self.email = email        # Atributo: email do cliente
        self.endereco = endereco  # Atributo: endereço do cliente
        self.telefone = telefone  # Atributo: telefone do cliente


# Definição da classe SistemaDeCompras para interagir com o banco de dados e gerenciar produtos e clientes
class SistemaDeCompras:
    def __init__(self):
        # Conectando ao banco de dados MySQL
        self.conexao = mysql.connector.connect(
            host="localhost",       # Host onde está o servidor MySQL
            user="root",            # Usuário do banco de dados
            password="he182555@",   # Senha do usuário
            database="commerce_db"  # Nome do banco de dados
        )
        self.cursor = self.conexao.cursor()  # Criando um cursor para executar comandos SQl
    # Método para adicionar um produto ao banco de dados.

    def adicionar_produto(self, produto):
        sql = "INSERT INTO produtos (nome, codigobar, preco, descricao) VALUES (%s, %s, %s, %s)"
        valores = (produto.nome, produto.codigobar, produto.preco, produto.descricao)
        self.cursor.execute(sql, valores,)  # Executando o comando SQL para inserção
        self.conexao.commit()
    # Método para adicionar um cliente ao banco de dados

    def adicionar_cliente(self, cliente):
        sql = "INSERT INTO cliente (nome, email, endereco, telefone) VALUES (%s, %s, %s, %s)"
        valores = (cliente.nome, cliente.email, cliente.endereco, cliente.telefone)
        self.cursor.execute(sql, valores)  # Executando o comando SQL para inserção
        self.conexao.commit()

    # Método para listar todos os produtos cadastrados no banco de dados
    def listar_produtos(self):
        self.cursor.execute('SELECT nome, codigobar, preco, descricao FROM produtos')
        produtos = self.cursor.fetchall()  # Obtendo todos os produtos do banco de dados
        for produto in produtos:
            # Imprimindo informações de cada produto
            print(f"Nome: {produto[0]}, Código de Barras: {produto[1]}, Preço: {produto[2]}, Descrição: {produto[3]}")

    # Método para listar todos os clientes cadastrados no banco de dados
    def listar_cliente(self):
        self.cursor.execute('SELECT nome, email, endereco, telefone FROM cliente')
        clientes = self.cursor.fetchall()  # Obtendo todos os clientes do banco de dados
        for cliente in clientes:
            # Imprimindo informações de cada cliente
            print(f"Nome: {cliente[0]}, Email: {cliente[1]}, Endereço: {cliente[2]}, Telefone: {cliente[3]}")

    # Método para fechar a conexão com o banco de dados
    def fechar_conexao(self):
        self.cursor.close()    # Fechando o cursor
        self.conexao.close()   # Fechando a conexão com o banco de dados

# Criando uma instância do SistemaDeCompras
sistema = SistemaDeCompras()

# Criando alguns produtos e um cliente
nome = input("digite o nome do produti: ")
codigobar = input("digite o codigo de barra: ")
preco= float(input('digite o preço: '))
descricao = input('digite a descriçao: ')

produto03 = Produto(f'seu nome:{nome}', f'seu codigo de barra {codigobar}', f'seu preço:{preco}',f'sua descriçao:{descricao}')

nome = input("digite seu nome: ")
email = input("digite seu email: ")
endereco= input('digite seu endereco: ')
telefone = input('digite o seu telefone ')

cliente01= Cliente(f'seu nome:{nome}', f'seu email: {email}', f'seu endereço:{endereco}',f'seu telefone:{telefone}')
# Adicionando os produtos e cliente ao banco de dados

sistema.adicionar_produto(produto03)
print("produto adicionado com sucesso")

sistema.adicionar_cliente(cliente01) 
print('cliente adicionado com sucesso')
# Imprimindo o catálogo de produtos

print('Catálogo de Produtos:')
sistema.listar_produtos()

# Imprimindo a lista de clientes
print('Lista de Clientes:')
sistema.listar_cliente()
# Fecha
