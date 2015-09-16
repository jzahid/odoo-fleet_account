# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Addon by
#    CLEARCORP S.A. (<http://clearcorp.co.cr>).
#    AURIUM TCHNOLOGIES (<http://auriumtechnologies.com>).
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

{
    "name" : 'Fleet Analytic Account',
    "version" : '1.0',
    "author" : 'ClearCorp, Aurium Technologies',
    'complexity': 'normal',
    "description": """
""",
    "category": 'Managing vehicles and contracts',
    "sequence": 3,
    "website" : "http://clearcorp.co.cr, http://www.auriumtechnologies.com",
    "images" : [],
    "depends" : [
                 'fleet',
                 'account_analytic_analysis',
		 'account'
                 ],
    "data" : ['fleet_analytic_account_analysis.xml'],
    "init_xml" : [],
    "demo_xml" : [],
    "update_xml" : [],
    "test" : [],
    "auto_install": False,
    "application": False,
    "installable": True,
    'license': 'AGPL-3',
}
