from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render 
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question, Users

user = Users()
def reset():
    global user
    user = Users()    

class IndexView(generic.TemplateView):
    template_name = 'polls/index.html'
    context_object_name = 'start_question'
    
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/details.html'

class MapaView(generic.TemplateView):
    model = Users
    template_name = 'polls/mapa.html'

class ResultadosView(generic.TemplateView):
    model = Users
    template_name = 'polls/resultados.html'        

def listaResultados(request):
    reset()
    points = list(Users.objects.values('id', 'latitude', 'longitude', 'total_score'))
    context = {'points':points}
    return render(request, 'polls/resultados.html', context)    
    
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        if str(selected_choice) == str(question.answer):
            user.total_score += int(str(question.score))
            print (user.total_score)
        else:
            print ("No entro")
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        if question.id == 5:
            return HttpResponseRedirect(reverse('polls:mapa', args=(user.total_score,)))
        else :
            return HttpResponseRedirect(reverse('polls:details', args=(question.id + 1,)))

def add_location(request):
    user.latitude = request.GET.get('lat')
    user.longitude = request.GET.get('long')
    user.save()
    reset()
    return 1