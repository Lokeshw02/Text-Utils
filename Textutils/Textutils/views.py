# Views.py
# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
         #return render(request, 'analyze.html', params)
        djtext = analyzed
    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if (newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed New Lines ', 'analyzed_text': analyzed}
        djtext = analyzed
       # return render(request, 'analyze.html', params)
    if (extraspaceremover == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if (djtext[index] == " " and djtext[index + 1] == " "):
                pass
            else:
                analyzed = analyzed + char


        params = {'purpose': 'Removed Extra Spaces  ', 'analyzed_text': analyzed}

       # return render(request, 'analyze.html', params)
        djtext = analyzed
    if (charactercounter == 'on'):
        count = 0;
        for char in djtext:
            count = count + 1

        analyzed = count
        params = {'purpose': djtext + "   ||    No of characters you entered are(is)"  ,'analyzed_text': analyzed }
        # return render(request, 'analyze.html', params)
        djtext = analyzed

    return render(request, 'analyze.html', params)









def ex1(requets):
    sites = ['''<h1>For Entertainment </h1><a href = "https://www.youtube.com" ><h2>youtube video</h2></a>''',
             '''<h1>For Interaction </h1><a href = "https://www.facebook.com" ><h2>Facebook</h2></a>''',
             '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" ><h2>Ted Talk</h2></a>''',
             '''<h1>For Internship   </h1><a href="https://internshala.com" ><h2>Intenship</h2></a>''',
             ]
    return HttpResponse((sites))

# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("newline remove first")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover back")
#
# def charcount(request):
#     return HttpResponse("charcount ")
