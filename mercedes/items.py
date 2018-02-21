# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MercedesItem(scrapy.Item):
    ANNONCE_LINK = scrapy.Field()                                                                                                                                    
    FROM_SITE = scrapy.Field()                                                                                                                                       
    #PRIX = scrapy.Field()
#    SITE = scrapy.Field()                                                                                                                                                #ID_CLIENT = scrapy.Field()

    GARAGE_ID = scrapy.Field() 
    MOIS = scrapy.Field()
    ANNEE = scrapy.Field()
    PHOTO = scrapy.Field()
    MINISITE = scrapy.Field()
    ID_CLIENT = scrapy.Field()
    PROVINCE = scrapy.Field()
    VILLE = scrapy.Field()
    PUISSANCE = scrapy.Field()
    DEPARTEMENT = scrapy.Field()
    NOM = scrapy.Field()
    GARAGE_NAME = scrapy.Field()
    SLUG = scrapy.Field()
    LATITUDE = scrapy.Field()
    LONGITUDE = scrapy.Field()
    ADRESSE = scrapy.Field()
    NUMBER_OF_CARS = scrapy.Field()
    TELEPHONE = scrapy.Field()
    #ANNONCE_LINK = scrapy.Field()
    DEALER_CODE = scrapy.Field() 
    EMAIL = scrapy.Field() 
    OPTIONS = scrapy.Field()

    CARBURANT = scrapy.Field()
    CYLINDRE = scrapy.Field()
    KM = scrapy.Field()
    PRIX = scrapy.Field()
    COULEUR = scrapy.Field()
    BOITE = scrapy.Field()
    #DATE_ENREGISTREMENT = scrapy.Field()
    CARROSSERIE = scrapy.Field()




