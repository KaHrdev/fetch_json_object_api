def get_objects_controllers_and_atis(data):
    
    #-- get the controllers and atis keys
    controllers = data["controllers"]
    atis = data["atis"]
    print(controllers)
    print(atis)

    # clear the dictionary
    data.clear()

    # add controllers and atis keys again
    data["controllers"] = controllers
    data["atis"] = atis

    return data


def get_objects_callsign_and_frequency(data):
    controllers = []
    for controller in data["controllers"]:
        
        #-- get the callsign and frequency keys
        callsign = controller["callsign"]
        frequency = controller["frequency"]
        
        #-- clean the controller dictionary
        controller.clear()

        # add callsign and frequency keys again
        controller["callsign"] = callsign
        controller["frequency"] = frequency


        controllers.append(controller)

    atis = []
    for ati in data["atis"]:
        
        #-- get the callsign and frequency keys
        callsign = ati["callsign"]
        frequency = ati["frequency"]
        
        #-- clean the ati dictionary
        ati.clear()

        # add callsign and frequency keys again
        ati["callsign"] = callsign
        ati["frequency"] = frequency


        atis.append(ati)

    
    #-- clear data
    data.clear()

    #-- rebuild the data dictionary
    data["controllers"] = controllers
    data["atis"] = atis 

    return data