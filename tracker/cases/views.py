from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'cases/index.html')

def track(request, *args):

    v1 = request.POST['c1']
    v2 = request.POST['c2']

    l1 = v1.split()
    l2 = v2.split()

    if l1==l2:
        my_context = {
            'msg1': 'Congratulations! No leakage in your cases.'
        }

    elif l1!=l2:
        if len(l1)<len(l2):
            my_context = {
                'result': set(l2).difference(l1),
                'msg': 'Hey, the below-mentioned noted cases are either leaked from your bin or in open status:-'
            }
        # result = ", ".join(n) We can also use it if we need he cases separated by comma and not the table.
        if len(l1) > len(l2):
            if (all(x in l1 for x in l2)):
                my_context = {
                'result': set(l1).difference(l2),
                'msg': 'Hurray!!! NO LEAKAGE but I can see you have more cases in your bin compare to the noted cases which are:-'
            }

            else:
                my_context = {
                    'result': set(l2).difference(l1),
                    'msg': 'Here are the cases which are leaked:-'
                }


        if len(l1)==len(l2):
            my_context = {
                'result': set(l2).difference(l1),
                'msg': 'Hey, the below-mentioned noted cases are either leaked from your bin or in open status:-'
            }

    return render(request, 'cases/result.html', my_context)





