from django.shortcuts import render
from .Tweepy import scrapper
from .Sentiment import analyze


def userForm(request):
    try:
        x = ''
        y = ''
        z = ''
        e = ''
        b = ''
        c = ''
        hash = request.GET['hashtag']
        apt = request.GET['apt']
        results = []
        for i in scrapper('(#' + hash + ') since:' + apt, 10):
            a = analyze(i)
            results.append(a)
        d = results
        x = d.count("Positive")
        y = d.count("Negative")
        z = d.count("Neutral")
        list1 = [x, y, z]
        e = list1[0] * 100.0 / len(d)
        b = list1[1] * 100.0 / len(d)
        c = list1[2] * 100.0 / len(d)
    except:
        pass
    return render(request, "userform.html", dict(num1=e, num2=b, num3=c))
