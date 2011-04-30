# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from polls.models import Choice, Poll
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext

def redirect_to_polls(request):
    return HttpResponseRedirect('/polls/')

def index(request):
    #return HttpResponse("Hello, world. You're at the poll index.")
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    #output = ', '.join([p.question for p in latest_poll_list])
    #return HttpResponse(output)
    context = {'latest_poll_list': latest_poll_list}
    return render_to_response('index.html', context)

from django.http import Http404

from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response

def detail(request, poll_id):
    #return HttpResponse("You are looking at poll %s." % (poll_id,))
    #return render_to_response('detail.html', {'poll': p})
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('detail.html', {'poll': p}, context_instance=RequestContext(request))

def results(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('results.html', {'poll': p})

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))

