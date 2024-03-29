from django.shortcuts import render,redirect
from items.models import Category, Item
from .forms import SignupForm
# index view.
def index(request):
  items=Item.objects.filter(is_sold=False)[0:6]
  categories=Category.objects.all()
  return render(request,'core/index.html',{'items':items,'categories':categories})

# contact view
def contact(request):
  return render(request,'core/contact.html')
#signup view
def signup(request):
  if request.method=='POST':
    form=SignupForm(request.POST)
    
    if form.is_valid():
      form.save()
      return redirect('/login/')
  else:
    form=SignupForm()
  return render(request, 'core/signup.html',{'form':form})