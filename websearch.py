import requests
import urllib
import sys
import logging

#----------------- Logger import ---------------------------------

logger = logging.getLogger(__name__)
log_level = logging.DEBUG

#-----------------Search Term using Custom Search API---------------------------

def search_item(search_term,
                API_KEY= "AIzaSyD0H_G1JKCgklUtvDFVcdoMtto3ooyalZ8",
                CUSTOM_KEY="007585794764902922731:lhcpji7ohgq",
                google_url = "https://www.googleapis.com/customsearch/v1?",
                log_level = logging.DEBUG
                ):

    logger.setLevel(log_level)

    parameters = {
        "key": API_KEY,
        "cx": CUSTOM_KEY,
        "q": search_term
        }

    google_url += urllib.parse.urlencode(parameters)

    logger.debug("Looking up {}".format(google_url))
    results = requests.get(google_url)
    results = results.json()

    logger.debug("Got {} results".format(len(results)))
    
    output={}
    output["search_term"]=search_term
    output["search_url"]=google_url

    if results.get("error") is not None :
        output["formattedTotalResults"]=None
        output["totalResults"]=None
        output["correction"]="None"
        output["status"]="{}. {}".format(results.get("error").get("code"),results.get("error").get("message"))
    else:
        output["formattedTotalResults"]=\
            results.get("searchInformation").get("formattedTotalResults")
        output["totalResults"]=\
            results.get("searchInformation").get("totalResults")
        if results.get("spelling"):
            output["correction"]=results.get("spelling").get("correctedQuery")
        
    return output

#---------------------------------------------Main-----------------------------------
#Search the parameters or perform basic test
if __name__ == '__main__':
    if(len(sys.argv) > 1):
        print(search_item(str(sys.argv[1:])))
    else:
        result = search_item("Quail Rd, Lake Clifton, WA 6215")
        logger.debug("Hello")
        print(result)

    input()
