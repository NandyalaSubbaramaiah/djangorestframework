import io
import base64
import urllib.parse
import matplotlib.pyplot as plt
from django.shortcuts import render
from .forms import PieChartForm

def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            labels = form.cleaned_data['labels'].split(',')
            sizes = list(map(int, form.cleaned_data['sizes'].split(',')))
        else:
            labels = ['Django REST framework', 'Django Channels', 'Django Oscar', 'Django CMS', 'Django Haystack']
            sizes = [50, 20, 10, 10, 10]
    else:
        form = PieChartForm()
        labels = ['Django REST framework', 'Django Channels', 'Django Oscar', 'Django CMS', 'Django Haystack']
        sizes = [50, 20, 10, 10, 10]

    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.

    # Save the pie chart to a bytes buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    # Render the template with the pie chart
    return render(request, 'pie_chart.html', {'data': uri, 'form': form})

def chart_view(request):
    return render(request, 'chart.html')

