"""Definition of the TwapPartner content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from twap.partnerdb import partnerdbMessageFactory as _

from twap.partnerdb.interfaces import ITwapPartner
from twap.partnerdb.config import PROJECTNAME

TwapPartnerSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.LinesField(
        'partnertype',
        widget=atapi.LinesWidget(
            label=_(u"Partnership type"),
            description=_(u"Partnership type"),
        ),
        required=True,
    ),


    atapi.LinesField(
        'data_provider',
        widget=atapi.LinesWidget(
            label=_(u"Data and source provider"),
            description=_(u"Data and source provider"),
        ),
    ),


    atapi.TextField(
        'contacts',
        widget=atapi.RichtextWidget(
            label=_(u"Coordinates/Contacts"),
            description=_(u"Coordinates/Contacts"),
        ),
    ),


    atapi.LinesField(
        'work_field',
        widget=atapi.LinesWidget(
            label=_(u"Fields of work"),
            description=_(u"Fields of work"),
        ),
    ),


    atapi.TextField(
        'arangement_level',
        widget=atapi.TextAreaWidget(
            label=_(u"Level of arrangement"),
            description=_(u"Level of Arrangement"),
        ),
    ),


    atapi.TextField(
        'indicator',
        widget=atapi.TextAreaWidget(
            label=_(u"Indicators"),
            description=_(u"Indicators"),
        ),
    ),


    atapi.StringField(
        'water_type',
        widget=atapi.StringWidget(
            label=_(u"Water Type"),
            description=_(u"Type of water body"),
        ),
        required=True,
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.


schemata.finalizeATCTSchema(TwapPartnerSchema, moveDiscussion=False)


class TwapPartner(base.ATCTContent):
    """TWAP Partner"""
    implements(ITwapPartner)

    meta_type = "TwapPartner"
    schema = TwapPartnerSchema



atapi.registerType(TwapPartner, PROJECTNAME)
