import requests
import urllib
import sys

#-----------------Search Term using Custom Search API---------------------------

def search_item(search_term,
                API_KEY= "AIzaSyB59pE6hsc4iep2fNKQuziVgBDB3hq0bjM",
                CUSTOM_KEY="007585794764902922731:lhcpji7ohgq",
                google_url = "https://www.googleapis.com/customsearch/v1?"
                ):

    parameters = {
        "key": API_KEY,
        "cx": CUSTOM_KEY,
        "q": search_term
        }

    google_url += urllib.parse.urlencode(parameters)

    results = requests.get(google_url)
    results = results.json()

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
        output["correction"]=results.get("spelling").get("correctedQuery")
        output[status]="OK"
    return output

#---------------------------------------------Main-----------------------------------
#Search the parameters or perform basic test
if __name__ == '__main__':
    if(len(sys.argv) > 1):
        print(search_item(str(sys.argv[1:])))
    else:
        result = search_item("108 THE HARDWICKE VILLAGE, NORTH BRUNSWICK ST, DUBLIN 7")
        print(result)

