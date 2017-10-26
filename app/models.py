from . import db
import pandas as pd
from flask_script import Manager, Command, Option


class Continent(db.Model):
	__tablename__ = 'CONTINENTS'
	id = db.Column(db.String(2), primary_key=True)
	name = db.Column(db.String(64), unique=True)
	countries = db.relationship('Country', backref='continent')

	def __repr__(self):
		return '<Continent %r' %self.name

class Country(db.Model):
	__tablename__ = 'COUNTRIES'
	id = db.Column(db.String(2), primary_key=True)
	continent_id = db.Column(db.String(2), db.ForeignKey('CONTINENTS.id'), nullable=False)
	name = db.Column(db.String(64))
	cities = db.relationship('City', backref='country')

	def __repr__(self):
		return '<Country %r' %self.name

class City(db.Model):
	__tablename__ = 'CITIES'
	id = db.Column(db.Integer, primary_key=True)
	ascii_name = db.Column(db.String(80))
	lat = db.Column(db.Float)
	lon = db.Column(db.Float)
	country_code = db.Column(db.String(2), db.ForeignKey('COUNTRIES.id'), nullable=False)
	population = db.Column(db.Integer)
	elevation = db.Column(db.Float)


	def __repr__(self):
		return '<City %r' %self.name

#Adding data to the database
class add_data_from_csv(Command):
	#Can be used to add arguments
	# option_list = (
	# 	Option('--filename', '-fn', dest='filename'),
	# 	)

	def run(self):

		df_cont = pd.read_csv('Raw_data/Continents.csv', header=None, na_filter=False)
		df_coun = pd.read_csv('Raw_data/Countries.csv', header=None, na_filter=False)
		df_city = pd.read_csv('Raw_data/Cities.csv', header=None, na_filter=False)
		# Either add in the same column names as a fall back or see below
		df_cont.columns = ['id','name']
		df_coun.columns = ['id', 'continent_id', 'name']
		df_city.columns = ['id', 'ascii_name', 'lat', 'lon', 'country_code', 'population', 'elevation']
		df_city = df_city.sort_values('population')
		df_city = df_city[df_city.population > 100000]

		# Use the model to insert data iteratively
		df_cont.to_sql(con=db.engine, name=Continent.__tablename__, if_exists='append', index=False)
		df_coun.to_sql(con=db.engine, name=Country.__tablename__, if_exists='append', index=False)
		df_city.to_sql(con=db.engine, name=City.__tablename__, if_exists='append', index=False)
