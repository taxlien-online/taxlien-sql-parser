import mysql.connector # type: ignore
import csv
from config import DB_CONFIG, VIEW_NAMES

db_config = DB_CONFIG

view_names = VIEW_NAMES

for view_name in view_names:
	try:
			connection = mysql.connector.connect(**db_config)
			cursor = connection.cursor()

			query = f"SELECT * FROM {view_name}"
			cursor.execute(query)

			rows = cursor.fetchall()
			columns = [desc[0] for desc in cursor.description]

			with open(f'output/{view_name}.csv', 'w', newline='') as file:
					writer = csv.writer(file)
					writer.writerow(columns)
					writer.writerows(rows)

			print(f"Данные успешно экспортированы в {view_name}.csv")

	except mysql.connector.Error as err:
			print(f"Ошибка: {err}")
	finally:
			if connection.is_connected():
					cursor.close()
					connection.close()
					print("Подключение к MySQL закрыто")