from carp_watcher.models import Stream, Data_Stream
import datetime


def get_temp_graph_data(stream):
    to_return = []
    # note that stream is a string here

    stream_ins = Stream.objects.get(name="Chris Creek")
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
