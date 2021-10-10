from django import forms

choice_size = [("1","XXXL"),("2", "XXL"), ("3", "XL"), ("4", "L"), ("5", "M"),("6", "S"), ("7","MS")]

choice_gender = [("Man", "man"), ("Woman", "woman"), ("Helicopter", "c14334")]

class Registration(forms.Form):
    name = forms.CharField(label="Your name" , max_length=100)
    weight = forms.FloatField(label="Your weight", max_value=300)
    height = forms.FloatField(label="Your height", max_value=300)
    years = forms.IntegerField(label="Your years", max_value=95)
    size = forms.ChoiceField(choices=choice_size ,label="Your sizes")
    gender = forms.ChoiceField(label="Your gender", choices=choice_gender)