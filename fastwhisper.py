# djm 2025/02
# Copy of whisperer.py
# different class name, different call to speech recognition
# 90% of this code is from Kalliope

import speech_recognition as sr
import logging

from kalliope.core import Utils
from kalliope.stt.Utils import SpeechRecognition

logging.basicConfig()
logger = logging.getLogger("kalliope")

class Fastwhisper(SpeechRecognition):

    def __init__(self, callback=None, **kwargs):
        """
        Start recording the microphone and analyse audio
        :param callback: The callback function to call to send the text
        :param kwargs:
        """
        # give the audio file path to process directly to the mother class if exist
        SpeechRecognition.__init__(self, kwargs.get('audio_file_path', None))

        self.language = kwargs.get('language', "English")
        self.model = kwargs.get('model', "base")

        # callback function to call after the translation speech/tex
        self.main_controller_callback = callback
        self.set_callback(self.whisper_callback)

        # start processing, record a sample from the microphone if no audio file path provided, else read the file
        logger.debug("[Whisperer] starting whisper with %s model" %  self.model + " " + self.language)
        self.start_processing()

    def whisper_callback(self, recognizer, audio):
        """
        called from the background thread
        suppress_tokens, remove punctuation, !,.?, different than whisper 
        """
        try:
            captured_audio = recognizer.recognize_faster_whisper(audio,
                                                         language=self.language,
                                                         model=self.model,
                                                         suppress_tokens=[0,11,13,30])
            Utils.print_success("Faster Whisper Speech Recognition thinks you said %s" % captured_audio)
            self._analyse_audio(captured_audio)

        except sr.UnknownValueError:
            Utils.print_warning("Faster Whisper Speech Recognition could not understand audio")
            # callback anyway, we need to listen again for a new order
            self._analyse_audio(audio_to_text=None)
        except sr.RequestError as e:
            Utils.print_danger("Could not request results from Faster Whisper Speech Recognition service; {0}".format(e))
            # callback anyway, we need to listen again for a new order
            self._analyse_audio(audio_to_text=None)
        except AssertionError:
            Utils.print_warning("No audio caught from microphone")
            self._analyse_audio(audio_to_text=None)

    def _analyse_audio(self, audio_to_text):
        """
        Confirm the audio exists and run it in a Callback
        :param audio_to_text: the captured audio
        """
        logger.debug("[Faster Whisper] audio_to_text: %s end" % audio_to_text)
        if "BLANK_AUDIO" in audio_to_text:
            audio_to_text = ""
            print(audio_to_text)
		
        if self.main_controller_callback is not None:
            self.main_controller_callback(audio_to_text)
