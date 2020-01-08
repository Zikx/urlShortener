from django.shortcuts import render, redirect 
from .models import short_url
from .forms import UrlForm   
from .shortener import shortener

# Create your views here.
def Home(request, token):
    long_url = short_url.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url)

def Make(request):
    form = UrlForm(request.POST)
    rtnData = ""
    formInputData = request.POST.get('long_url', False)

    if request.method == 'POST':
        if form.is_valid():
            NewUrl = form.save(commit=False)
            rtnData = shortener().issue_token() 
            NewUrl.short_url = rtnData
            NewUrl.save()
            # rtnData = "https://127.0.0.1:8000/" + rtnData
        else:
            form = UrlForm()
            rtnData = short_url.objects.get(long_url=formInputData)
            
    return render(request, 'index.html', {'form': form, 'rtnData': rtnData})