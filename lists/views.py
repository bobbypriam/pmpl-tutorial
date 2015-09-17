from django.shortcuts import redirect, render
from lists.models import Item

def home_page(request):
  if request.method == 'POST':
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/')

  items = Item.objects.all()
  count = items.count()
  comment = ''

  if count == 0:
    comment = 'Yey, waktunya berlibur!'
  elif count < 5:
    comment = 'Sibuk tapi santai.'
  else:
    comment = 'Oh, tidak!'

  return render(request, 'home.html', {'items': items, 'comment': comment})
