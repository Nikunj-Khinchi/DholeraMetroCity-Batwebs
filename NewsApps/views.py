from django.shortcuts import render

# Create your views here.
def index(request):
    
    image_range = range(1, 53)  # Generate a range from 1 to 20
    context = {'image_range': image_range}
    return render(request , 'news-pages/index.html' , context)