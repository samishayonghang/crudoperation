from django.shortcuts import render,redirect,get_object_or_404
from.forms import ReviewForm,LoginForm,SignupForm
from.models import Review,Authentic
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/signup/")
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

def loginpage(request):
    form=LoginForm()
    if request.method=="POST":
     
      username=request.POST.get('username')
      password=request.POST.get('password')
      if not User.objects.filter(username=username).exists():
          messages.error(request,'Invalid Username')
          return redirect('loginpage')
      user=authenticate(username=username,password=password)
      if user is None:
          messages.error(request,'Invalid password')
          return redirect('loginpage')
      
          
          
      else:
         
         login(request,user)
         return redirect('reviews')
      
    return render(request,'Book/login.html',{'form':form})
   
  
def signup(request):
   if request.method=="POST":
      first_name=request.POST.get('first_name')
      last_name=request.POST.get('last_name')
      username=request.POST.get('username')
      password=request.POST.get('password')
      email=request.POST.get('email')

      user=User.objects.filter(username=username)
      if user.exists():
         messages.info(request,'username already exists')
         return redirect('register')

      user=User.objects.create(
         first_name=first_name,
         last_name=last_name,
         username=username,
         password=password,
         email=email
      )
      user.set_password(password)
      user.save()
      messages.info(request,'Account created Sucessfully')
      
      return redirect('loginpage')
      



   else:

         user=SignupForm()

   return render(request,'Book/register.html',{'user':user})


def logoutpage(request):
   logout(request)
   return redirect('loginpage')