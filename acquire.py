#In my aquire.py folder there is a  get_connection(to help us get access to the data set from code up using our Env credentials).
# get_zillow_data() allows me to import the data and start to visualize it.

from cgi import test
from lib2to3.pgen2.pgen import DFAState
from lib2to3.refactor import get_all_fix_names
import numpy as np
import seaborn as sns
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import env
from pydataset import data
import scipy
import os
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
import warnings
warnings.filterwarnings('ignore')



def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def get_zillow_data():
    #in this data set I will be importing (Properties_2017, Predictions_2017, Propertylandusetype) to allow me to look into zillows single family home data. (which is what we are interested in."""
    filename = "zillow.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read the SQL query into a dataframe, left join to grab data regardless of wather it shares same info, anf join regularly for center join.
        
        df = pd.read_sql("""SELECT *
          FROM properties_2017
          JOIN predictions_2017 using(parcelid)
          LEFT JOIN airconditioningtype USING(airconditioningtypeid)
          LEFT JOIN architecturalstyletype USING(architecturalstyletypeid)
          LEFT JOIN buildingclasstype USING(buildingclasstypeid)
          LEFT JOIN heatingorsystemtype USING(heatingorsystemtypeid)
          LEFT JOIN typeconstructiontype USING(typeconstructiontypeid)
          LEFT JOIN storytype USING(storytypeid)
          LEFT JOIN unique_properties USING(parcelid)
          JOIN propertylandusetype USING(propertylandusetypeid)
          WHERE (propertylandusetypeid = 261) OR (propertylandusetypeid = 279) OR (propertylandusetypeid = 266) OR (propertylandusetypeid = 263) OR (propertylandusetypeid = 262) OR (propertylandusetypeid = 266) OR(propertylandusetypeid = 268) OR (propertylandusetypeid = 273) OR(propertylandusetypeid = 276) OR (propertylandusetypeid = 279)
          ; """, get_connection('zillow'))
            # propertylandusetypeid = 261 and propertylandusetypeid = 279 both are the single family home category, we will be using this data set and join them both using parcelid. 
         # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename, index = False)
        #changing it csv because its a csv

        # Return the dataframe to the calling code
        return df
#