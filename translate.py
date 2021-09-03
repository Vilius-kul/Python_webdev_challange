import json
from settings import TRANSLATION_API_KEY,TRANSLATION_URL
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

class Translator:

    authenticator = IAMAuthenticator(TRANSLATION_API_KEY)
    language_translator = LanguageTranslatorV3(version='2018-05-01',
                                           authenticator=authenticator)       

    @classmethod
    def watson_translate(cls,joke, langInput):
        
        #Authentication 
        cls.language_translator.set_service_url(TRANSLATION_URL)
        #translation via ibm_watson api
        translation = cls.language_translator.translate(text=joke,
                                                source='en', target=langInput).get_result()
        #from dict to str + new line after each joke
        string =''
        for j in translation['translations']:
            string += j['translation']+"<br>"
        return string

    #mock translator
    @staticmethod
    def translate(text: str, language: str) -> str:
        jstring ='<br>'.join([j for j in text])

        return f"{jstring} <br> Selected language to translate to:  {language}"