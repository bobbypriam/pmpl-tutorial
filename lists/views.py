from django.shortcuts import redirect, render
from lists.models import Item, List

def home_page(request):
  count = Item.objects.count()
  comment = ''

  if count == 0:
    comment = 'Yey, waktunya berlibur!'
  elif count < 5:
    comment = 'Sibuk tapi santai.'
  else:
    comment = 'Oh, tidak!'

  return render(request, 'home.html', {'comment': comment})

def view_list(request, list_id):
  list_ = List.objects.get(id=list_id)
  return render(request, 'list.html', {'list': list_})

def new_list(request):
  list_ = List.objects.create()
  Item.objects.create(text=request.POST['item_text'], list=list_)
  return redirect('/lists/%d/' % (list_.id,))

def add_item(request, list_id):
  list_ = List.objects.get(id=list_id)
  Item.objects.create(text=request.POST['item_text'], list=list_)
  return redirect('/lists/%d/' % (list_.id,))
