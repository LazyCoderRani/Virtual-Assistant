# from odoo import fields,models,api
# import requests
# import json
# import os
# import time
# from openai import OpenAI
# import logging
# _logger = logging.getLogger(__name__)

# key = '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'   # OPEN_AI_API_KEY
# client = OpenAI(api_key=key)

# class Gpt(models.Model):
#     _name = 'pragtech_website_cusotmization.gpt'
#     _description = 'pragtech_website_cusotmization_gpt'

    
#     # -------------------------------------------------------Odoo App GPT----------------------------------------------------------
#     @api.model
#     def get_user_input(self, vals):
#         print("-------------------------------------------Odoo App GPT Input-------------------------------------",vals)
#         # ------------------------------Request Method--------------------------------------------------
#         ODOO_APP_GPT_API_KEY = '11ee40b1-fe08-9b30-9125-69cd6b73f344'   # Odoo_App_GPT_API_KEY
#         url = 'https://retune.so/api/chat/11ee8df0-ebe2-0630-aa48-33fc8c4294d1/new-thread'   # Odoo_App_GPT_Thread_url

#         try:
#             thread_response = requests.post(url, json.dumps({
#             }), headers={
#                 'Content-Type': 'application/json',
#                 'X-Workspace-API-Key': ODOO_APP_GPT_API_KEY
#             })
            
#             thread_data = json.loads(thread_response.text)
#             thread_id = thread_data.get('threadId')
#             print("-------------------------------------------Odoo App GPT Thread-------------------------------------", thread_id)
#         except Exception as e:
#             print('Error in Thread creation:', e)

#         # ------------------------------Response Method--------------------------------------------------
#         PROXY_URL = 'https://retune.so/api/chat/11ee8df0-ebe2-0630-aa48-33fc8c4294d1/response'    # Odoo_App_GPT_Response_url
#         try:
#             responseData = requests.post(PROXY_URL, json.dumps({
#                 'threadId': thread_id,
#                 'input': str(vals),
#             }), headers={
#                 'Content-Type': 'application/json',
#                 'X-Workspace-API-Key': ODOO_APP_GPT_API_KEY
#             })
#             response = responseData.json();
#             print("-------------------------------------------Odoo App GPT Response-------------------------------------", response)
#             return response
#         except Exception as e:
#             print('Error in Thread creation:', e)
#         return vals
    
