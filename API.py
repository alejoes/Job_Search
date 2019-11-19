import requests
import json

def send_request(jobCate):
    try:
        response = requests.get( url="https://www.amazon.jobs/en/search.json?",params={
                "base_query": "",
                "category[]": jobCate,
                "city": "",
                "country": "",
                "county": "",
                "facets[]": "location,category,normalized_location,job_function_id, business_category, schedule_type_id, employee_class, normalized_location, job_function_id",
                "latitude": "",
                "loc_group_id": "",
                "loc_query": "",
                "longitude": "",
                "offset": 0,
                "query_options": "",
                "radius": "24km",
                "region": "",
                "result_limit": 100,
                "sort": "relevant"},
            headers={
                "Host": "www.amazon.jobs",
                "Connection": "keep-alive",
                "Pragma": "no-cache",
                "Cache-Control": "no-cache",
                "Accept": "*/*",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
                "Accept-Encoding": "gzip, deflate",
                "Cookie": "preferred_locale=en-US"})
            print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        return response.text
    except requests.exceptions.RequestException:
        print('HTTP Request failed')