from django.shortcuts import render

from cowsay.models import CowText
from cowsay.forms import AddCowText
import subprocess


def index(request):
    if request.method == 'POST':
        form = AddCowText(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form = AddCowText()
            cowsay_text = subprocess.run(
                ['cowsay'] + data['text'].split(), capture_output=True
            ).stdout.decode()
            CowText.objects.create(
                text=data['text']
            )

        return render(request, 'index.html', {'cowsay_text': cowsay_text, 'form': form})

    form = AddCowText()
    return render(request, 'index.html', {'form': form})


def history(request):
    cowsay_history_list = list(CowText.objects.all())
    most_recent = cowsay_history_list[-10:][::-1]

    return render(request, 'history.html', {'most_recent': most_recent})
