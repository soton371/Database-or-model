from django.shortcuts import render, HttpResponse
from data_collect.models import CollectModel
def home(request):
    if request.method == "GET":
        name = ['This is demo', 'Aaa', 'Bbb']
        context = {'name':name}
    return render(request, 'home.html', context)
    
def collect(request):
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        team = request.POST['team']
        print('name: ' +name+ ' age: ' +age)
        obj = CollectModel(name=name,age=age,team = team)
        obj.save()
    return render(request,'collect.html')