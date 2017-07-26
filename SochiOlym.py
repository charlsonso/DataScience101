'''
	grab data using crawler 
	Tutorial: https://www.youtube.com/watch?v=hMxOuWJaVDA&index=17&list=PLAwxTw4SYaPk41og7PER4HBpGciPw6n3x

'''
import pandas as pd
#create a pandas dataframe called 'olylmpic_medal_counts_df'
#col should be called 'country_name','gold',silver','bronze'


countries = ['Russia (RUS)','Norway (NOR)','Canada (CAN)','United States (USA)',
'Netherlands (NED)','Germany (GER)','Switzerland (SUI)','Belarus (BLR)','Austria (AUT)','France (FRA)']

gold=[13,11,10,9,8,8,6,5,4,4]
silver=[11,5,10,7,7,6,3,0,8,4]
bronze=[9,10,5,12,9,5,2,1,5,7]

olympic_medal_counts = {'country_name':pd.Series(countries),
'gold':pd.Series(gold),
'silver':pd.Series(silver),
'bronze':pd.Series(bronze)
}

olympic_medal_counts_df=pd.DataFrame(olympic_medal_counts)
# print(olympic_medal_counts_df)
print(olympic_medal_counts_df['gold'])
print(olympic_medal_counts_df[['country_name','gold','silver']])

