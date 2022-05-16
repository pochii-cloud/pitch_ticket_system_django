from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from core.forms import AddFixtureForm
from core.models import Field, Team, Contact, Fixture
from core.printpdf import html_to_pdf


class Homepage(TemplateView):
    template_name = 'index.html'


class ContactUs(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact()
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        messages.info(request, 'message sent successfully')
        return render(request, 'contact.html')


class FixturesPage(TemplateView):
    template_name = 'Fixtures.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fixtures'] = Fixture.objects.all()
        return context


class AboutUs(TemplateView):
    template_name = 'About.html'


class AdminPage(TemplateView):
    template_name = 'AdminPage.html'


class AddField(View):
    def get(self, request):
        return render(request, 'addfield.html')

    def post(self, request):
        field_name = request.POST.get('field_name')
        field_location = request.POST.get('field_location')
        field_capacity = request.POST.get('field_capacity')
        field = Field()
        field.name = field_name
        field.location = field_location
        field.capacity = field_capacity
        field.save()
        messages.info(request, 'field added successfully')
        return render(request, 'addfield.html')


class AddFixture(View):
    def get(self, request):
        form = AddFixtureForm(request.POST)
        return render(request, 'AddFixture.html', {'form': form})

    def post(self, request):
        form = AddFixtureForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Fixture added successfully')
        return render(request, 'AddFixture.html', {'form': form})


class AddTeam(View):
    def get(self, request):
        return render(request, 'AddTeam.html')

    def post(self, request):
        team_name = request.POST.get('team_name')
        team_slogan = request.POST.get('team_slogan')
        team = Team()
        team.name = team_name
        team.slogan = team_slogan
        team.save()
        messages.info(request, 'team added successfully')
        return render(request, 'AddTeam.html')


class FixtureDetail(TemplateView):
    template_name = 'Fixture_Details.html'

    def get_context_data(self, **kwargs):
        context = super(FixtureDetail, self).get_context_data(**kwargs)
        context['fixtures'] = Fixture.objects.get(pk=self.kwargs.get('pk'))
        return context


class MakeReservation(View):
    def get(self, request, pk):
        fixtures = Fixture.objects.get(pk=pk)
        if not fixtures.Booked:
            fixtures.Booked = True
            fixtures.Ground.capacity = - 1
            fixtures.save()
            messages.info(request, 'Your reservation made successfully!!')
        else:
            messages.info(request, 'Your reservation is already made!!')
        return render(request, 'MakeReservation.html')

    def post(self, request):
        return render(request, 'MakeReservation.html')


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        # getting the template
        pdf = html_to_pdf('MakeReservation.html')

        # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')