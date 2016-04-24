"""
Functions related to degree days
"""


from carp_watcher.models import Stream
from carp_watcher.models import Data_Stream_Temp

import datetime

def get_degree_days(stream_ins):
    """
    Calculates degree_days for a stream for a current year
    :param stream: {Model.object.Stream}  Stream model instance
    :return: degree_days: {int} number of degree days per stream

    date = datetime.datetime.now()
    current_year = datetime.datetime.strftime(date, "%Y")
    temp_data_ins = Data_Stream_Temp.objects.filter(day__year=current_year)
    for instance in temp_data_ins:
        print instance
    """
    return 901
