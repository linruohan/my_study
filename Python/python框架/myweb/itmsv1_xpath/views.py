from django.shortcuts import render

# Create your views here.
def insert(request):
    if request.method=='POST':
        username=request.POST.get('username',None)
        password=request.POST.get('password',None)
        models.messages.objects.Create(username=username,password=password)
        models.messages.save()
    return render(request,'insert.html')

def list(request):
    people_list=models.messages.objects.all()
    c=Context({'people_list':people_list})
    return render(request,'showuser.html',c)
