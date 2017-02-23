from django.shortcuts import render

# Create your views here.
    
from frageAntwo.models import Frage, Antwort

    
def home(request, pk):
    frag = Frage.objects.get(pk= pk)
    antworten = Antwort.objects.filter(frage = frag)
    context = {'antworten': antworten,'frage' : frag}
    return render(request, "frageAntwo/home.html", context)

    
def frageOhneAkzAntwo(request):
    fragen = Frage.objects.exclude( antwort__isAkzeptiert = True )
    context = {'fragen' : fragen}
    return render(request, "frageAntwo/frageOhneAkzAntwo.html", context)
