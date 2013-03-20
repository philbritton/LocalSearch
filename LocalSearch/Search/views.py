# Create your views here.
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
import fetcher
def search(request):
    if request.method == 'GET':
        c={}
        c.update(csrf(request))
        return render_to_response("search.htm",c)
    if request.method == 'POST':
        query = request.POST["query"]
        
        result = fetcher.getresult(query)
        result.update({"query":query})
        result.update(csrf(request))
        return render_to_response("search.htm",result)