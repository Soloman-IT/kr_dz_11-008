from django.template import loader
from django.http import HttpResponse
from . import forms
from .models import Record
from django.shortcuts import render
#
interpretation = {(0, 16): "Выраженный дефицит массы тела",
           (16, 18.5): "Недостаточная масса тела (дефицит)",
           (18.5, 25): "Норма",
           (25, 30): "Избыточная масса тела",
           (30, 35): "Ожирение 1-й степени",
           (35, 40): "Ожирение 2-й степени",
           (40, 999): "Ожирение 3-й степени",
}

count_1 = 0
def main(request):
    global count_1
    count_1 += 1
    context = {"count" : count_1}
    global interpretation
    if request.method == "POST":
        form = forms.Registration(request.POST)
        if form.is_valid():

            chel = Record()


            name = form.cleaned_data['name']
            years = form.cleaned_data['years']
            weight = form.cleaned_data['weight']
            height = form.cleaned_data['height']
            size = form.cleaned_data['size']
            gender = form.cleaned_data['gender']
            new_height = height/100
            bmi = weight / new_height ** 2

            for r, inter in interpretation.items():
                if r[0] <= bmi < r[1]:
                    print(res)
                    break
                res = inter
            else:
                res = 'WTF'

            print("bmi", bmi)
            sum = 0
            print(Record.objects.all())

            for i in range(len(Record.objects.all())):
                sum += Record.objects.all()[i].imt
            print(Record.objects.all()[0].name)
            mean = sum / len(Record.objects.all())
            try:
                imt = round((bmi / mean - 1) * 10, 1)
            except:
                imt = 0

            chel.name = name
            chel.height = height
            chel.weight = weight
            chel.age = years
            chel.imt = bmi
            chel.result = res
            chel.gender = gender
            chel.save()

            context["form"] = forms.Registration()
            context["result"] = res
            context["user"] = (name, years, weight, height, size, imt)
            context["size"] = size
            return render(request, "main.html", context=context)

    context["form"] = forms.Registration()
    return render(request, "main.html", context=context)

count_2 = 0
def dop_page_1(request):
    global count_2
    count_2 += 1
    context = {"count" : count_2}
    template = loader.get_template("dop_site_1.html")
    return HttpResponse(template.render(context, request))

count_3 = 0
def dop_page_2(request):
    global count_3
    count_3 += 1
    context = {"count" : count_3}
    template = loader.get_template("dop_site_2.html")
    return HttpResponse(template.render(context, request))