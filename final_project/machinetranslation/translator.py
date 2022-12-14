"""
This module is used to translate English to French and French to English
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-12-13',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    This function translate engligh to french
    """
    if english_text=="":
        return ""
    else:
        french_text = language_translator.translate(
        text=english_text, model_id='en-fr').get_result()
        french_text=french_text["translations"][0]["translation"]
        return french_text

def french_to_english(french_text):
    """
    This function translate french to english
    """
    if french_text=="":
        return ""
    else:
        english_text = language_translator.translate(
        text=french_text, model_id='fr-en').get_result()
        english_text_text=english_text["translations"][0]["translation"]
        return english_text_text
