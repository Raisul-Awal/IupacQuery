
import json
import requests

url = "http://classyfire.wishartlab.com"

def get_results(query_id, return_format="json"):
    r = requests.get('%s/queries/%s.%s' % (url, query_id, return_format),
                     headers={"Content-Type": "application/%s" % return_format})
    r.raise_for_status()
    return r.text

def iupac_query(compound, label='pyclassyfire'):
    



    request_data = {
        'label': label,
        'query_input': compound,
        'query_type': 'IUPAC_NAME'
    }
    json_data = json.dumps(request_data)
    # print(json_data)
    # data = f"'label':{label},'query_input':{compound},query_type:'IUPAC_NAME'"
    r = requests.post(url + '/queries.json', data=json_data, headers={"Content-Type": "application/json"})
    if(r.status_code >= 400 and r.status_code <= 600) :  
        return None
   
    results = get_results(r.json()['id'])
    return json.loads(results)







