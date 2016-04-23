#
# This script populates the database with for stream temps
#

import os
import sys


script_path = os.path.dirname(__file__)
project_dir = os.path.abspath(os.path.join(script_path, '../','..','wecsl_test'))
sys.path.insert(0, project_dir)

# Set the django settings module to the symlink in the scripts directory (which points to the actual file)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django
django.setup()

import xml.etree.ElementTree as eTree
import datetime

from carp_watcher import Stream, Data_Stream_Temp


# noinspection PyBroadException
def setup_schedule():
    """
    Parses an XML file and populates the database with Game model instances.
    :return: void:
    """
    schedule_tree = eTree.parse('schedule.xml').getroot()
    for game_day in schedule_tree:
        # generate a date object for a particular day
        year = int(game_day.attrib['year'])
        day = int(game_day.attrib['day'])
        month = int(game_day.attrib['month'])
        date_obj = datetime.date(year, month, day)
        for game_time in game_day:
            # (cont..) for each time in that date, generate a time object and find the correct teams
            # then add create a game model instance and save it to the database
            start_time = game_time.attrib['start_time']
            time_obj = datetime.datetime.strptime(start_time, '%H:%M').time()
            try:
                home_query = game_time.find('home_team').text
                away_query = game_time.find('away_team').text
                home_team_ins = Team.objects.get(name=home_query)
                away_team_ins = Team.objects.get(name=away_query)
                add_game(date_obj, time_obj, home_team_ins, away_team_ins)
            except:
                print('Probable error in XML: Queries are\n' +
                      ' home_team ' + home_query + '\n'
                      ' away_team ' + away_query + '\n'
                      ' date_obj ' + str(date_obj) + '\n'
                      ' game_time ' + str(time_obj))




def add_game(date_obj, time_obj, home_team_ins, away_team_ins):
    """
    Adds a game to the database
    :param date_obj: {datetime.date} the day of the game
    :param time_obj: {datetime.time} the time of the game
    :param home_team_ins: {Model.object.Team} the home team (instance object)
    :param away_team_ins: {Model.object.Team} the away team (instance object)
    :return: game_ins: {Model.object.Game} instance object of the game created
    """
    print ('Adding game: ' + str(date_obj) + ' ' + str(time_obj.strftime('%H:%M')) + ' ' +
           away_team_ins.name + ' at ' + home_team_ins.name)
    game_ins = Game.objects.get_or_create(game_date=date_obj, game_time=time_obj,
                                          home_team=home_team_ins, away_team=away_team_ins)[0]
    return game_ins


setup_stream_and_temp()

