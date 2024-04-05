from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from items.models import Item
from communication.forms import CommunicationMessageForm
from communication.models import Communication

# Create your views here.
@login_required
def new_communication(request,item_pk):
  item=get_object_or_404(Item,pk=item_pk)
  
  if item.created_by == request.user:
    return redirect('dashboard:home')
  
  conversations =Communication.objects.filter(item=item).filter(members__in=[request.user.id])
  
  if conversations:
    pass #redirect
  
  if request.method =='GET':
    form=CommunicationMessageForm()
    return render(request,'conversation/new.html',{"form":form})
  else:
    form = CommunicationMessageForm(request.POST)
    
    if form.is_valid():
      conversation=Communication.objects.create(item=item)
      conversation.members.add(request.user)
      conversation.members.add(item.created_by)
      conversation.save()
      
      conversation_message=form.save(commit=False)
      conversation_message.conversation=conversation
      conversation_message.created_by=request.user
      conversation_message.save()
      
      return redirect('items:detail',pk=item_pk)

@login_required
def inbox(request):
  conversations =Communication.objects.filter(members__in=[request.user.id])
  return render(request,'conversation/inbox.html',{'conversations':conversations})

@login_required
def detail(request, pk):
  conversation=Communication.objects.filter(members__in=[request.user.id]).get(pk=pk)
  if request.method=='POST':
    form=CommunicationMessageForm(request.POST)
    
    if form.is_valid():
      conversation_message=form.save(commit=False)
      conversation_message.conversation=conversation
      conversation_message.created_by=request.user
      conversation_message.save()
      
      conversation.save()
      
      return redirect('communication:detail',pk=pk)
  else:
    form=CommunicationMessageForm()
  return render(request,'conversation/detail.html',{'conversation':conversation,'form':form})
  