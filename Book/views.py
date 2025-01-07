from django.shortcuts import render,redirect,get_object_or_404
from.forms import ReviewForm
from.models import Review

# Create your views here.
def Reviews(request):
    if request.method=="POST":
     form=ReviewForm(request.POST)
     if form.is_valid():
        form.save()
        return redirect("genre")
    else:
       form=ReviewForm()
    return render(request,"Book/index.html",{'form':form})

def Genre(request):
     books=Review.objects.all()
    # genre=request.GET.get('Genre','')

     #if genre=="fiction":
       # books=books.filter(genre='fiction')
        #return books
     #else:
        #  form=ReviewForm()

    
     return render(request,"Book/genre.html",{'books':books})
    


def update(request,pk):
   review=get_object_or_404(Review,pk=pk)
   if request.method=="POST":
      form=ReviewForm(request.POST,instance=review)
      if form.is_valid():
         form.save()
         return redirect('genre')
   else:
      form=ReviewForm(instance=review)

   return render(request,'Book/update.html',{'form':form})

def delete(request,pk):
   review=get_object_or_404(Review,pk=pk)
   
   review.delete()
   return redirect ('genre')

def search(request):
   query=request.GET.get('query','')
   reviews=Review.objects.all()
   if query:
     reviews=Review.objects.filter(Title__icontains=query)
   else:
      reviews=Review.objects.none
   context={
      'reviews':reviews,
      'query':query
   }
   return render(request,'Book/search.html',context)