# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Guewen Baconnier
#    Copyright 2013 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

# flake8: noqa : ignore style in this file because it is a data file
# only

"""
Shopware responses for calls done by the connector.

This set of responses has been recorded for the synchronizations
with a Shopware 1.7 version with demo data.

It has been recorded using ``shopwareerpconnect.unit.backend_adapter.record``
and ``shopwareerpconnect.unit.backend_adapter.output_recorder``

This set of data contains examples of customers and their address books
"""


# customer without address
no_address = {
    ('customer.info', (9999253,)): {'confirmation': None,
                                    'created_at': '2013-06-28 12:35:33',
                                    'created_in': 'English',
                                    'customer_id': '9999253',
                                    'default_billing': None,
                                    'default_shipping': None,
                                    'disable_auto_group_change': '0',
                                    'dob': None,
                                    'email': 'lucie69+testdata@example.com',
                                    'firstname': 'Benjamin',
                                    'gender': None,
                                    'group_id': '1',
                                    'increment_id': None,
                                    'lastname': 'Le Goff',
                                    'middlename': None,
                                    'password_hash': '1c200f3cca5856a6da405359a4640de7:Ae',
                                    'prefix': None,
                                    'rp_token': None,
                                    'rp_token_created_at': None,
                                    'store_id': '1',
                                    'suffix': None,
                                    'taxvat': None,
                                    'updated_at': '2013-06-28 12:36:23',
                                    'website_id': '1'},
    ('customer_address.list', (frozenset([('customer_id', frozenset([('eq', '9999253')]))]),)): [],
}


# individual customer with 1 address
individual_1_address = \
    {('customer.info', (9999254,)): {'confirmation': None,
                                     'created_at': '2013-06-28 12:43:49',
                                     'created_in': 'English',
                                     'customer_id': '9999254',
                                     'default_billing': '9999253',
                                     'default_shipping': '9999253',
                                     'disable_auto_group_change': '0',
                                     'dob': None,
                                     'email': 'bourdon.laurent+testdata@example.net',
                                     'firstname': 'Alexandre',
                                     'gender': None,
                                     'group_id': '1',
                                     'increment_id': None,
                                     'lastname': 'Laroche',
                                     'middlename': None,
                                     'password_hash': '6f1a99ac3f1acf03f7534dfd6464e5ce:QI',
                                     'prefix': None,
                                     'rp_token': None,
                                     'rp_token_created_at': None,
                                     'store_id': '1',
                                     'suffix': None,
                                     'taxvat': None,
                                     'updated_at': '2013-06-28 12:43:49',
                                     'website_id': '1'},
     ('customer_address.info', (9999253,)): {'city': u'Boutin-la-Forêt',
                                             'company': None,
                                             'country_id': 'FR',
                                             'created_at': '2013-06-28 12:43:49',
                                             'customer_address_id': '9999253',
                                             'fax': None,
                                             'firstname': 'Ferreira',
                                             'increment_id': None,
                                             'is_default_billing': True,
                                             'is_default_shipping': True,
                                             'lastname': 'Margaux',
                                             'middlename': None,
                                             'postcode': '28371',
                                             'prefix': None,
                                             'region': 'Gers',
                                             'region_id': '214',
                                             'street': 'avenue Bourdon',
                                             'suffix': None,
                                             'telephone': '0450615076',
                                             'updated_at': '2013-06-28 12:43:49',
                                             'vat_id': None,
                                             'vat_is_valid': None,
                                             'vat_request_date': None,
                                             'vat_request_id': None,
                                             'vat_request_success': None},
        ('customer_address.list', (frozenset([('customer_id', frozenset([('eq', '9999254')]))]),)):
        [{'city': u'Boutin-la-Forêt',
          'company': None,
          'country_id': 'FR',
          'created_at': '2013-06-28 12:43:49',
          'customer_address_id': '9999253',
          'firstname': 'Ferreira',
          'is_default_billing': True,
          'is_default_shipping': True,
          'lastname': 'Margaux',
          'postcode': '28371',
          'region': 'Gers',
          'region_id': '214',
          'street': 'avenue Bourdon',
          'telephone': '0450615076',
          'updated_at': '2013-06-28 12:43:49'}],
     }


