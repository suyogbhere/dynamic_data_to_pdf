from django.shortcuts import render, HttpResponse
from myapp.models import Student
from myapp.forms import StudentForm
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.
def home(request):
    stu = Student.objects.all()
    context ={
        'student': stu
    }
    return render(request, 'pdf_convert/home.html',context)


def pdf_report_create(request):
    stu = Student.objects.all()
    template_path = 'pdf_convert/pdf_report.html'
    context = {'student': stu}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="student_report.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    #create pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    #if error then show some view
    if pisa_status.err:
        return HttpResponse('We had some errors <prev>' + html+ '</prev>')
    return response