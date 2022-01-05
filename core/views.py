from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse("<h1>Hello {} e você tem {}</h1>".format(nome, idade))

def soma(request, num1, num2):
    return HttpResponse("<h1> os números informados são {} e {}</h1>".format(num1, num2) + "<h1>E a soma dos números é igual = {}</h1>".format(num1+num2))

def subtracao(request, num1, num2):
    return HttpResponse("<h1> os números informados são {} e {}</h1>".format(num1, num2) + "<h1>E a subtração dos números é igual = {}</h1>".format(num1-num2))

def multiplicacao(request, num1, num2):
    return HttpResponse("<h1> os números informados são {} e {}</h1>".format(num1, num2) + "<h1>E a multiplicação dos números é igual = {}</h1>".format(num1*num2))

def divisao(request, num1, num2):
    return HttpResponse("<h1> os números informados são {} e {}</h1>".format(num1, num2) + "<h1>E a divisão dos números é igual = {}</h1>".format(num1/num2))
