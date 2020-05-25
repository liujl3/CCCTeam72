state_6 = ["New South Wales","Victoria","Queensland","Western Australia","South Australia","Tasmania"]

city_name = list(set(city["city"].values()))
city_name.sort()

def clear_city(city):
    result = {}
    state_sum = []
    city_sum =[]
    for name in state_6:
        
        
        state_data = {"name":'',"value":0}
        
        
        detail_data = {"cat":'',"data":''}
        
        full_name = city["full_name"]
        
        check_city = []
        cities = []
        
        for index in full_name.keys():
            city_data = {"name":'',"value":0}
            city_name = full_name[index].split(',')[0]
            #print(city_name)
            state_name = full_name[index].split(',')[1]
            tweets_num = city["Tweets_Num"][index]
            
            if  name.strip() == state_name.strip():

                state_data["name"] = name
                state_data["value"]+= tweets_num
                
                if city_name not in check_city:
                    check_city.append(city_name)
                    
                    city_data["name"] = city_name
                    city_data["value"] += tweets_num
                else:
                    city_data["value"] += tweets_num
                
                cities.append(city_data)
                
        #sorted(detail_data["data"])
        detail_data["cat"] = name
        detail_data["data"] = cities
        
        city_sum.append(detail_data)
        
        state_sum.append(state_data)

    final_data = []
    state_final = {}
    state_final["cat"] = "Total"
    state_final["data"] = state_sum
    final_data.append(state_final)
    for item in city_sum:
        final_data.append(item)
    result["data"] = final_data
        

    return result
    