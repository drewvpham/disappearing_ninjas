from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'disappearing_ninjas/index.html')

def show_ninja(request, color):
	#ninja got passed in through the url parameter!
    if color in ['blue','red','orange','purple']:
        turtle=color
        context = {'img' : turtle}
    else:
        turtle='notapril'
        context = {'img' : turtle}

    return render(request, 'disappearing_ninjas/ninjas.html', context)
