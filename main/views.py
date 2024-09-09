from django.shortcuts import render

def show_main(request):
    context = {
        'app_name' : 'snowpy',
        'name': 'Olav Dendy Christian Manullang',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
