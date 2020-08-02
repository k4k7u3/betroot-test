import json
import psycopg2
import requests
import sys
from functools import partial

from typing import Dict, List, Union, Optional, NoReturn
from PyQt5 import Qt, QtCore
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QHBoxLayout,
                             QVBoxLayout,
                             QGridLayout,
                             QFormLayout,
                             QMainWindow,
                             QPushButton,
                             QLineEdit,
                             QLabel,
                             QMenuBar,
                             QPlainTextEdit,
                             QAction,
                             QSpacerItem,
                             QSizePolicy,
                             QGroupBox,
                             QScrollArea,
                             QScrollBar,
                             QListWidgetItem,
                             QTextEdit)

data = {}
history = []


def load_data_from_url() -> NoReturn:
    global data
    url: str = "http://api.football-data.org/v2/competitions/2021/matches"
    headers: Dict = {
        'X-Auth-Token': "e93d7e476bdf45a19d172a1fb740bf3f",
    }
    response = requests.request("GET", url, params={"dateFrom": "2019-08-09", "dateTo": "2020-07-17"}, headers=headers)
    data = response.json()


def open_json_and_load_data() -> NoReturn:
    global data, history
    try:
        json_file = open('matches.json', 'r')
        json_info = json.load(json_file)
    except FileNotFoundError:
        json_info = []
    except json.decoder.JSONDecodeError:
        json_info = []
    if not json_info:
        history.append(data)
        with open('matches.json', 'w+') as json_file:
            json.dump(history, json_file, indent=4)
        return
    history.append(data)


def create_tables_in_database() -> NoReturn:
    connection = psycopg2.connect(host='localhost', database='postgres', port=5432, user='postgres', password='qwe123')
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE TABLE All_commands_in_this_seasons (command_id integer primary key not null, command_name varchar(100) not null)")
        connection.commit()
        cursor.execute("CREATE TABLE Premier_League (id serial primary key, seasons varchar(100) not null, start_seasons date, end_seasons date, champion_id integer not null)")
        connection.commit()
        cursor.execute("CREATE TABLE info_about_season (id serial primary key, season_id integer not null, round integer not null, match_date date not null, home_team_id integer not null, away_team_id integer not null, home_team_goal integer not null, away_team_goal integer not null)")
        connection.commit()
        cursor.close()
    except:
        connection.rollback()
    connection.close()


def load_to_database() -> NoReturn:
    global data
    seasons = (f'{data["matches"][0]["season"].get("startDate")[:4]}/{data["matches"][0]["season"].get("endDate")[:4]}')
    start_seasons = data["matches"][0]["season"].get("startDate")
    end_seasons = data["matches"][0]["season"].get("endDate")
    champion_id = data["matches"][0]['homeTeam']['id']
    connection = psycopg2.connect(host='localhost', database='postgres', port=5432, user='postgres', password='qwe123')
    cursor = connection.cursor()
    try:
        for item in data["matches"]:
            if item["matchday"] == 1:
                cursor.execute("Insert into All_commands_in_this_seasons(command_id, command_name) values(%s, %s)", (item['homeTeam']['id'], item['homeTeam']['name']))
                connection.commit()
                cursor.execute("Insert into All_commands_in_this_seasons(command_id, command_name) values(%s, %s)", (item['awayTeam']['id'], item['awayTeam']['name']))
                connection.commit()
        cursor.execute("Insert into Premier_League(seasons, start_seasons, end_seasons, champion_id) values(%s, %s, %s, %s)", (seasons, start_seasons, end_seasons, champion_id))
        connection.commit()
        cursor.execute("ALTER TABLE premier_league ADD CONSTRAINT id_team_fpkey FOREIGN KEY(champion_id) REFERENCES All_commands_in_this_seasons(command_id) match simple ON UPDATE NO ACTION ON DELETE NO ACTION")
        connection.commit()
        cursor.execute("Select id from premier_league")
        season_id = cursor.fetchall()
        for item in data["matches"]:
            cursor.execute("Insert into info_about_season(season_id, round, match_date, home_team_id, away_team_id, home_team_goal, away_team_goal) values(%s, %s, %s, %s, %s, %s, %s)", (season_id[0][0], item['matchday'], item['utcDate'][:10], item['homeTeam']['id'], item['awayTeam']['id'], item['score']['fullTime']['homeTeam'], item['score']['fullTime']['awayTeam']))
            connection.commit()
        cursor.execute("ALTER TABLE info_about_season ADD CONSTRAINT home_team_id_pkey_with_comand_id_home_team FOREIGN KEY (home_team_id) REFERENCES All_commands_in_this_seasons (command_id) match simple ON UPDATE NO ACTION ON DELETE NO ACTION")
        connection.commit()
        cursor.execute("ALTER TABLE info_about_season ADD CONSTRAINT home_team_id_pkey_with_comand_id_away_team FOREIGN KEY (away_team_id) REFERENCES All_commands_in_this_seasons (command_id) match simple ON UPDATE NO ACTION ON DELETE NO ACTION")
        connection.commit()
        cursor.execute("ALTER TABLE info_about_season ADD CONSTRAINT seasons_id FOREIGN KEY (season_id) REFERENCES premier_league (id) match simple ON UPDATE NO ACTION ON DELETE NO ACTION")
        connection.commit()
        cursor.close()
    except:
        print("Program break")
        connection.rollback()
    connection.close()


class MyWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.number_of_round = 0
        self.setWindowTitle('My first menu bar')
        self.setFixedSize(500, 300)
        self.widget = QWidget()
        self.main_layout = QGridLayout()
        self.main_layout.setSpacing(10)
        self.setLayout(self.main_layout)

        #menu bar
        self.menu_bar = QMenuBar()
        self.main_layout.addWidget(self.menu_bar, 0, 0)
        self.msg_layout = QVBoxLayout()
        self.main_layout.addLayout(self.msg_layout, 1, 0)
        self.text_edit = QTextEdit()
        self.text_edit.setFixedHeight(180)
        self.msg_layout.addWidget(self.text_edit)
        self.space = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.main_layout.addItem(self.space, 2, 0)
        self.action_file = self.menu_bar.addMenu("Seasons")

        self.horizontalLayout = QHBoxLayout()

        self.edit = self.action_file.addMenu("2019/2020")

        self.chooseround_10 = self.edit.addMenu("Round 1-10")
        self.chooseround_20 = self.edit.addMenu("Round 11-20")
        self.chooseround_30 = self.edit.addMenu("Round 21-30")
        self.chooseround_40 = self.edit.addMenu("Round 31-37")
        for i in range(1, 38):
            if i <= 10:
                self.chooseround = QAction(f"Round {i}", self)
                self.chooseround_10.addAction(self.chooseround)
                self.chooseround.triggered.connect(partial(self.add_msg, i))
            elif i > 10 and i <= 20:
                self.chooseround = QAction(f"Round {i}", self)
                self.chooseround_20.addAction(self.chooseround)
                self.chooseround.triggered.connect(partial(self.add_msg, i))
            elif i > 20 and i <= 30:
                self.chooseround = QAction(f"Round {i}", self)
                self.chooseround_30.addAction(self.chooseround)
                self.chooseround.triggered.connect(partial(self.add_msg, i))
            elif i > 30 and i <= 40:
                self.chooseround = QAction(f"Round {i}", self)
                self.chooseround_40.addAction(self.chooseround)
                self.chooseround.triggered.connect(partial(self.add_msg, i))
        self.widget.setLayout(self.main_layout)
        self.setCentralWidget(self.widget)

    def add_msg(self, number):
        self.download_info_from_database(number)
        self.text_edit.clear()
        self.text_edit.append(f"Round {number}")
        for i in range(0, 10):
            self.text_edit.append(f"{self.info_about_tour[i][0]}: \t {self.info_about_tour[i][-2]}-{self.info_about_tour[i][-1]} \t {self.name_home_team[i][0]} - {self.name_away_team[i][0]}")

    def download_info_from_database(self, number):
        try:
            connection = psycopg2.connect(host='localhost', database='postgres', port=5432, user='postgres',
                                          password='qwe123')
            cursor = connection.cursor()
            cursor.execute(
                'Select info_about_season.match_date, info_about_season.home_team_id, info_about_season.away_team_id, info_about_season.home_team_goal, info_about_season.away_team_goal from premier_league inner join info_about_season on premier_league.id = info_about_season.season_id where info_about_season.round = %s;',
                (number,))
            self.info_about_tour = cursor.fetchall()
            cursor.execute(
                'select all_commands_in_this_seasons.command_name from all_commands_in_this_seasons inner join info_about_season on all_commands_in_this_seasons.command_id = info_about_season.home_team_id where info_about_season.round = %s;',
                (number,))
            self.name_home_team = cursor.fetchall()
            cursor.execute(
                'select all_commands_in_this_seasons.command_name from all_commands_in_this_seasons inner join info_about_season on all_commands_in_this_seasons.command_id = info_about_season.away_team_id where info_about_season.round = %s;',
                (number,))
            self.name_away_team = cursor.fetchall()
            cursor.close()
        except:
            print("HEREEEE")
            connection.rollback()
        connection.close()


def main() -> NoReturn:
    load_data_from_url()
    open_json_and_load_data()
    create_tables_in_database()
    load_to_database()
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()