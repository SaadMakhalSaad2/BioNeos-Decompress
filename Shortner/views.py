from bz2 import decompress
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from . models import MessageData
from . forms import CompressForm

"""
this function is to perform the compressing logic
it is done first by separating letters from numbers into different strings
then looping through them and repeating letters with their corresponding numbers
"""
def decompress(message):
    integers = "1234567890"
    numbers = ""
    letters = ""
    decoded_message = ""
    i = 0
    #separating numbers from letters into two strings, numbers and letters
    while i < len(message):
        if message[i] in integers: 
            numbers += message[i]     
        else:
            letters += message[i]
        i += 1
    #repeat each letter with its coressponding number 
    for i, letter in enumerate(numbers):
        decoded_message += int(letter) * letters[i]
    return decoded_message


#main endpoint for displaying the form
def get_form(request):
    #getting message records from the database
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
