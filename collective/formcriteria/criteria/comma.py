from Products.Archetypes import atapi
from Products.ATContentTypes import criteria

from collective.formcriteria.criteria import list as list_

class CommaWidget(atapi.LinesWidget):
    _properties = atapi.LinesWidget._properties.copy()
    _properties.update({
        'macro' : "comma_widget",
        'size' : '30',
        'maxlength' : '255',
        'blurrable' : True,
        'show_form_help': True,
        })

    def process_form(self, *args, **kw):
        result = super(CommaWidget, self).process_form(
            *args, **kw)
        if not isinstance(result, tuple):
            return result

        value, mutator_kw = result
        value = [item.strip() for item in value.split(',')]
        return value, mutator_kw

class ATCommaCriterion(list_.ATListCriterion):
    """A comma separated criterion"""

    archetype_name = 'Comma Separated Criterion'
    shortDesc = 'Enter comma separated values'

    schema = list_.ATListCriterion.schema.copy()
    schema['value'].widget = CommaWidget(
        label=schema['value'].widget.label,
        description=u'Values, separated by commas.',
        hide_form_label=True)

criteria.registerCriterion(
    ATCommaCriterion,
    criteria._criterionRegistry.indicesByCriterion(
        list_.ATListCriterion.meta_type))
