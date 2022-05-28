from django.urls import path

from core.views import *

urlpatterns = [
    path('', Homepage.as_view(), name='Homepage'),
    path('FixturesPage/', FixturesPage.as_view(), name='FixturesPage'),
    path('AdminPage/', AdminPage.as_view(), name='AdminPage'),
    path('AddField/', AddField.as_view(), name='AddField'),
    path('UpdateField/<int:pk>/', UpdateField.as_view(), name='UpdateField'),
    path('DeleteField/<int:pk>/', DeleteField.as_view(), name='DeleteField'),
    path('AddFixture/', AddFixture.as_view(), name='AddFixture'),
    path('FixtureDetail/<int:pk>/', FixtureDetail.as_view(), name='FixtureDetail'),
    path('UpdateFixture/<int:pk>/', UpdateFixture.as_view(), name='UpdateFixture'),
    path('DeleteFixture/<int:pk>/', DeleteFixture.as_view(), name='DeleteFixture'),
    path('AddTeam/', AddTeam.as_view(), name='AddTeam'),
    path('ContactUs/', ContactUs.as_view(), name='ContactUs'),
    path('AboutUs/', AboutUs.as_view(), name='AboutUs'),
]
