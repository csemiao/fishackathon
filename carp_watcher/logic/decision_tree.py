import jsonpickle as jp
import degree_days as deg_day
import temperature as temp
import length as length
import velocity as velocity

from carp_watcher.models import Stream

def get_data():
    return_json = []

    streams = Stream.objects.all()
    if len(streams) > 0:
        for stream in streams:
            result = follow_decision_tree(stream)
            return_json.append(result)
    return return_json

def follow_decision_tree(stream):
    """
    Follows the decision tree outlined in the problem statement to determine a stream is suitable for fish spawning
    :param stream:
    :return: json_object: {JSON object} a JSON object containing the following information:
        {
            name: {String - name of the river}
            lat: {Float} - latitude
            long: {Float} - longitude
            status: {Int} - integer corresponding to status enumeration
    """
    # Calculate degree days
    degree_days = deg_day.get_degree_days(stream)
    if degree_days < 650:
        return make_result(stream, 0)

    #Calculate water temp
    water_temp = temp.get_water_temp(stream)
    if water_temp < 17:
        return make_result(stream, 0)

    #Calculate stream length
    predicted_length = length.get_length(stream)
    if stream.length < predicted_length:
        return make_result(stream, 0)

    #Assign flow spike choices
    flow_spike = velocity.get_flow_spike(stream)
    if degree_days > 900:
        if flow_spike:
            return make_result(stream, 4)
        else:
            return make_result(stream, 3)
    else:
        if flow_spike:
            return make_result(stream, 2)
        else:
            return make_result(stream, 1)


def make_result(stream, status):
    """
    Returns a dict corresponding to a non-suitable stream for use with the map
    :param stream: {Models.objects.Stream} Stream model instance
    :return: stream_to_return {dict} dictionary for a non-suitable stream (enumeration 0)
    """
    stream_to_return = {
        "name": stream.name,
        "lat": stream.lat,
        "lng": stream.long,
        "status": status
    }

    return stream_to_return



