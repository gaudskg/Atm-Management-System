import pandas as pd
from django.shortcuts import render, redirect, get_object_or_404
from .models import ATMSite, State, City
from .forms import ATMSiteForm

#import ATM sites from an Excel file
def import_atm_sites(request):
    if request.method == 'POST':
        # Get the uploaded file# Get the uploaded file
        file = request.FILES['file']
        # Read the file using pandas
        df = pd.read_excel(file,engine='openpyxl')
        for index, row in df.iterrows():
            # Get the data from each column of the row
            name = row['Name']
            id = row['ID']
            address = row['Address']
            state_name = row['State']
            city_name = row['City']
            person_name = row['Person Name']
            phone = row['Phone']
            email = row['Email']

            # Get or create State and City objects
            state, _ = State.objects.get_or_create(name=state_name)
            city, _ = City.objects.get_or_create(name=city_name, state=state)

            # Create ATMSite object
            ATMSite.objects.create(
                name=name,
                site_id=id,
                address=address,
                city=city,
                contact_details={
                    'person_name': person_name,
                    'phone': phone,
                    'email': email,
                }
            )

        return render(request, 'import_atm_sites_done.html')

    return render(request, 'import_atm_sites.html')


# display the list of ATMs
def atm_list(request):
    atms = ATMSite.objects.all()
    return render(request, 'atm_list.html', {'atms': atms})

# display the form for editing an ATM
def atmupdate(request, pk):
    atm = get_object_or_404(ATMSite, pk=pk)
    if request.method == 'POST':
        form = ATMSiteForm(request.POST, instance=atm)
        if form.is_valid():
            form.save()
            return redirect('atm_list')
    else:
        form = ATMSiteForm(instance=atm)
    return render(request, 'atm_form.html', {'form': form, 'title': 'Edit ATM Site'})

# to confirm the deletion of an ATM
def atmdelete(request, pk):
    atm = get_object_or_404(ATMSite, pk=pk)
    if request.method == 'POST':
        atm.delete()
        return redirect('atm_list')
    return render(request, 'atm_confirm_delete.html', {'atm': atm})

# display the details of an ATM
def atmview(request, pk):
    atm = get_object_or_404(ATMSite, pk=pk)
    return render(request, 'atm_view.html', {'atm': atm})