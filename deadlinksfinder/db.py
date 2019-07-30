#!/usr/bin/env python3
# coding: utf-8
import os, flask
import sqlalchemy as sqla
from sqlalchemy.ext.declarative import declarative_base as sqla_declarative_base

Base = sqla_declarative_base()

class LinkOccurrence(Base):
	__tablename__ = 'wiki_external'
	wikipage_id = sqla.Column('wikipage_id', None, sqla.ForeignKey('wikipages.id'), primary_key=True)
	externalpage_id = sqla.Column('externalpage_id', None, sqla.ForeignKey('externalpages.id'), primary_key=True)

class WikiPage(Base):
	__tablename__ = 'wikipages'
	id = sqla.Column('id', sqla.Integer, primary_key=True)
	address = sqla.Column('address', sqla.String, nullable=False)
	exists = sqla.Column('exists', sqla.Boolean)
	is_dirty = sqla.Column('is_dirty', sqla.Boolean)
	last_check = sqla.Column('last_check', sqla.TIMESTAMP)

	links = sqla.orm.relationship('ExternalPage', secondary=wiki_external, back_populates=wiki_pages)

class ExternalPage(Base):
	__tablename__ = 'externalpages'
	id = sqla.Column('id', sqla.Integer, primary_key=True)
	address = sqla.Column('address', sqla.String, nullable=False)
	exists = sqla.Column('exists', sqla.Boolean)
	last_check = sqla.Column('last_check', sqla.TIMESTAMP)

	wiki_pages = sqla.orm.relationship('WikiPage', secondary=wiki_external, back_populates=links)

def init_session(database_path, echo_commands=False):
	# full_database_path = sqla.engine.url.URL(drivername='sqlite+pysqlite', database=database_path)
	full_database_path = 'sqlite+pysqlite:///'+database_path
	# print('full db path is "{}"'.format(full_database_path))
	engine = sqla.create_engine(full_database_path, echo=echo_commands)
	Base.metadata.create_all(engine)
	Session = sqla.orm.sessionmaker(bind=engine)
	session = Session()
	return session
