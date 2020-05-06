from bs4 import BeautifulSoup
from scrapper.selenium import chrome

from utils.log import log
from utils.setting import setting

_instagram = None
class instagram:
    @staticmethod
    def getInstance():
        global _instagram
        if _instagram == None:
            _instagram = instagram()
        return _instagram

    def __init__(self):
        pass

    def start(self):
        chrome.getInstance().doAction(message='Open instagram', action='open', params={'url': setting.getInstance().get('INSTAGRAM')})
        chrome.getInstance().doAction(action='setValue', params={'name': 'username', 'value': setting.getInstance().get('INSTAGRAM_USER')})
        chrome.getInstance().doAction(action='setValue', params={'name': 'password', 'value': setting.getInstance().get('INSTAGRAM_PASSWORD')})
        chrome.getInstance().doAction(message='Login instagram', action='click', params={'tag': 'button', 'text': 'Log In'})
        chrome.getInstance().doAction(message='Waiting for login', action='wait_for_pageload')
        chrome.getInstance().doAction(message='Remove notification dialog', action='click', params={'tag': 'button', 'text': 'Not Now'})
        # html = chrome.getInstance().getHtml()
        # soup = Beautifulsoup(content)