from django.contrib import messages
from django.http import FileResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import TemplateView
from fpdf import FPDF

from core.forms import ReservationForm
from core.models import Fixture
from reservations.models import Reservation


class ReservationPage(View):
    def get(self, request, pk):
        form = ReservationForm(request.POST)
        return render(request, 'MakeReservation.html', {'form': form})

    def post(self, request, pk):
        form = ReservationForm(request.POST)
        fixture = Fixture.objects.get(pk=pk)
        form.instance.fixture = fixture
        if form.is_valid():
            form.save()
        if not fixture.Booked:
            persons = form.cleaned_data.get('persons')
            fixture.Ground.capacity -= persons
            fixture.Ground.save()
        elif fixture.Booked:
            persons = form.cleaned_data.get('persons')
            fixture.Ground.capacity -= persons
            fixture.Ground.save()
            messages.info(request, 'reservation made.You can print ticket now')
            return redirect('PrintTicket', pk=pk)
        return render(request, 'MakeReservation.html', {'form': form})


class PrintTicket(TemplateView):
    template_name = 'PrintTicket.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reservation'] = Reservation.objects.get(pk=self.kwargs.get('pk'))
        return context


def GenerateTicketPdf(request, pk):
    reservation = Reservation.objects.get(pk=pk)
    details = [
        {"item": "Ticket for:", "details": "reservations.fixture"},
        {"item": "Fixture", "details": "reservation.fixture"},
        {"item": "persons", "details": "reservation.persons"},
        {"item": "stadium", "details": "reservation.fixture.Ground.name"},
    ]
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('courier', 'B', 16)
    pdf.cell(40, 10, 'EazyTicket for you:', 0, 1)
    pdf.cell(40, 10, '', 0, 1)
    pdf.set_font('courier', '', 12)
    pdf.cell(200, 8, f"{'Item'.ljust(30)} {'Details'.rjust(20)}", 0, 1)
    pdf.line(10, 30, 150, 30)
    pdf.line(10, 38, 150, 38)
    for line in details:
        pdf.cell(200, 8, f"{line['item'].ljust(30)} {line['details']}", 0, 1)
    pdf.output('report.pdf', 'F')
    return FileResponse(open('report.pdf', 'rb'), as_attachment=True, content_type='application/pdf')
