"""
Functions related to degree days
"""

from carp_watcher.models import Stream, Data_Stream

import datetime


def get_degree_days(stream):
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
    date = datetime.datetime.now()
    current_year = datetime.datetime.strftime(date, "%Y")
    data_stream_list = Data_Stream.objects.all().filter(stream=stream).filter(day__year=current_year)
    dd = 0
    i = 0
    while i < len(data_stream_list):
        aTemp = data_stream_list[i].temp - 15
        if aTemp > 0:
            dd += aTemp
        i += 1
    return dd