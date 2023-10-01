from django.shortcuts import render
from django.contrib import messages

def bmiView(request):
    c=''
    try:
        if request.method=="POST":
            weight=eval(request.POST.get('weight'))
            age=eval(request.POST.get('age')) 
            if weight<83 and age<23:
                c='you are fit'
            else:
                c='damn u fucking fat'
            # elif opr=="-":
            #     c=n1-n2
            # elif opr=="*":
            #     c=n1*n2 ;  
            # elif opr=="/":
            #     c=n1/n2

    except:
      c="numbers not found , please enter your numbers again"
    print(c)
    return render(request,'bmi/bmi.html',{"c":c})
# Create your views here.
