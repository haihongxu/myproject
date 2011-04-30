# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from polls.models import Poll

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

def detail(request, poll_id):
    #return HttpResponse("You are looking at poll %s." % (poll_id,))
    try:
        p = Poll.objects.get(id=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render_to_response('detail.html', {'poll': p})

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll <strong>%s</strong>." % (poll_id,))

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % (poll_id,))

