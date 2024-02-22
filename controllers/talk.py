from odoo import http
from odoo.http import request
import json

class MyController(http.Controller):

    @http.route('/my_route', type='json', auth='user')
    def my_route_method(self, **kw):
        DID_API_KEY = 'YWNjb3VudHNAcHJhZ3RlY2guY28uaW4:gBecwpLFJ7kaGBSgsvBf7'
        DID_API_URL = 'https://api.d-id.com'
        OPENAI_API_KEY = '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'
        
        if DID_API_KEY == '🤫':
            return {'message': 'Please put your API key inside ./api.json and restart.'}

        # Define a function to fetch OpenAI response
        async def fetch_openai_response(user_message):
            response = http.request('POST', 'https://api.openai.com/v1/chat/completions', headers={
                'Authorization': f'Bearer {OPENAI_API_KEY}',
                'Content-Type': 'application/json',
            }, json={
                'model': "gpt-3.5-turbo",
                'messages': [{'role': "user", 'content': user_message}],
                'temperature': 0.7,
            })
            
            if not response.status == 200:
                return {'message': f'OpenAI API request failed with status {response.status}'}

            data = response.json()
            return data['choices'][0]['message']['content'].strip()

        # Define a function to handle user input
        async def handle_user_input(user_input):
            if peerConnection and (peerConnection.signalingState == 'stable' or peerConnection.iceConnectionState == 'connected'):
                response_from_openai = await fetch_openai_response(user_input)
                print("OpenAI Response:", response_from_openai)
                
                talk_response = http.request('POST', f'{DID_API_URL}/talks/streams/{streamId}', headers={
                    'Authorization': f'Basic {DID_API_KEY}',
                    'Content-Type': 'application/json',
                }, json={
                    'script': {
                        'type': 'text',
                        'subtitles': 'false',
                        'provider': {'type': 'microsoft', 'voice_id': 'en-US-AvaNeural'},
                        'ssml': False,
                        'input': response_from_openai,
                    },
                    'config': {
                        'fluent': True,
                        'pad_audio': 0,
                        'driver_expressions': {
                            'expressions': [{'expression': 'neutral', 'start_frame': 0, 'intensity': 0}],
                            'transition_frames': 0
                        },
                        'align_driver': True,
                        'align_expand_factor': 0,
                        'auto_match': True,
                        'motion_factor': 0,
                        'normalization_factor': 0,
                        'sharpen': True,
                        'stitch': True,
                        'result_format': 'mp4'
                    },
                    'driver_url': 'bank://lively/',
                    'config': {
                        'stitch': True,
                    },
                    'session_id': sessionId
                })
                print("Response from D-ID API:", talk_response)
                # Clear the input field after sending the prompts
                kw['textbox'].val('')

        # Define a function to handle speech recognition
        @http.route('/start_speech_recognition', type='json', auth='user')
        def start_speech_recognition(self, **kw):
            speech_recognition = kw.get('window').webkitSpeechRecognition
            recognition = speech_recognition()
            recognition.continuous = True

            # recognition is started
            recognition.onstart = lambda: kw.get('instructions').text("Recognising...")

            recognition.onspeechend = lambda: kw.get('instructions').text(" ")

            recognition.onerror = lambda: kw.get('instructions').text("I can't hear you. Could you please try again...")

            recognition.onresult = lambda event: kw.get('handle_user_input')(event.results[event.resultIndex][0].transcript)

            def click_event(event):
                content = kw.get('content')
                if len(content) > 0:
                    content += ''
                clearTimeout(kw.get('recognitionTimeout'))
                recognition.start()
                # Set a timeout to stop recognition after 10 seconds of silence
                recognition_timeout_id = setTimeout(lambda: recognition.stop(), 10000)
                kw['recognitionTimeout'] = recognition_timeout_id


            kw.get('speak_button').click(click_event)

        return {'message': 'Success'}
