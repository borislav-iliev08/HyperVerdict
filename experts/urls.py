from django.urls import path

from experts.views import ExpertsListingListView

urlpatterns=[
    path('',ExpertsListingListView.as_view(),name='listing'),

]