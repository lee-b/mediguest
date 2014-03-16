from django.contrib.admin.widgets import AdminFileWidget
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe
import os
from PIL import Image

class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []

        if value and getattr(value, "url", None):
            image_url = value.url
            file_name=str(value)

            # defining the size
            x, y = (100, 100)
            size="%dx%d" % (x,y)

            # defining the filename and the miniature filename
            filehead, filetail  = os.path.split(value.path)
            basename, format    = os.path.splitext(filetail)
            miniature           = basename + '_' + size + format
            filename            = value.path
            miniature_filename  = os.path.join(filehead, miniature)
            filehead, filetail  = os.path.split(value.url)
            miniature_url       = filehead + '/' + miniature

            # make sure that the thumbnail is a version of the current original sized image
            if os.path.exists(miniature_filename) and os.path.getmtime(filename) > os.path.getmtime(miniature_filename):
                os.unlink(miniature_filename)

            # if the image wasn't already resized, resize it
            if not os.path.exists(miniature_filename):
                image = Image.open(filename)
                image.thumbnail((x, y), Image.ANTIALIAS)
                try:
                    image.save(miniature_filename, image.format, quality=90, optimize=1)
                except:
                    image.save(miniature_filename, image.format, quality=90)

            output.append(u' <div><a href="%s" target="_blank"><img src="%s" alt="%s" /></a></div> %s ' % \
            (miniature_url, miniature_url, miniature_filename, _('Change:')))

        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))