# individual customer with 2 addresses
individual_2_addresses = \
    {('customer.info', (9999255,)): {'confirmation': None,
                                     'created_at': '2013-06-28 12:56:40',
                                     'created_in': 'English',
                                     'customer_id': '9999255',
                                     'default_billing': '9999254',
                                     'default_shipping': '9999255',
                                     'disable_auto_group_change': '0',
                                     'dob': None,
                                     'email': 'marguerite.ramos+testdata@example.org',
                                     'firstname': 'Richard',
                                     'gender': None,
                                     'group_id': '1',
                                     'increment_id': None,
                                     'lastname': 'Humbert',
                                     'middlename': None,
                                     'password_hash': '18d73f47a1dec14fb90c6e87ff95b327:S5',
                                     'prefix': None,
                                     'rp_token': None,
                                     'rp_token_created_at': None,
                                     'store_id': '1',
                                     'suffix': None,
                                     'taxvat': None,
                                     'updated_at': '2013-06-28 13:00:23',
                                     'website_id': '1'},
     ('customer_address.info', (9999254,)): {'city': 'Perez',
                                             'company': None,
                                             'country_id': 'FR',
                                             'created_at': '2013-06-28 12:56:43',
                                             'customer_address_id': '9999254',
                                             'fax': None,
                                             'firstname': 'Mace',
                                             'increment_id': None,
                                             'is_default_billing': True,
                                             'is_default_shipping': False,
                                             'lastname': u'Sébastien',
                                             'middlename': None,
                                             'postcode': '91803',
                                             'prefix': None,
                                             'region': u'Deux-Sèvres',
                                             'region_id': '261',
                                             'street': 'rue Jacques Petitjean',
                                             'suffix': None,
                                             'telephone': '+33 5 69 07 51 52',
                                             'updated_at': '2013-06-28 13:00:23',
                                             'vat_id': None,
                                             'vat_is_valid': None,
                                             'vat_request_date': None,
                                             'vat_request_id': None,
                                             'vat_request_success': None},
        ('customer_address.info', (9999255,)): {'city': 'Bugarach',
                                                'company': None,
                                                'country_id': 'FR',
                                                'created_at': '2013-06-28 13:00:23',
                                                'customer_address_id': '9999255',
                                                'fax': None,
                                                'firstname': 'Richard',
                                                'increment_id': None,
                                                'is_default_billing': False,
                                                'is_default_shipping': True,
                                                'lastname': 'Humbert',
                                                'middlename': None,
                                                'postcode': '11190',
                                                'prefix': None,
                                                'region': 'Aude',
                                                'region_id': '192',
                                                'street': 'Rue Raz 1',
                                                'suffix': None,
                                                'telephone': '+33 5 69 07 51 52',
                                                'updated_at': '2013-06-28 13:00:23',
                                                'vat_id': None,
                                                'vat_is_valid': None,
                                                'vat_request_date': None,
                                                'vat_request_id': None,
                                                'vat_request_success': None},
        ('customer_address.list', (frozenset([('customer_id', frozenset([('eq', '9999255')]))]),)):
        [{'city': 'Perez',
          'company': None,
          'country_id': 'FR',
          'created_at': '2013-06-28 12:56:43',
          'customer_address_id': '9999254',
          'firstname': 'Mace',
          'is_default_billing': True,
          'is_default_shipping': False,
          'lastname': u'Sébastien',
          'postcode': '91803',
          'region': u'Deux-Sèvres',
          'region_id': '261',
          'street': 'rue Jacques Petitjean',
          'telephone': '+33 5 69 07 51 52',
          'updated_at': '2013-06-28 13:00:23'},
         {'city': 'Bugarach',
            'country_id': 'FR',
            'created_at': '2013-06-28 13:00:23',
            'customer_address_id': '9999255',
            'firstname': 'Richard',
            'is_default_billing': False,
            'is_default_shipping': True,
            'lastname': 'Humbert',
            'postcode': '11190',
            'region': 'Aude',
            'region_id': '192',
            'street': 'Rue Raz 1',
            'telephone': '+33 5 69 07 51 52',
            'updated_at': '2013-06-28 13:00:23'}],
     }


# company with 1 address
company_1_address = \
    {('customer.info', (9999256,)): {'confirmation': None,
                                     'created_at': '2013-06-28 13:10:21',
                                     'created_in': 'English',
                                     'customer_id': '9999256',
                                     'default_billing': '9999256',
                                     'default_shipping': '9999256',
                                     'disable_auto_group_change': '0',
                                     'dob': None,
                                     'email': 'theophile.arnaud+testdata@example.com',
                                     'firstname': 'Patrick',
                                     'gender': None,
                                     'group_id': '1',
                                     'increment_id': None,
                                     'lastname': 'Allard',
                                     'middlename': None,
                                     'password_hash': '5fea77dbd8c40f8e1cee408631856e15:1n',
                                     'prefix': None,
                                     'rp_token': None,
                                     'rp_token_created_at': None,
                                     'store_id': '1',
                                     'suffix': None,
                                     'taxvat': None,
                                     'updated_at': '2013-06-28 13:10:22',
                                     'website_id': '1'},
     ('customer_address.info', (9999256,)): {'city': 'Launaynec',
                                             'company': 'Marechal',
                                             'country_id': 'FR',
                                             'created_at': '2013-06-28 13:10:22',
                                             'customer_address_id': '9999256',
                                             'fax': None,
                                             'firstname': 'Leclerc',
                                             'increment_id': None,
                                             'is_default_billing': True,
                                             'is_default_shipping': True,
                                             'lastname': 'Nicole',
                                             'middlename': None,
                                             'postcode': '51591',
                                             'prefix': None,
                                             'region': 'Yvelines',
                                             'region_id': '260',
                                             'street': 'rue de Arnaud',
                                             'suffix': None,
                                             'telephone': '05 11 66 85 86',
                                             'updated_at': '2013-06-28 13:10:22',
                                             'vat_id': None,
                                             'vat_is_valid': None,
                                             'vat_request_date': None,
                                             'vat_request_id': None,
                                             'vat_request_success': None},
        ('customer_address.list', (frozenset([('customer_id', frozenset([('eq', '9999256')]))]),)):
        [{'city': 'Launaynec',
          'company': 'Marechal',
          'country_id': 'FR',
          'created_at': '2013-06-28 13:10:22',
          'customer_address_id': '9999256',
          'firstname': 'Leclerc',
          'is_default_billing': True,
          'is_default_shipping': True,
          'lastname': 'Nicole',
          'postcode': '51591',
          'region': 'Yvelines',
          'region_id': '260',
          'street': 'rue de Arnaud',
          'telephone': '05 11 66 85 86',
          'updated_at': '2013-06-28 13:10:22'}],
     }


