from django.contrib import admin

from py_card.core.models import CreditCard

admin.site.site_header = "PyCard"
admin.site.site_title = "PyCard"
admin.site.index_title = "PyCard Administration"


class CreditCardAdmin(admin.ModelAdmin):
    list_display = ("number", "holder", "get_month_year", "cvv", "brand")
    search_fields = ("number", "holder", "exp_date", "cvv", "brand")
    ordering = ("number",)

    @admin.display(description="Expiration Date")
    def get_month_year(self, obj):
        return obj.exp_date.strftime("%m/%Y")


admin.site.register(CreditCard, CreditCardAdmin)
