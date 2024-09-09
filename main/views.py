from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306230590',
        'name': 'Olav Dendy Christian Manullang',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
