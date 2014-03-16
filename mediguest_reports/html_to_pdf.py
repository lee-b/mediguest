import settings
import cStringIO as StringIO
import os

def _fetch_resources(uri, rel):
    """Return local filepaths for the URIs present in HTML files"""

    if uri.startswith(settings.STATIC_URL):
        path = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ""))

    elif uri.startswith(settings.MEDIA_URL):
        path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))

    path = os.path.abspath(path)

    return path

class PDFRenderer(object):
    def __call__(self, request, template_src, context_dict):
        raise NotImplementedError()

    def _render_template(self, request, template_src, context_dict):
        from django.template.loader import get_template
        from django.template import RequestContext

        template = get_template(template_src)
        context = RequestContext(request, context_dict)
        html = template.render(context)

        return html

class PISA_PDFRenderer(PDFRenderer):
    """Convert HTML to PDF using the Python PISA library."""

    def __call__(self, request, template_src, context_dict):
        import ho.pisa as pisa

        html = self._render_template(request, template_src, context_dict)
        result = StringIO.StringIO()

        pdf = pisa.pisaDocument(
                StringIO.StringIO(html.encode("UTF-8")),
                result,
                link_callback = _fetch_resources,
        )

        if pdf.err:
            # FIXME: should throw an exception here, instead of just returning 
            #        an error string
            err_msg = "ERROR: PDF generation failed, please contact your IT Administrator! %s" % cgi.escape(html)
            return err_msg

        return result.getvalue()

class WKHTMLToPDF_PDFRenderer(PDFRenderer):
    """Render HTML to PDF using wkhtmltopdf.  Note: this is mostly a proof of
    concept: we don't (yet?) generate HTML compatible with this, and
    wkhtmltopdf is too limited anyway."""

    def __call__(self, request, template_src, context_dict):
        import tempfile

        html = self._render_template(request, template_src, context_dict)

        tmp_html_fd, tmp_html_fname = tempfile.mkstemp(prefix='kintassa_mediguest_db', suffix='html')
        tmp_html_file = os.fdopen(tmp_html_fd, 'w')
        tmp_html_file.write(html.encode("UTF-8"))
        tmp_html_file.close()

        tmp_pdf_fd, tmp_pdf_fname = tempfile.mkstemp(prefix='kintassa_mediguest_db', suffix='pdf')
        os.close(tmp_pdf_fd)

        rc = os.system("wkhtmltopdf --ignore-load-errors '%s' '%s'" % (tmp_html_fname,tmp_pdf_fname))

        os.unlink(tmp_html_fname)

        if rc == 0:
            tmp_pdf_file = open(tmp_pdf_fname, 'rb')
            pdf_buf = tmp_pdf_file.read()
            print pdf_buf
            tmp_pdf_file.close()
        else:
            pdf_buf = u""

        os.unlink(tmp_pdf_fname)
        return pdf_buf

