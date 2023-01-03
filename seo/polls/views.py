from imp import C_EXTENSION
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
import pandas as pd
import os
def index(request):
    return HttpResponse("Hello, world!")
dot = ''
from .models import Document
def home(request):
    documents = Document.objects.all()
    #rank = Document.objects.latest('id')
    #print(rank)
    for obj in documents:
        rank = obj.document.url
        #print(rank)
    #print(rank)
    return render(request, 'home.html', { 'documents': documents })


from django.shortcuts import render
from django.shortcuts import render
from mysite import settings
from django.core.files.storage import FileSystemStorage

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        #print(uploaded_file_url)
        return render(request, 'simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'simple_upload.html')

from .forms import DocumentForm
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            #func_obj = form
            #func_obj.sourceFile = form.cleaned_data['sourceFile']
            form.save()
            #print(form.Document.document)
            #form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })

cx = 'cxkey'
key = 'csekey'

import advertools as adv
import pandas as pd
pd.options.display.max_columns = None
import urllib.request
import requests
import csv
def uploadings(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print(uploaded_file_url)
        dot ='/var/www/seo/t'
        df=pd.read_csv(dot+uploaded_file_url)
        z=list(df['keyword'])
        y=list(df['url'])
        print(y[0])
        print(z)
        search = adv.serp_goog(q=z, cx=cx, key=key)
        search.to_csv('/var/www/seo/t/media/input/input.csv')
        df1 = pd.read_csv('/var/www/seo/t/media/input/input.csv', index_col=[0])
	    #df2 = df1[df1['displayLink']== 'www.desss.com']
        df2 = df1[df1['displayLink']== y[0]]
        df2.to_csv('/var/www/seo/t/media/output/output.csv')
	    #return HttpResponse("Hello, world!")
        return render(request, 'simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'simple_upload.html')

cxs = 'cxkey'
keys = 'csekey'
    
def csvs(request):
    documents = Document.objects.all()
    #rank = Document.objects.latest('id')
    #print(rank)
    for obj in documents:
        rank = obj.document.url
        #print(rank)
    #print(rank)
    dot = '/var/www/seo/t'
    df1=pd.read_csv(dot+rank)
    n=list(df1['keyword'])
    m=list(df1['url'])
    print(m[0])
    print(n)
    search = adv.serp_goog(q=n, cx=cxs, key=keys)
    search.to_csv('/var/www/seo/t/media/input/input1.csv')
    #df3 = pd.read_csv('/var/www/seo/t/media/input/input1.csv', index_col=[0])
	#df2 = df1[df1['displayLink']== 'www.desss.com']
    #df4 = df3[df3['displayLink']== m[0]]
    #df4.to_csv('/var/www/seo/t/media/output/output1.csv')
    options = list(df1['url'])
    df3 = pd.read_csv('/var/www/seo/t/media/input/input1.csv', index_col=None, header=0)
    #df = pd.read_csv('input.csv', index_col=None, header=0)
    rslt_df = df3[df3['displayLink'].isin(options)]
    rslt_df.to_csv('/var/www/seo/t/media/output/output1.csv', index=False)
    return render(request, 'csv.html', { 'documents': documents })

def form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            #func_obj = form
            #func_obj.sourceFile = form.cleaned_data['sourceFile']
            form.save()
            #print(form.Document.document)
            #form.save()
            return redirect('csvs')
    else:
        form = DocumentForm()
    return render(request, 'form_upload.html', {
        'form': form
    })
