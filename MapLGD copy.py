import pandas as pd

file_location = "Data/output/Andaman And Nicobar Islands/"

df_01 = pd.read_csv( file_location + 'allBlockStateWithCoveredVillage12024:06:23:00:50:11:325.csv')
df_02 = pd.read_csv( file_location + 'blockofspecificState2024:06:23:00:50:11:258.csv')
# 
# df_04 = pd.read_csv( file_location + 'priLbSpecificState2024:06:23:00:50:10:828.csv')
# df_05 = pd.read_csv( file_location + 'priWards2024:06:23:00:50:11:073.csv')
# 
# df_07 = pd.read_csv( file_location + 'tlbSpecificState2024:06:23:00:50:10:894.csv')
# df_08 = pd.read_csv( file_location + 'ulbSpecificState2024:06:23:00:50:10:855.csv')
# df_09 = pd.read_csv( file_location + 'uLBWardforState2024:06:23:00:50:10:920.csv')
# df_10 = pd.read_csv( file_location + 'uLBWardforStateWithCov2024:06:23:00:50:10:981.csv')
# 
# 

##################################################

df_comb_01 = pd.merge(df_01, df_02, on='Development Block Code')

df_comb_01 = df_comb_01.drop(["S.No.","District Code_y","District Name","Development Block Name","Development Block Name.1"], axis=1)
df_comb_01 = df_comb_01.rename(columns={'District Code_x': 'District Code'})

original_columns = df_comb_01.columns.tolist()
new_order = ["State Code","State Name (In English)","District Code","District Name (In English)","Development Block Code","Development Block Name (In English)","Development Block Version","Village Code","Village Name (In English)"]
df_comb_01 = df_comb_01[new_order]

#################################################

df_03 = pd.read_csv( file_location + 'districtofSpecificState2024:06:23:00:50:10:581.csv')

df_comb_02 = pd.merge(df_comb_01, df_03, on='District Code')

df_comb_02 = df_comb_02.drop(["S. No.","District Name","District Name.1"], axis=1)
df_comb_02 = df_comb_02.rename(columns={'Census 2001 Code': 'District Census 2001 Code'})
df_comb_02 = df_comb_02.rename(columns={'Census 2011 Code': 'District Census 2011 Code'})

original_columns = df_comb_02.columns.tolist()
new_order = ["State Code","State Name (In English)","District Code","District Name (In English)","District Version","District Census 2001 Code","District Census 2011 Code","Development Block Code","Development Block Name (In English)","Development Block Version","Village Code","Village Name (In English)"]
df_comb_02 = df_comb_02[new_order]

###################################################

df_06 = pd.read_csv( file_location + 'subDistrictofSpecificState2024:06:23:00:50:10:606.csv')
df_06 = df_06.rename(columns={'District code': 'District Code'})

df_comb_03 = pd.merge(df_comb_02, df_06, on='District Code')

df_comb_03 = df_comb_03.drop(["S.No.","District Name","Subdistrict Name.1"], axis=1)
df_comb_03 = df_comb_03.rename(columns={'Census 2001 Code': 'Subdistrict Census 2001 Code'})
df_comb_03 = df_comb_03.rename(columns={'Census 2011 Code': 'Subdistrict Census 2011 Code'})

original_columns = df_comb_03.columns.tolist()
new_order = ["State Code","State Name (In English)","District Code","District Name (In English)","District Version","District Census 2001 Code","District Census 2011 Code","Subdistrict Code","Subdistrict Version","Subdistrict Name","Subdistrict Census 2001 Code","Subdistrict Census 2011 Code","Development Block Code","Development Block Name (In English)","Development Block Version","Village Code","Village Name (In English)"]
df_comb_03 = df_comb_03[new_order]

###################################################

df_11 = pd.read_csv( file_location + 'villageGramPanchayatMapping2024:06:23:00:50:11:226.csv')

df_comb_04 = pd.merge(df_comb_03, df_11, on='Village Code')

df_comb_04 = df_comb_04.drop(["S.No.","District Code_y","District Name","District Census 2011 Code_y","District Census 2001 Code_y","Subdistrict Code_y","Subdistrict Name_y","Subdistrict Census 2011 Code_y","Subdistrict Census 2001 Code_y","Village Name"], axis=1)

df_comb_04 = df_comb_04.rename(columns={'District Code_x': 'District Code'})
df_comb_04 = df_comb_04.rename(columns={'District Census 2001 Code_x': 'District Census 2001 Code'})
df_comb_04 = df_comb_04.rename(columns={'District Census 2011 Code_x': 'District Census 2011 Code'})
df_comb_04 = df_comb_04.rename(columns={'Subdistrict Code_x': 'Subdistrict Code'})
df_comb_04 = df_comb_04.rename(columns={'Subdistrict Name_x': 'Subdistrict Name'})
df_comb_04 = df_comb_04.rename(columns={'Subdistrict Census 2001 Code_x': 'Subdistrict Census 2001 Code'})
df_comb_04 = df_comb_04.rename(columns={'Subdistrict Census 2011 Code_x': 'Subdistrict Census 2011 Code'})


####################################################

df_12 = pd.read_csv( file_location + 'villageofSpecificState2024:06:23:00:50:10:782.csv')

df_comb_05 = pd.merge(df_comb_04, df_12, on='Village Code')

#####################################################

df_comb_05.drop_duplicates(subset=None, keep='first', inplace=False)
df_comb_05.to_csv(file_location + "merged.csv", index=False)