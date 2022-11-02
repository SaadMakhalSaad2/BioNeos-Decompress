from bz2 import decompress
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from . models import MessageData
from . forms import CompressForm

# Declare Key Varaibles
BASE_LIST = '0123456789abcdefghijklmnopqrstuvwxyz./:'
BASE_DICT = dict((c, idx) for idx, c in enumerate(BASE_LIST))
# service_url = 'https://shortnsweet.herokuapp.com'
service_url = '127.0.0.1'


def decompress(str1):
    ints = "1234567890"
    num = ""
    letters = ""
    result_string = ""
    i = 0
    while i < len(str1):
        if str1[i] in ints:
            num += str1[i]
        else:
            letters += str1[i]
        i += 1
    for i, char in enumerate(num):
        result_string += int(char) * letters[i]
    return result_string


def get_form(request):
    list = []
    data = MessageData.objects.all()
    for d in data:
        list.append(d)
    print(list)
    list.reverse()

    if request.method == 'POST':
        form = CompressForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['message']

            msg = MessageData()
            msg.message = text
            msg.decoded = decompress(text)
            if msg.decoded:
                msg.save()
            else:
                messages.success(request, '{}'.format('Invalid input'))

            return HttpResponseRedirect("/")

    form = CompressForm()
    return render(request, 'myform/form.html', {'form': form, 'things': list})
