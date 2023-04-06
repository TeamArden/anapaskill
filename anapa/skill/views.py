from django.shortcuts import render
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
TOKEN = (os.getenv('TOKEN'))

# def index(request):
#     return render(request, 'skill/index.html')


def index(request):
    context = {'TOKEN': TOKEN}
    return render(request, 'skill/index.html', context)
