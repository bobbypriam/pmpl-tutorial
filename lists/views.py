from django.shortcuts import redirect, render
from lists.models import Item

def home_page(request):
  if request.method == 'POST':
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-only-list-in-the-world/')

  count = Item.objects.count()
  comment = ''

  if count == 0:
    comment = 'Yey, waktunya berlibur!'
  elif count < 5:
    comment = 'Sibuk tapi santai.'
  else:
    comment = 'Oh, tidak!'

  return render(request, 'home.html', {'comment': comment})

def view_list(request):
  items = Item.objects.all()
  return render(request, 'list.html', {'items': items})
