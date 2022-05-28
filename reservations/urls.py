from django.urls import path

from reservations.views import ReservationPage, PrintTicket,GenerateTicketPdf

urlpatterns = [
    path('ReservationPage/<int:pk>/', ReservationPage.as_view(), name='ReservationPage'),
    path('PrintTicket/<int:pk>/', PrintTicket.as_view(), name='PrintTicket'),
    path('GenerateTicketPdf/<int:pk>/', GenerateTicketPdf, name='GenerateTicketPdf'),
]
