from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def admit(request):
    form = UserCreationForm()
    return render(request, 'admission/admit.html',{'form':form})
