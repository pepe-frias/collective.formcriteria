from Products.ATContentTypes.criteria import path

from collective.formcriteria.criteria import common

class PathFormCriterion(
    common.FormCriterion, path.ATPathCriterion):
    __doc__ = path.ATPathCriterion.__doc__

    schema = path.ATPathCriterion.schema.copy(
        ) + common.FormCriterion.schema.copy()
    schema['value'].widget.hide_form_label = True
    schema['formFields'].vocabulary = common.makeVocabularyForFields(
        schema['value'], schema['recurse'])
    schema['formFields'].widget.format = 'checkbox'

common.replaceCriterionRegistration(
    path.ATPathCriterion, PathFormCriterion)
