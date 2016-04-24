"""
Logic related to stream lengths
"""

from carp_watcher.models import Data_Stream, Fish
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
