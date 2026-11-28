from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from experts.models import ExpertsListing


# Create your views here.
class ExpertsListingListView(ListView):
    model = ExpertsListing
    context_object_name = 'experts_listing'
    template_name = 'experts/listing.html'
    paginate_by = 12
    paginate_orphans = 5

    def get_queryset(self):
        query = super().get_queryset()
        search_query = self.request.GET.get('q', '').strip()

        if search_query:
            query = query.filter(Q(title__icontains=search_query)| Q(profile__user__first_name__icontains=search_query))

        selected_category = self.request.GET.get('category')

        if selected_category:
            query = query.prefetch_related('specialization').filter(specialization__category__iexact=selected_category)


        return query
