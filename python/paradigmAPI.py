import requests as r
from datetime import datetime, timedelta

class ParadigmAPI(object):

    # init with freekey if key is not defined
    def __init__ (self, key='59b910a23d4d4d21b9094ad5c7ffdc2f'):
        self.key = key

        if len(self.key) != 32:
            raise Exception('API key is invalid.')

        self.base = 'https://api.paradigmapi.com/v1/paradigm/'


    # make a request for any valid Paradigm method
    def query(self, method, args={}, df=False):

        # add the api key to the args
        args['subscription-key'] = self.key
        
        res = r.get(self.base + method, params=args)

        data = res.json()

        if df: 
            import pandas as pd
            return pd.DataFrame(data['result'])

        return res.json()

    # paginate through any valid Paradigm method with a datetime
    # the date format is YYYY-mm-dd
    def paginate(self, method, start, end, args={}, df=False):

        out = []
        args['subscription-key'] = self.key

        # verify the date is in the valid format
        try:
            datetime.strptime(start, '%Y-%m-%d')
            datetime.strptime(end, '%Y-%m-%d')
        except:
            raise Exception('Invalid start or end date. Please use the format `YYYY-mm-dd`')


        # loop through requests until the all data is gathered or a rate limit is encountered

        while True:
            print(start)
            args['datetimeUTC'] = start + ':' + end
            args['sort'] = 'datetimeUTC'
            args['order'] = 'asc'

            res = r.get(self.base + method, params=args)

            if res.status_code == 200:
                data = res.json()

                if data['results_returned'] == 0:
                    break

                start = self._fmt_date_str(data['result'][-1]['datetimeUTC'], 1)
                out += data['result']
            else:
                raise Exception('Your API key has reached a rate limit. Please reduce the range or increase your limits.')

        if df: 
            import pandas as pd
            return pd.DataFrame(out)

        return out

    def _fmt_date_str(self, date, delta):
        date = datetime.strptime(date[:10], '%Y-%m-%d') + timedelta(days=delta)
        return date.isoformat()[:10]


if __name__ == '__main__':

    pAPI = ParadigmAPI()
    out = pAPI.query('api-status')
    print(out)