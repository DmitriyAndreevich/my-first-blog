from django.shortcuts import redirect
from django.shortcuts import render
from .forms import ContactForm

def index(request):
  
    return render(request, 'site/index.html')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'site/contact.html', {'form': form})
  

def about(request):
  
    return render(request, 'site/about.html')

def page(request):
  
    return render(request, 'site/page.html')

def success(request):
  
    return render(request, 'site/success.html')


