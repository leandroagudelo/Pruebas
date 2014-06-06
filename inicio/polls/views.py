#from django.shortcuts import render
from django.http import HttpResponseBadRequest
from django.shortcuts import render_to_response
from django.template import RequestContext
from polls.models import Poll


def home(request):
    result = {}

    name = "Leandro Esneyder"
    lastname = "Agudelo Villalobos"

    result['name'] = name
    result['lastname'] = lastname
    result['query'] = Poll.objects.all()

    return render_to_response('home.html',result ,context_instance=RequestContext(request))


def save_poll(request):
    result = {}
    question = request.POST["question"]
    pub_date = request.POST["pub_date"]
    try:
        poll = Poll()
        poll.question = question
        poll.pub_date = pub_date
        poll.save()

        result["status"] = "SUCCESS"
        result["msg_status"] = "Su encuesta se ha creado satisfactoriamente"
        result['name'] = "Leandro"
        result['lastname'] = "Agudelo"

    except Exception as error:
        result["status"] = "FAILURE"
        result["msg_status"] = "Error en la creacion"



    return render_to_response('home1.html',result ,context_instance=RequestContext(request))


def save_poll_3(request):
    result = {}
    question = request.POST["question"]
    pub_date = request.POST["pub_date"]
    try:
        poll = Poll()
        poll.question = question
        poll.pub_date = pub_date
        poll.save()

        result["status"] = "SUCCESS"
        result["msg_status"] = "Su encuesta se ha creado satisfactoriamente"
        result['name'] = "Leandro"
        result['lastname'] = "Agudelo"

    except Exception as error:
        result["status"] = "FAILURE"
        result["msg_status"] = "Error en la creacion"



    return render_to_response('home3.html',result ,context_instance=RequestContext(request))
# Create your views here.
