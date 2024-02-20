from odoo.http import request,Response
from odoo import http


class VirtualAssistant(http.Controller):
    @http.route('/assist', website=True, auth='public', type='http', csrf=False)
    def render_assistant_webpage(self, **post):
        return request.render("virtual_assistant.assistant_webpage")