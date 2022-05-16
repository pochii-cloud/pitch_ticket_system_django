from django.urls import path

from core.views import *

urlpatterns = [
    path('', Homepage.as_view(), name='Homepage'),
    path('FixturesPage/', FixturesPage.as_view(), name='FixturesPage'),
    path('AdminPage/', AdminPage.as_view(), name='AdminPage'),
    path('AddField/', AddField.as_view(), name='AddField'),
    path('AddFixture/', AddFixture.as_view(), name='AddFixture'),
    path('FixtureDetail<int:pk>/', FixtureDetail.as_view(), name='FixtureDetail'),
    path('MakeReservation/<int:pk>/', MakeReservation.as_view(), name='MakeReservation'),
    path('Pdf/', GeneratePdf, name='GeneratePdf'),
    path('AddTeam/', AddTeam.as_view(), name='AddTeam'),
    path('ContactUs/', ContactUs.as_view(), name='ContactUs'),
    path('AboutUs/', AboutUs.as_view(), name='AboutUs'),
]
