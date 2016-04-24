"""
Logic related to stream lengths
"""

from carp_watcher.models import Data_Stream, Fish, Stream
import datetime

def get_length(stream):
    """
    Returns the PREDICTED length of the stream in question (depends on the Fish)
    :param stream: {Model.objects.Stream} A stream model instance
    :return: {int} the length of the stream object
    """
    # TODO: Eventually we will parameterize fish

    date = datetime.datetime.now()
    year = datetime.datetime.strftime(date, "%Y")
    month = datetime.datetime.strftime(date, "%m")
    day = datetime.datetime.strftime(date, "%d")

    data_stream_ins = Data_Stream.objects.filter(stream=stream).filter(day__year=year).filter(day__month=month).filter(day__day=day)

    if len(data_stream_ins) != 1:
        raise Exception('too many data_stream instances when calculating length')
    else:
        data_stream = data_stream_ins[0]
        fish_ins = Fish.objects.get(pk=1)   #TODO: get the first fish object... we will fix this later
        incubation_time = pow(float(data_stream.temp), float(fish_ins.exponent)) * float(fish_ins.coefficient)

        length = 3.6 * float(data_stream.velocity) * incubation_time

        return length


def get_length_graph_data(stream):
    # here stream is a string

    to_return = []

    date = datetime.datetime.now()
    year = datetime.datetime.strftime(date, "%Y")

    stream_ins = Stream.objects.get(name="Chris Creek")
    fish = Fish.objects.get(pk=1)
    coeff = fish.coefficient
    exponent = fish.exponent

    data_points = Data_Stream.objects.filter(stream=stream_ins).filter(day__year=year)

    for data_point in data_points:
        temp = float(data_point.temp)
        day = datetime.datetime.strftime(data_point.day, "%Y-%m-%d")
        incubation_time = pow(temp, float(exponent))
        length = 3.6 * incubation_time * float(data_point.velocity)

        dict_obj = {
            "key": day,
            "value": length
        }

        to_return.append(dict_obj)

    return to_return
