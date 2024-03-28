from django.shortcuts import render

# index view.
def index(request):
  return render(request,'core/index.html')

# contact view
def contact(request):
  return render(request,'core/contact.html')