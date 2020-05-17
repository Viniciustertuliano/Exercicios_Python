
import sqlalchemy
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

engine = sqlalchemy.create_engine("sqlite:///serve.db")
connection = engine.connect()

Base = declarative_base(engine)
session = Session()

# creação da tabela autor
connection.execute(""" CREATE TABLE IF NOT EXISTS AUTOR(
                       ID INTEGER PRIMARY KEY,
                       NOME VARCHAR(40) NOT NULL)
                  """)


connection.execute(""" CREATE TABLE IF NOT EXISTS LIVRO(
                       ID INTEGER PRIMARY KEY,
                       TITULO CHAR(30) NOT NULL,
                       PAGINAS INT NOT NULL,
                       AUTOR_ID INT NOT NULL)
                  """)


# MAPEAMENTO DA TABLE
class Autor(Base):
    __tablename__ = 'AUTOR'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(40))

    def __init__(self, nome):
        self.nome = nome


class Livro(Base):
    __tablename__ = 'LIVRO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    titulo = Column('TITULO', String(30))
    paginas = Column('PAGINAS', Integer)
    autor_id = Column('AUTOR_ID', Integer)

    def __init__(self, titulo, paginas: int, autor_id: int):
        self.titulo = titulo
        self.paginas = paginas
        self.autor_id = autor_id


autor1 = Autor('Gabriela de jesus')
autor2 = Autor('Ferrez')
autor3 = Autor('Yuval Harari')
autores = [autor1, autor2, autor3]
session.add_all(autores)
session.commit()

livro1 = Livro('Quarto de Despejo - Diário de uma Favelada', 173, autor1.id)
livro2 = Livro('Capão Pecado', 160, autor2.id)
livro3 = Livro('Os ricos também morrem', 190, autor2.id)
livro4 = Livro('Sapiens - Uma Breve História da Humanidade', 443, autor3.id)
livros = [livro1, livro2, livro3, livro4]
session.add_all(livros)
session.commit()


aut = session.query(Autor).all()
liv = session.query(Livro).all()
print('-'*30)
for i in aut:
    print('ID:{}\nNome:{}\n'.format(i.id, i.nome))
print('-'*30)
for l in liv:
    print('ID_LIVRO:{}\nTITULO:{}\nPAGINAS:{}\nID_AUTOR:{}\n'.format(
        l.id, l.titulo, l.paginas, l.autor_id))
