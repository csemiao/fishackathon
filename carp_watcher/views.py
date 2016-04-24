
from django.shortcuts import render
from django.http import JsonResponse

import logic.decision_tree as d_tree


def main_page(request):
    some_bindings = {
        'message': "hello",
    }
    return render(request, 'main.html', some_bindings)

def show_all(request):
    if request.method == 'GET':
        results = d_tree.get_data()
        return JsonResponse(results, safe=False)

def length_data(request):
    return ('hello')

def velocity_data(request):
    return ('hello')
