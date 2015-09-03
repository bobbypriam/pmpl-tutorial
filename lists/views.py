from django.http import HttpResponse

# Create your views here.
def home_page(request):
  return HttpResponse("""<!DOCTYPE html>
    <html>
      <head>
        <title>Bobby Priambodo</title>
      </head>
      <body>
        <h1>Bobby Priambodo's Profile</h1>
        <p>Hello, my name is Widyanto Bagus Priambodo, but you can call me Bobby. My student ID is 1206208315.</p>
      </body>
    </html>""")
