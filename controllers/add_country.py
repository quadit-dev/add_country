# -*- coding: utf-8 -*-
# Copyright 2019 <Quadit S.A. de C.V.> (https://www.quadit.mx)
# Copyright 2019 Leticia González Contreras
# Copyright 2019 Lázaro Rodríguez Triana
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import http
from odoo.http import request
from odoo.addons.website_crm.controllers.main import WebsiteForm


class WebsiteForm(WebsiteForm):

    @http.route('/contactus', website=True)
    def website_add_country(self, **kw):
        Country = request.env['res.country']
        countries = Country.search([])
        request.params['countries'] = countries
        return http.request.render('website_add_country.contactus_form_country',
                                   {'countries': countries})

    def insert_record(self, request, model, values, custom, meta=None):
        values['country_id'] = request.params.get('country_id')
        return super(WebsiteForm, self).insert_record(
            request, model, values, custom, meta=meta)

    @http.route('/website_form/<string:model_name>', type='http',
                auth="public", methods=['POST'], website=True)
    def website_form(self, model_name, **kwargs):
        print ("params", request.params)
        country = request.params.get('country_id', {})
        if country:
            request.params['country_id'] = country
        return super(WebsiteForm, self).website_form(model_name, **kwargs)
