from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from smart_settings import Namespace

namespace = Namespace(name='document_parsing', label=_('Document parsing'))

setting_auto_parsing = namespace.add_setting(
    global_name='DOCUMENT_PARSING_AUTO_PARSING', default=True,
    help_text=_(
        'Set new document types to perform parsing automatically by default.'
    )
)
setting_pdftotext_path = namespace.add_setting(
    global_name='DOCUMENT_PARSING_PDFTOTEXT_PATH',
    default='/usr/bin/pdftotext',
    help_text=_(
        'File path to poppler\'s pdftotext program used to extract text '
        'from PDF files.'
    ),
    is_path=True
)
