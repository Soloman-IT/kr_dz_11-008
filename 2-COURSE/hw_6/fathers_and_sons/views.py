from django.template import loader
from django.http import HttpResponse
from . import forms
#
interpretation = {(0, 16): "Выраженный дефицит массы тела",
           (16, 18.5): "Недостаточная масса тела (дефицит)",
           (18.5, 25): "Норма",
           (25, 30): "Избыточная масса тела",
           (30, 35): "Ожирение 1-й степени",
           (35, 40): "Ожирение 2-й степени",
           (40, 999): "Ожирение 3-й степени",
}

db = []

count_1 = 0
def main(request):
    global count_1
    count_1 += 1
    context = {"count" : count_1}
    global interpretation
    global db
    if request.method == "POST":
        print(request.POST)
        form = forms.Registration(request.POST)
        if form.is_valid():
            print("ok")
            name = form.cleaned_data['name']
            years = int(form.cleaned_data['years'])
            weight = float(form.cleaned_data['weight'])
            height = float(form.cleaned_data['height'])
            size = form.cleaned_data['size']
            height /= 100
            bmi = weight / height ** 2
            db.append((bmi, years))
            sum = 0
            for elem in db:
                sum += elem[0]
            mean = sum / len(db)
            imt = bmi / mean - 1
            print(imt)


            for r, inter in interpretation.items():
                if r[0] <= bmi < r[1]:
                    res = inter
                    print(res)
                    break
            else:
                res = 'WTF'
            context["result"] = res
            context["user"] = (name, years, weight, height, size, imt)

            template = loader.get_template("main.html")
            return HttpResponse(template.render(context, request))
    template = loader.get_template("main.html")
    context["form"] = forms.Registration()
    return HttpResponse(template.render(context, request))

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
