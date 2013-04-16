from collective.behavior.sku import _
from zope import schema
from plone.supermodel.model import Schema


class ISKU(Schema):
    """Interface for SKU behavior."""

    sku = schema.TextLine(
        title=_(u"SKU"),
        description=_(u"Unique ID for Stock Keeping Unit."))
