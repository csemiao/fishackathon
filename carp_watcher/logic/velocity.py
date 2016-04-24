'''
Flow data logic
'''
import datetime

from carp_watcher.models import Data_Stream


def get_flow_spike(stream):
    date = datetime.datetime.now()
    current_year = datetime.datetime.strftime(date, "%Y")
    current_month = datetime.datetime.strftime(date, "%m")
    current_day = datetime.datetime.strftime(date, "%d")

    the_streams = Data_Stream.objects.filter(stream=stream).filter(day__year=current_year, day__month=current_month,
                                                                  day__day=current_day)
    if len(the_streams) == 1:
        return the_streams[0].spike
    else:
        return -1
