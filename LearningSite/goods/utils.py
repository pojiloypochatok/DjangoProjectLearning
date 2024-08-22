from django.contrib.postgres.search import SearchVector, SearchRank, SearchQuery

from .models import Products


def q_search(request):
    query = request.GET.get('q')
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    vector = SearchVector("name", "description")
    query = SearchQuery(query)

    return Products.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank")
