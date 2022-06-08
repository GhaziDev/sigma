from django.shortcuts import render

# Create your views here.
def index(request):
    def get_name():
        return "Patrick"
    return render(request, 'index.html', {'name': get_name()})