from collections import defaultdict

import pandas as pd
import requests, json,pprint
base_url = 'https://api.carbonintensity.org.uk/regional'
response=requests.get(base_url)
dnoregion=[]
shortname=[]
forecast=[]
index=[]
result=[]
fuel=[]
perc=[]
regionid=[]
if response.status_code==200:
    data=response.json()
    #print(type(data)) #dictionary
    data_inside=data['data']
    for date_ in data_inside:
        #print(type(date_))#dict
        regions = date_['regions']
        pprint.pprint(regions, indent=4)
        for region in regions:
            temp_dict = defaultdict(set)
            my_dict = {}
            dnoregion.append(region['dnoregion'])
            # region['intensity']
            forecast.append(region['intensity']['forecast'])
            index.append(region['intensity']['index'])
            regionid.append(region['regionid'])
            shortname.append(region['shortname'])
            generator_mix = region['generationmix']
            #print(generator_mix)
            for generator_fuel in generator_mix:
                for key, value in generator_fuel.items():
                    temp_dict[key].add(value)
            for key, value in temp_dict.items():
                my_dict[key] = "".join(str(value))
            #        #print(value)
            for keys,values in my_dict.items():
                if keys=='fuel':
                    fuel.append(values)
                elif keys=='perc':
                    #print(values)
                    perc.append(values)
    #print(new_data)

    data_df = {'dnoregion': dnoregion, 'shortname': shortname, 'regionid': regionid, 'forecast': forecast,
               'index': index, 'fuel': fuel, 'perc': perc}

    dict_df = pd.DataFrame({key: pd.Series(value,dtype=pd.StringDtype()) for key, value in data_df.items()})
    #dict_df['fuel'] = dict_df['fuel'].str.replace(r"([0-9]+)$", "")
    #dict_df.replace({'\'': '"'}, regex=True)
    dict_df['fuel'] = dict_df['fuel'].str.strip("{},")
    dict_df['perc'] = dict_df['perc'].str.strip("{},")
    dict_df.to_csv('carbon_intensity.csv')