# company with 2 addresses
company_2_addresses = \
    {('customer.info', (9999257,)): {'confirmation': None,
                                     'created_at': '2013-06-28 13:23:01',
                                     'created_in': 'English',
                                     'customer_id': '9999257',
                                     'default_billing': '9999257',
                                     'default_shipping': '9999258',
                                     'disable_auto_group_change': '0',
                                     'dob': None,
                                     'email': 'pruvost.aurelie+testdata@example.org',
                                     'firstname': 'Isaac',
                                     'gender': None,
                                     'group_id': '1',
                                     'increment_id': None,
                                     'lastname': 'Maillot',
                                     'middlename': None,
                                     'password_hash': '374fbdc81b990d44703a4b76ea7f1ad2:Ud',
                                     'prefix': None,
                                     'rp_token': None,
                                     'rp_token_created_at': None,
                                     'store_id': '1',
                                     'suffix': None,
                                     'taxvat': None,
                                     'updated_at': '2013-06-28 13:25:28',
                                     'website_id': '1'},
     ('customer_address.info', (9999257,)): {'city': 'Raynauddan',
                                             'company': 'Bertin',
                                             'country_id': 'FR',
                                             'created_at': '2013-06-28 13:23:01',
                                             'customer_address_id': '9999257',
                                             'fax': None,
                                             'firstname': 'Lombard',
                                             'increment_id': None,
                                             'is_default_billing': True,
                                             'is_default_shipping': False,
                                             'lastname': 'Yves',
                                             'middlename': None,
                                             'postcode': '60669',
                                             'prefix': None,
                                             'region': 'Eure',
                                             'region_id': '209',
                                             'street': 'boulevard Benjamin Guillou',
                                             'suffix': None,
                                             'telephone': '01 42 39 24 13',
                                             'updated_at': '2013-06-28 13:25:28',
                                             'vat_id': None,
                                             'vat_is_valid': None,
                                             'vat_request_date': None,
                                             'vat_request_id': None,
                                             'vat_request_success': None},
        ('customer_address.info', (9999258,)): {'city': 'Cailla',
                                                'company': None,
                                                'country_id': 'FR',
                                                'created_at': '2013-06-28 13:25:28',
                                                'customer_address_id': '9999258',
                                                'fax': None,
                                                'firstname': 'Isaac',
                                                'increment_id': None,
                                                'is_default_billing': False,
                                                'is_default_shipping': True,
                                                'lastname': 'Maillot',
                                                'middlename': None,
                                                'postcode': '11140',
                                                'prefix': None,
                                                'region': 'Aude',
                                                'region_id': '192',
                                                'street': 'Rue Montgomery 1',
                                                'suffix': None,
                                                'telephone': '01 42 39 24 13',
                                                'updated_at': '2013-06-28 13:25:28',
                                                'vat_id': None,
                                                'vat_is_valid': None,
                                                'vat_request_date': None,
                                                'vat_request_id': None,
                                                'vat_request_success': None},
        ('customer_address.list', (frozenset([('customer_id', frozenset([('eq', '9999257')]))]),)):
        [{'city': 'Raynauddan',
          'company': 'Bertin',
          'country_id': 'FR',
          'created_at': '2013-06-28 13:23:01',
          'customer_address_id': '9999257',
          'firstname': 'Lombard',
          'is_default_billing': True,
          'is_default_shipping': False,
          'lastname': 'Yves',
          'postcode': '60669',
          'region': 'Eure',
          'region_id': '209',
          'street': 'boulevard Benjamin Guillou',
          'telephone': '01 42 39 24 13',
          'updated_at': '2013-06-28 13:25:28'},
         {'city': 'Cailla',
            'country_id': 'FR',
            'created_at': '2013-06-28 13:25:28',
            'customer_address_id': '9999258',
            'firstname': 'Isaac',
            'is_default_billing': False,
            'is_default_shipping': True,
            'lastname': 'Maillot',
            'postcode': '11140',
            'region': 'Aude',
            'region_id': '192',
            'street': 'Rue Montgomery 1',
            'telephone': '01 42 39 24 13',
            'updated_at': '2013-06-28 13:25:28'}],
     }
