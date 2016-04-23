from django.shortcuts import render

def main_page(request):
    some_bindings = {
        'message': 'hello'
    }
    return render(request, 'main.html', some_bindings)
