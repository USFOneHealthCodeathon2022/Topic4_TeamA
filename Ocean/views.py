from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .forms import HomeForm, EmailForm
from .models import Ocean
#from django.core.files import File
from django.core.mail import send_mail

import Ocean.globalvars as Globalvars

from django.db.models import Q
def homepage(request):
    form = HomeForm(request.POST or None)
    if request.method == 'POST':
       if form.is_valid():
          items = request.POST.get('search')
          #print(items)
          request.session['query'] = items
          return redirect('data')
    return render(request, 'Ocean/homepage.html', {'form': form})

def data(request):
    query = request.session['query']
    print(query)
    lookups = Q(kingdom__icontains=query)
    query_results = Ocean.objects.filter(lookups).distinct()
    #query_results = Ocean.objects.filter(kingdom__startswith='Bac')
    print("query results are:")
    print(query_results)
    return render(request, 'Ocean/data.html', {'query_results': query_results})



def email(request):
    # input email address
    youremail = EmailForm(request.POST or None)
    if request.method == 'POST':
       if youremail.is_valid():
          youremailis = request.POST.get('email')
          request.session['emailis'] = request.POST.get('email')
          send_mail('Your Unique Code', 'Here is email test.', 'liulabdellserver@gmail.com', [youremailis], fail_silently=False)
          #return redirect('download')
    return render(request, 'Codeathon/email.html',{'youremail':youremail})

    

