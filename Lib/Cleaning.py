import  pandas as pd

import os

class CleanClass:

    def __init__(self, csv_file):
        self.df = csv_file
    
    def process_data(self):
        
        df2 = self.df.copy()

        df3=df2.copy()

        


        # Add function add_none from Juyter Notebook

        ##########################


        # Apply the function to the entire column
        df3['Airline_Company_and_Layover_AIRprt'] = df3['Airline_Company_and_Layover_AIRprt'].apply(self.replace_ndashn)
        df3['Airline_Company_and_Layover_AIRprt'] = df3['Airline_Company_and_Layover_AIRprt'].apply(self.replace_doublenn)
        df3['Airline_Company_and_Layover_AIRprt'] = df3['Airline_Company_and_Layover_AIRprt'].apply(self.replace_singlen)
        df3['Airline_Company_and_Layover_AIRprt'] = df3['Airline_Company_and_Layover_AIRprt'].apply(self.replace_leftbrack)
        df3['Airline_Company_and_Layover_AIRprt'] = df3['Airline_Company_and_Layover_AIRprt'].apply(self.replace_rightbrack)
        df3['Airline_Company_and_Layover_AIRprt'] = df3['Airline_Company_and_Layover_AIRprt'].apply(self.replace_extra_comma)
        
        df4 = df3.copy()


        add_none = lambda row: row['Airline_Company_and_Layover_AIRprt'] + '&None' if row['Number_of_stops'] == 'nonstop' else row['Airline_Company_and_Layover_AIRprt']

        df4['Airline_Company_and_Layover_AIRprt'] = df4.apply(add_none,axis=1)

        df5 = df4.copy()

        df5[['Airline_Companies', 'Layover_stops', 'total_flight_path', 'departure_loc', 'arrival_loc']] = df5.apply(
        lambda row: pd.Series(row['Airline_Company_and_Layover_AIRprt'].split('&')), axis=1)

        df6=df5.copy()



        mask = df6['Number_of_stops'] == 'nonstop'
        df6.loc[mask,['Layover_stops', 'total_flight_path', 'departure_loc', 'arrival_loc']] = df6.loc[mask,['arrival_loc', 'Layover_stops', 'total_flight_path', 'departure_loc']].values

        # df7 = df6.drop('Airline_Company_and_Layover_AIRprt', axis=1).copy()

        spath = '/Users/zoepetropoulou/Development/code/post_flatiron/Gen_flightdata/Cleaned_Flight_Data'
        name = '08092023_clean.csv'
        file_path_and_name = os.path.join(spath,name)

        df6.to_csv(file_path_and_name, index=False)
        df7 = df6.copy()

        return df7

    
    def replace_ndashn(self,text):
        return text.replace('\\n-\\n', '-')

    def replace_doublenn(self,text):
        return text.replace(r'\n\n','&')

    def replace_singlen(self,text):
        return text.replace(r'\n','&')

    def replace_leftbrack(self,text):
        return text.replace('[','')

    def replace_rightbrack(self,text):
        return text.replace(']','')

    def replace_extra_comma(self,text):
        return text.replace(', ',' and ')
    
    



custom_folder_path = "/Users/zoepetropoulou/Development/code/post_flatiron"
csv_file_path = os.path.join(custom_folder_path, "10102023_raw_test.csv")

df=pd.read_csv(csv_file_path)

cleaner = CleanClass(csv_file=df)
print(cleaner.process_data())



