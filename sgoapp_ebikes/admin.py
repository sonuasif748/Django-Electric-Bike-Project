from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import cust,dealer,bike
from .models import *
from .models import bookbike,shopnames,estimatekms

admin.site.register(bookbike)
admin.site.register(shopnames)
admin.site.register(estimatekms)
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(cust, CustomerAdmin)
class dealerAdmin(admin.ModelAdmin):
    pass
admin.site.register(dealer, dealerAdmin)


class bikeAdmin(admin.ModelAdmin):
    pass
admin.site.register(bike, bikeAdmin)



class AdminKilometers(admin.ModelAdmin):
    pass
class AdminRecharge(admin.ModelAdmin):
    pass

class Battery_statusAdmin(admin.ModelAdmin):
    pass
admin.site.register(Battery_status, Battery_statusAdmin)

class SpeedometerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Speedometer, SpeedometerAdmin)

class LockUnlockAdmin(admin.ModelAdmin):
    pass
admin.site.register(LockUnlock, LockUnlockAdmin)

class BikesalesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Bikesales, BikesalesAdmin)


admin.site.register(kilometers,AdminKilometers)
admin.site.register(Recharge,AdminRecharge)