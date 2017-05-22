from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'disappearing_ninjas/index.html')

def show_ninja(request, color):
    image_path = "disappearing_ninjas/img/"
	#ninja got passed in through the url parameter!
    if color in ['blue','red','orange','purple']:
        image_path += color

    else:
        image_path += 'notapril'
    context = {'img' : image_path + '.jpg'}

    return render(request, 'disappearing_ninjas/ninjas.html', context)
