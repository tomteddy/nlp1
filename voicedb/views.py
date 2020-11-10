from django.shortcuts import render
from voicedb.models import Items, Prices
from django.views.decorators.csrf import csrf_exempt
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

from rest_framework import viewsets

from .serializers import NlpSerializer
from .models import Prices

class NlpViewSet(viewsets.ModelViewSet):
    queryset = Prices.objects.all().order_by('item')
    serializer_class = NlpSerializer

@csrf_exempt
def index(request):
    if request.method == 'POST':
        data = request.POST.get('data', False)
        # item = Items.objects.create(item=data)
        # item.save()
        print(data)
        sent = preprocess(str(data))
        item=''
        price=''
        for s in sent:
            if s[1]=='NN':
                if s[0]!='price':
                    item=s[0]
            if s[1]=='CD':
                price=s[0]
            if s[1]=='JJ':
                price=s[0]
        if len(item) == 0 or len(price) == 0:
            print('no value')
        else:
            print('yay!')
            if Items.objects.filter(item=item).exists() == False:
                item = Items.objects.create(item=item)
                item.save()
            item = Items.objects.get(item = item)
            entry = Prices.objects.create(item=item, price=price)
            entry.save()
    return render(request, 'index.html')

def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent