from robot.api import *
import warnings

from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
import Selenium2Library
from SeleniumLibrary.base import DynamicCore
from SeleniumLibrary.errors import NoOpenBrowser
from SeleniumLibrary.keywords import (AlertKeywords,
                                      BrowserManagementKeywords,
                                      CookieKeywords,
                                      ElementKeywords,
                                      FormElementKeywords,
                                      FrameKeywords,
                                      JavaScriptKeywords,
                                      RunOnFailureKeywords,
                                      ScreenshotKeywords,
                                      SelectElementKeywords,
                                      TableElementKeywords,
                                      WaitingKeywords,
                                      WebDriverCache,
                                      WindowKeywords)
from SeleniumLibrary.locators import ElementFinder
from SeleniumLibrary.utils import Deprecated, LibraryListener, timestr_to_secs

driver=BrowserManagementKeywords(Selenium2Library.Selenium2Library())
driver.open_browser('http://www.baidu.com',browser='chrome')
driver.find_element('id=kw').clear()
driver.find_element('id=kw').send_keys('123')
driver.find_element('id=su').clear()

