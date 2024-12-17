# api/mixins.py

class FilterByNameMixin:
    """
    Mixin to filter a queryset by 'name'
    """
    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset
