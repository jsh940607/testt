from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from wow.models import Question,Choice
# Create your views here

def vote(request):
    choice = request.POST['choice']
    c=choice.objects.get(ok=choice)
    c.votes=c.votes+1
    c.save()

    pinrt('~~~~~~',choice)

    return render(request , 'wow/vote.html',{})

def deatil(request,id):
    question=Question.objext.get(id=id)
    return render(request , 'wow/deatil.html',{'item':question})

def index(request)
