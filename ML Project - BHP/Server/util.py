import pickle 
import json
import numpy as np

__location = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())

    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if loc_index>=0:
        x[loc_index]=1
    return np.round(__model.predict([x])[0],2)

def load_saved_artifacts():
    print('loading saved artifacts')
    global __data_columns
    global __location
    

    with open('Server/artifacts/columns.json') as f:
        __data_columns = json.load(f)['data_columns']
        __location = __data_columns[3:]

    global __model
    if __model is None:
        with open('Server/artifacts/BHP_model.pickle','rb') as  f:
            __model = pickle.load(f)

        print('All Done!!!')

def get_location_names():
    return __location

def get_data_columns():
    return __data_columns


if __name__=="__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st block jayanagar',1000,2,2))