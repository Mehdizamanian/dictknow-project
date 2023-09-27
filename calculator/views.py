from django.shortcuts import render

def index(request):
    c=0
    try:
        if request.method=="POST":
            n1=eval(request.POST.get("num1"))
            n2=eval(request.POST.get("num1"))
            opr=request.POST.get("opr")  
            

            if opr=="+":
                c=n1+n2

            elif opr=="-":
                c=n1-n2

            elif opr=="*":
                c=n1*n2   

            elif opr=="/":
                c=n1/n2
    except:
      c="select your operator"
 
    return render(request,'calculator/index.html',{'c':c})

# Create your views here.
