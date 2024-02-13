from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(CategoryMaster)
admin.site.register(ColorMasterData)
admin.site.register(ColorVariants)
admin.site.register(SizeMasterData)
admin.site.register(SizeVariants)
admin.site.register(Coupon)


class ColorAdmin(ColorVariants):

    @admin.display(description="categories")
    def get_categories(self):
        return [category.name for category in self.categories.all()]
