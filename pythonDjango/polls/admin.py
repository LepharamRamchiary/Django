from django.contrib import admin
from .models import TeaVarity, TeaReview, TeaCertificate, Store

# Register your models here.
class TeaReviewInline(admin.TabularInline):
    model = TeaReview
    extra = 2

class TeaVarityAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "price", "date_added")
    inlines = [TeaReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ("name", "location")
    filter_horizontal = ("tea_varieties",)

class TeaCertificateAdmin(admin.ModelAdmin):
    list_display = ("tea", "certificate_number")


admin.site.register(TeaVarity, TeaVarityAdmin)
# admin.site.register(TeaReview, TeaReviewInline)
admin.site.register(TeaCertificate, TeaCertificateAdmin)
admin.site.register(Store, StoreAdmin)
