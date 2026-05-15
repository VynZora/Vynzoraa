import re

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='bold_to_inline_h3')
def bold_to_inline_h3(value):
    if not value:
        return value

    # Replace paragraph wrappers so inline <h3> does not create invalid HTML nesting.
    value = re.sub(r'<p\b[^>]*>', '<div class="seo-p-wrapper">', value, flags=re.IGNORECASE)
    value = re.sub(r'</p>', '</div>', value, flags=re.IGNORECASE)

    # Convert non-empty <strong>/<b> tags into inline SEO headings.
    pattern = r'<(strong|b)>\s*(.+?)\s*</\1>'
    replacement = r'<h3 class="seo-h3">\2</h3>'
    modified_html = re.sub(pattern, replacement, value, flags=re.IGNORECASE | re.DOTALL)

    return mark_safe(modified_html)
