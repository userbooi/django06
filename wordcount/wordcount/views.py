from django.shortcuts import render

def home(request):
    return render(request, 'word.html', {'counttext':'100'})

def count(request):
    words = request.GET['fulltext']
    wordslist = words.split(' ')
    return render(request, 'count.html', {'word':words, 'len':len(wordslist)})

def help(request):
    help_text = 'this is the help page'
    intruction = 'to use the count function, all you need to do is\n' \
                 'enter what ever you like into the text box and click count!'
    return render(request, 'help.html', {'help_text':help_text, 'intruc': intruction})