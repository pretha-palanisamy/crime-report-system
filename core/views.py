from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Crime
from .forms import CrimeForm
from django.db.models import Q  # idha top la import pannu
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate,login
from django.contrib.auth import views as auth_views

def my_login(request):  # <- idhu illama dhan error
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'core/login.html')

@login_required
def home(request):
    status_filter = request.GET.get('status', 'All') 
    search_query = request.GET.get('q', '')

    crimes = Crime.objects.all().order_by('-date_reported')

    if status_filter != 'All':
        crimes = crimes.filter(status=status_filter)

    if search_query:
        crimes = crimes.filter(
            Q(location__icontains=search_query) | 
            Q(description__icontains=search_query) |
            Q(crime_type__icontains=search_query)
        )

    # Ithu pudhu - Statistics
    total_crimes = Crime.objects.count()
    pending_crimes = Crime.objects.filter(status='Pending').count()
    under_crimes = Crime.objects.filter(status='Under Investigation').count()
    solved_crimes = Crime.objects.filter(status='Solved').count()

    return render(request, 'core/home.html', {
        'crimes': crimes,
        'status_filter': status_filter,
        'search_query': search_query,
        'total_crimes': total_crimes,
        'pending_crimes': pending_crimes,
        'under_crimes': under_crimes,
        'solved_crimes': solved_crimes,
    })


@login_required
def report_crime(request):
    if request.method == 'POST':
        form = CrimeForm(request.POST,request.FILES)
        if form.is_valid():
            crime = form.save(commit=False)
            crime.reported_by = request.user
            crime.save()
            return redirect('home')
    else:
        form = CrimeForm()

    return render(request, 'core/report.html', {'form':form
    })

@login_required
def edit_crime(request, crime_id):
    crime = get_object_or_404(Crime, id=crime_id, reported_by=request.user)
    
    if request.method == 'POST':
        form = CrimeForm(request.POST, instance=crime)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CrimeForm(instance=crime)

    return render(request, 'core/report.html', {'form':form,'crime':crime
    })

@login_required
def delete_crime(request, crime_id):
    crime = get_object_or_404(Crime, id=crime_id, reported_by=request.user)
    crime.delete()
    return redirect('home')
@login_required
def crime_detail(request, crime_id):
    crime = get_object_or_404(Crime, id=crime_id)
    return render(request, 'core/crime_detail.html', {'crime': crime})