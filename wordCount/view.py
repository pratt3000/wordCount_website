from django.http import HttpResponse
from django.shortcuts import render
import operator
def pict(request):
    return render(request, 'home.html' )

def bhavika(request):
    newtext = request.GET['text']
    list = newtext.split()
    wordcount = {}
    for word in list:
        if word in wordcount:
            wordcount[word]+=1
        else:
            wordcount[word]=1
        sortcount = sorted(wordcount.items(),key= operator.itemgetter(1), reverse = True)
    return render(request, 'next.html',{'newtext':newtext,'list':len(list),'wordcount':sortcount})

def pratt(request):
    return render(request, 'info.html')
    