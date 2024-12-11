from django import template
register = template.Library()


@register.filter(name="add_attr")
def add_attr(fields, css):
    attrs = {}
    clase, valor = css.split(':')
    attrs[clase] = valor
    return fields.as_widget(attrs=attrs)
