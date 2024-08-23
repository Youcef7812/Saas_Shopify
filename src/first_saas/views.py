from django.http import HttpResponse
import pathlib
from django.shortcuts import render

from visits.models import PageVisits

this_dir=pathlib.Path(__file__).resolve().parent

def home_page_view(request,*args,**kwargs):
    """"
    html_=""
    location=this_dir / "home.html"
    html_=location.read_text()
    """
    query_set=PageVisits.objects.all()
    page_qs=PageVisits.objects.filter(path=request.path)
    count_visits=query_set.count()
    html_template="home.html"
    mon_titre="First Saas"
    my_context={
        "page_title":mon_titre,
        "visits":query_set,
        "count_visits":count_visits,
        "page_visits":page_qs.count()
    }
    PageVisits.objects.create(path=request.path)
    return render(request,html_template,my_context)
