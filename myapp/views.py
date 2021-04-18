from django.shortcuts import render
from .models import inputFields
import csv
from django.http import HttpResponse
import xlwt
# Create your views here.

def home(request):
    return render(request, 'index.html')


def input(request):
    var1 = request.POST.get('environment')
    var2 = request.POST.getlist('country')
    request.session['environment'] = var1
    request.session['country'] = var2
    for i in var2:
        inputField = inputFields.objects.filter(environment=var1, country=i)
        return render(request, 'input.html', {'inputField': inputField})

def export_users_csv(request):
    
    var1 = request.session['environment']
    var2 = request.session['country']

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="{}.csv"'.format(var1+'-'+var2)
    
    '''response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="{}.xls"'.format(var1+'-'+var2)

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('{}'.format(var1+'-'+var2))

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Country', 'Environment', 'Component', 'Start Time', 'End Time', 'Total time taken']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows = inputFields.objects.filter(environment=var1, country=var2).values_list('country', 'environment', 'component', 'start', 'end', 'total')

    for row in rows:
        row_num =row_num + 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)'''

    writer = csv.writer(response)
    writer.writerow(['Country', 'Environment', 'Component', 'Start Time', 'End Time', 'Total time taken'])

    results = inputFields.objects.filter(environment=var1, country=var2).values_list('country', 'environment', 'component', 'start', 'end', 'total')
    for result in results:
        writer.writerow(result)

    
    return response
