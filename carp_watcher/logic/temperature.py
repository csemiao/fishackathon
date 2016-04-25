from carp_watcher.models import Stream, Data_Stream
import datetime
from carp_watcher.models import Data_Stream



def get_temp_graph_data(stream):
    to_return = []
    # note that stream is a string here

    stream_ins = Stream.objects.get(name=stream)
    date = datetime.datetime.now()
    year = datetime.datetime.strftime(date, "%Y")
    data_points_ins = Data_Stream.objects.filter(stream=stream_ins).filter(day__year=year)

    for data_point in data_points_ins:
        temp = data_point.temp
        day = data_point.day
        date = datetime.datetime.strftime(day, "%Y-%m-%d")

        dict = {
            "key": date,
            "value": float(temp)
        }
        to_return.append(dict)

    return to_return

def get_water_temp(stream):
    date = datetime.datetime.now()
    current_year = datetime.datetime.strftime(date, "%Y")
    current_month = datetime.datetime.strftime(date, "%m")
    current_day = datetime.datetime.strftime(date, "%d")

    the_streams = Data_Stream.objects.filter(stream=stream).filter(day__year=current_year, day__month=current_month,
                                                                   day__day=current_day)
    if len(the_streams) == 1:
        return the_streams[0].temp
    else:
        return -1
