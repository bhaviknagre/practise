from django.urls import path
from .views import *

urlpatterns = [
    path('cases/', CaseListCreateAPIView.as_view(), name='case-list-create'),
    path('cases/<int:pk>/', CaseDetailAPIView.as_view(), name='case-detail'),

    path('statuses/', CaseStatusListCreateAPIView.as_view(), name='status-list-create'),
    path('statuses/<int:pk>/', CaseStatusDetailAPIView.as_view(), name='status-detail'),

    path('types/', CaseTypeListCreateAPIView.as_view(), name='type-list-create'),
    path('types/<int:pk>/', CaseTypeDetailAPIView.as_view(), name='type-detail'),

    path('payments/', PaymentStatusListCreateAPIView.as_view(), name='payment-list-create'),
    path('payments/<int:pk>/', PaymentStatusDetailAPIView.as_view(), name='payment-detail'),

    path('opposing-parties/', OpposingPartyListCreateAPIView.as_view(), name='opposing-party-list-create'),
    path('opposing-parties/<int:pk>/', OpposingPartyDetailAPIView.as_view(), name='opposing-party-detail'),

    path('courts/', CourtListCreateAPIView.as_view(), name='court-list-create'),
    path('courts/<int:pk>/', CourtDetailAPIView.as_view(), name='court-detail'),

    path('judges/', JudgeListCreateAPIView.as_view(), name='judge-list-create'),
    path('judges/<int:pk>/', JudgeDetailAPIView.as_view(), name='judge-detail'),
]
