from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa

Base = declarative_base()

class Word(Base):
	__tablename__ = 'word'
	
	word_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
	
	en = sa.Column(sa.Text)
	ru = sa.Column(sa.Text)
	type = sa.Column(sa.Integer)

class Template(Base):
	__tablename__ = 'template'
	
	template_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
	
	template = sa.Column(sa.Text)
	type = sa.Column(sa.Integer)
	
	