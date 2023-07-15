from django.shortcuts import render

# Create your views here.
def index(request):
   
    return render(request  , 'photo-pages/photo-gallery.html' , )


def Investors(request):
    PngRange = range(1,23)
    JpgRange = range(1,179)
    
    return render(request , 'photo-pages/investor-visit.html' , {
        'PngRange': PngRange,
        'JpgRange' : JpgRange 
    })
    
def Feedback(request):
    JpgRange = range(1,20)
    
    return render(request , 'photo-pages/investor-feedback.html' , {
          'JpgRange' : JpgRange 
    })
    
def DMCSite(request):
    image_range = range(1, 42)  # Generate a range from 1 to 20
    JpgImage = range(1,34)
    context = {'image_range': image_range,
               'JpgImage' : JpgImage
                }
    return render(request  , 'photo-pages/index.html' , context)

def Dholera_images(request):
    Dholeraimages = range(1, 10)
    return render(request , 'photo-pages/dholeraMetro.html' , {
        'Dholeraimages' :Dholeraimages
    })
    
def Summit_2017(request):
    SummitImages = range(2,19)
    
    return render(request , 'photo-pages/summit-2017.html' , {
        'SummitImages' :SummitImages
    })
    
def Summit_2018(request): 
    SummitImages = range(1,21)
    
    return render(request , 'photo-pages/summit-2018.html' , {
        'SummitImages' :SummitImages
    })
    
def VideoGallery(request):
    return render(request , 'photo-pages/video-gallery.html')