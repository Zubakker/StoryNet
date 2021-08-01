from django.shortcuts import render, get_object_or_404

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse('<h1> Home </h1>')
    return render(request, 'pages/home.html', {})

def author_view(request, *args, **kwargs):
    #return HttpResponse('<h1> Hello </h1>')
    my_context = {
            'my_text': 'author rocks',
            'my_number': 796549,
            'my_list': [1, 2, 3, 4],
         }

    return render(request, 'pages/author.html', my_context)

def drafts_view(request, *args, **kwargs):
    #return HttpResponse('<h1> Drafts </h1>'
    return render(request, 'pages/drafts.html', {})

def messages_view(request, *args, **kwargs):
    #return HttpResponse('<h1> Messages </h1>'
    return render(request, 'pages/messages.html', {})

def news_view(request, *args, **kwargs):
    #return HttpResponse('<h1> News </h1>'
    return render(request, 'pages/news.html', {})

def auth_view(request, *args, **kwargs):
    #return HttpResponse('<h1> Auth </h1>'
    return render(request, 'pages/auth.html', {})
