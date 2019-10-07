from TestSetup import TestSetup
from WebKeywords import WebKeywords


class PyKeywords(
    TestSetup,
    WebKeywords
):

    ROBOT_LIBRARY_SCOPE = "GLOBAL"  