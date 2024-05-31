from django import forms

class PieChartForm(forms.Form):
    labels = forms.CharField(label='Labels (comma-separated)', max_length=200, initial='Django REST framework, Django Channels, Django Oscar, Django CMS, Django Haystack')
    sizes = forms.CharField(label='Sizes (comma-separated)', max_length=200, initial='50, 20, 10, 10, 10')