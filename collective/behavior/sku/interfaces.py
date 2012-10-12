from collective.behavior.sku import _
from zope import schema
from zope.interface import Interface


class ISKU(Interface):
    """Interface for SKU behavior."""

    sku = schema.TextLine(
        title=_(u"SKU"),
        description=_(u"Unique ID for Stock Keeping Unit."))
