from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from .models import Food

# Create your views here.
def index(request,):
    #列出清單
    foods=Food.objects.all()
    #把所有查詢到的food對象，傳給模板去渲染
    return render(request,'index.html',{'foods':foods})

def new(request):
    return render(request,'new.html')

@require_POST
def add(request):
    food =Food(
        food=request.POST['food'],
        price=request.POST['price'],
        date=request.POST['date'],
    )
    food.save()
    return redirect('food:index')

def show(request,id):
    food=get_object_or_404(Food,id=id)
    if request.method =='POST':
        food.food=request.POST['food']
        food.price=request.POST['price']
        food.date=request.POST['date']
        food.save()
        return redirect('food:show',id=food.id)
    return render(request, 'show.html', {'food':food})

def edit(request,id):
    food=get_object_or_404(Food,id=id)
    return render(request, 'edit.html', {'food':food})

def delete(request,id):
    food=get_object_or_404(Food,id=id)
    food.delete()
    return redirect('food:index')