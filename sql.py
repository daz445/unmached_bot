import sqlite3#aiosqlite
from config import db_path 
conn =  sqlite3.connect(db_path,check_same_thread=False)
cursor = conn.cursor()

#Создает изначалную структуру базы 
def new_import_player():
	for x in open("./sourse/person.txt",encoding="utf-8").read().split("\n"):
		name_hero, player = x.split(", ")
		cursor.execute(f"INSERT INTO users (player, name_hero) VALUES (?,?)", (player,name_hero))
		conn.commit()
#Создает изначалную структуру базы 
def new_import_map():
	for x in open("./sourse/map.txt",encoding="utf-8").read().split("\n"):
		name_hero, player = x.split(", ")
		cursor.execute(f"INSERT INTO map (player, name_hero) VALUES (?,?)", (player,name_hero))
		conn.commit()
		

#Получаем всех персонажей по имени игрока 
def get_persons_for_player(player):
  sqlite_select_query = f"""SELECT name_hero  from users WHERE player = '{player}'"""
  cursor.execute(sqlite_select_query)
  return [x[0] for x in cursor.fetchall()]

#Получаем всех персонажей кто есть в базе 
def get_all_persons():
  sqlite_select_query = f"""SELECT DISTINCT player from users """
  cursor.execute(sqlite_select_query)
  return [x[0] for x in cursor.fetchall()]

#Получаем все карты персонажа кто есть в базе 
def get_all_maps(player):
  sqlite_select_query = f"""SELECT DISTINCT name_hero from map WHERE player = '{player}'"""
  cursor.execute(sqlite_select_query)
  return [x[0] for x in cursor.fetchall()]