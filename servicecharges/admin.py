from mediguest_admin.site import mediguest_admin_site
from models import ServiceChargeType, ServiceCharge, ServiceChargePayment
from django.contrib import admin

class ServiceChargesInline(admin.TabularInline):
    model = ServiceCharge
    extra = 0

    def get_formset(self, request, obj=None, **kwargs):
        """
        Enable formfield_for_foreign key to be given obj instance
        """
        from django.utils.functional import curry
        return super(ServiceChargesInline, self).get_formset(request, obj=obj,
            formfield_callback=curry(self.formfield_for_foreignkey, request=request, obj=obj)
        )
    
    def formfield_for_foreignkey(self, field, request, **kwargs):
        """
        Filter only discounts which are currently applicable
        """
        from booking.models import Booking
        if field.name == 'related_booking':
            if kwargs['obj'] is not None:
                kwargs['queryset'] = Booking.objects.filter(client=kwargs['obj'].client)
        del kwargs['obj']
        return super(ServiceChargesInline, self).formfield_for_foreignkey(field, request, **kwargs)

class ServiceChargePaymentsInline(admin.TabularInline):
    model = ServiceChargePayment
    extra = 0

    def get_formset(self, request, obj=None, **kwargs):
        """
        Enable formfield_for_foreign key to be given obj instance
        """
        from django.utils.functional import curry
        return super(ServiceChargePaymentsInline, self).get_formset(request, obj=obj,
            formfield_callback=curry(self.formfield_for_foreignkey, request=request, obj=obj)
        )
    
    def formfield_for_foreignkey(self, field, request, **kwargs):
        """
        Filter only discounts which are currently applicable
        """
        from models import ServiceCharge
        if field.name == 'service_charge':
            if kwargs['obj'] is not None:
                kwargs['queryset'] = ServiceCharge.objects.filter(client=kwargs['obj'].client)
        del kwargs['obj']
        return super(ServiceChargePaymentsInline, self).formfield_for_foreignkey(field, request, **kwargs)

mediguest_admin_site.register(ServiceChargeType)
mediguest_admin_site.register(ServiceCharge)
mediguest_admin_site.register(ServiceChargePayment)

