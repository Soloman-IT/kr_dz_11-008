from django import forms

class Registration(forms.Form):
    name = forms.CharField(label = "Your name" , max_length = 100)
    weight = forms.IntegerField(label = "Your weight", max_value = 300)
    height = forms.IntegerField(label = "Your height", max_value = 300)
    years = forms.IntegerField(label = "Your years", max_value = 95)
    size = forms.CharField(label = "Your sizes", max_length=10)