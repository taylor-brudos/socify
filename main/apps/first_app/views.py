from django.shortcuts import render, HttpResponse, redirect
from django.template import loader, Context
import openpyxl
import os

def index(request):
    context = {
        "email" : "blog@gmail.com",
        "name" : "mike"
    }
    return render(request, "first_app/index.html", context)
    
def generate(request):
    if request.method == "POST":
        print("*"*50 + "   Generate method invoked!")
        print(os.getcwd())
        wb = openpyxl.Workbook()
        sheet = wb.active
        sheet.title = "WP-01"
        wb.save('testWorkPaper.xlsx')
        file_path = 'testWorkPaper.xlsx'
        response = HttpResponse(open(file_path, 'rb').read())
        response['Content-Type'] = 'mimetype/submimetype'
        response['Content-Disposition'] = 'attachment; filename=testWPdwnld.xlsx'
        return response
    else:
        return redirect("/")