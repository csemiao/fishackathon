
from django.shortcuts import render
from django.http import JsonResponse

import logic.decision_tree as d_tree
import logic.temperature as temp
import logic.length as length


def main_page(request):
    some_bindings = {
        'message': "hello",
    }
    return render(request, 'main.html', some_bindings)

def show_all(request):
    if request.method == 'GET':
        results = d_tree.get_data()
        return JsonResponse(results, safe=False)

def temp_data(request):
    if request.method == 'GET':
        stream_name = request.GET.get('stream')
        data = temp.get_temp_graph_data(stream_name)
        return JsonResponse(data, safe=False)


def length_data(request):
    if request.method == 'GET':
        stream_name = request.GET.get('stream')
        data = length.get_length_graph_data(stream_name)
        return JsonResponse(data, safe=False)