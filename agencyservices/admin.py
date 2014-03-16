from mediguest_admin.site import mediguest_admin_site
from models import GP, HealthProvider

mediguest_admin_site.register(GP)
mediguest_admin_site.register(HealthProvider)


