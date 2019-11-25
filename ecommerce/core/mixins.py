from ecommerce.core.models import Category


class ExtraContextMixin(object):
    def get_context_data(self):
        context = super().get_context_data()
        context.update({
            "categories": Category.objects.all()
        })
        return context
