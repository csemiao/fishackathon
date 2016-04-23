
from django.shortcuts import render
import logic.degree_days as deg_day

def main_page(request):
    some_bindings = {
        'message': "hello",
    }
    deg_day.get_degree_days_for_all_streams()
    return render(request, 'main.html', some_bindings)

def show_all(request):
    return ('hello')


