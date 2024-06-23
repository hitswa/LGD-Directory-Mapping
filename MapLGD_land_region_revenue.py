import pandas as pd

file_location = "Data/output/Andaman And Nicobar Islands/"


##################################################

df_01 = pd.read_csv( file_location + 'villageofSpecificState2024:06:23:00:50:10:782.csv')
df_02 = pd.read_csv( file_location + 'allBlockStateWithCoveredVillage12024:06:23:00:50:11:325.csv')

df_comb_03 = pd.merge(df_01, df_02, on='Village Code')

df_comb_03 = df_comb_03.rename(columns={'District Code_x': 'District Code'})
df_comb_03 = df_comb_03.rename(columns={'Census 2001 Code': 'Village Census 2001 Code'})
df_comb_03 = df_comb_03.rename(columns={'Census 2011 Code': 'Village Census 2011 Code'})
df_comb_03 = df_comb_03.rename(columns={'District Code_x': 'District Code'})
df_comb_03 = df_comb_03.rename(columns={'Village Name.1': 'Village Name (Local)'})

df_comb_03 = df_comb_03.drop(["S.No.","District Code_y","District Name","Village Name"], axis=1)

original_columns = df_comb_03.columns.tolist()
new_order = ["State Code","State Name (In English)","District Code","District Name (In English)","Sub-District Code","Sub-District Name","Development Block Code","Development Block Name (In English)","Village Code","Village Name (In English)","Village Name (Local)","Village Category","Village Status","Village Census 2001 Code","Village Census 2011 Code"]
df_comb_03 = df_comb_03[new_order]

#####################################################

df_03 = pd.read_csv( file_location + 'districtofSpecificState2024:06:23:00:50:10:581.csv')

df_comb_04 = pd.merge(df_comb_03, df_03, on='District Code')

df_comb_04 = df_comb_04.rename(columns={'District Name.1': 'District Name (Local)'})
df_comb_04 = df_comb_04.rename(columns={'Census 2001 Code': 'District Census 2001 Code'})
df_comb_04 = df_comb_04.rename(columns={'Census 2011 Code': 'District Census 2011 Code'})

df_comb_04 = df_comb_04.drop(["S. No.","District Name"], axis=1)

original_columns = df_comb_04.columns.tolist()
new_order = ["State Code","State Name (In English)","District Code","District Name (In English)","District Name (Local)","District Version","District Census 2001 Code","District Census 2011 Code","Sub-District Code","Sub-District Name","Development Block Code","Development Block Name (In English)","Village Code","Village Name (In English)","Village Name (Local)","Village Category","Village Status","Village Census 2001 Code","Village Census 2011 Code"]
df_comb_04 = df_comb_04[new_order]

#####################################################

df_04 = pd.read_csv( file_location + 'subDistrictofSpecificState2024:06:23:00:50:10:606.csv')
df_04 = df_04.rename(columns={'Subdistrict Code': 'Sub-District Code'})

df_comb_05 = pd.merge(df_comb_04, df_04, on='Sub-District Code')

df_comb_05 = df_comb_05.drop(["S.No.","District code","District Name","Subdistrict Name"], axis=1)

df_comb_05 = df_comb_05.rename(columns={'Subdistrict Name.1': 'Sub District Name (Local)'})
df_comb_05 = df_comb_05.rename(columns={'Census 2001 Code': 'Sub District Census 2001 Code'})
df_comb_05 = df_comb_05.rename(columns={'Census 2011 Code': 'Sub District Census 2011 Code'})
df_comb_05 = df_comb_05.rename(columns={'Sub-District Code': 'Sub District Code'})
df_comb_05 = df_comb_05.rename(columns={'Sub-District Name': 'Sub District Name'})

original_columns = df_comb_05.columns.tolist()
new_order = ["State Code","State Name (In English)","District Code","District Name (In English)","District Name (Local)","District Version","District Census 2001 Code","District Census 2011 Code","Sub District Code","Sub District Name","Sub District Name (Local)","Subdistrict Version","Sub District Census 2001 Code","Sub District Census 2011 Code","Development Block Code","Development Block Name (In English)","Village Code","Village Name (In English)","Village Name (Local)","Village Category","Village Status","Village Census 2001 Code","Village Census 2011 Code"]
df_comb_05 = df_comb_05[new_order]

#####################################################

df_05 = pd.read_csv( file_location + 'blockofspecificState2024:06:23:00:50:11:258.csv')

df_comb_06 = pd.merge(df_comb_05, df_05, on='Development Block Code')

df_comb_06 = df_comb_06.drop(["S.No.","District Code_y","District Name","Development Block Name"], axis=1)

df_comb_06 = df_comb_06.rename(columns={'District Code_x': 'District Code'})
df_comb_06 = df_comb_06.rename(columns={'Development Block Name.1': 'Development Block Name (Local)'})

original_columns = df_comb_06.columns.tolist()
new_order = ["State Code","State Name (In English)","District Code","District Name (In English)","District Name (Local)","District Version","District Census 2001 Code","District Census 2011 Code","Sub District Code","Sub District Name","Sub District Name (Local)","Subdistrict Version","Sub District Census 2001 Code","Sub District Census 2011 Code","Development Block Code","Development Block Name (In English)","Development Block Name (Local)","Development Block Version","Village Code","Village Name (In English)","Village Name (Local)","Village Category","Village Status","Village Census 2001 Code","Village Census 2011 Code"]
df_comb_06 = df_comb_06[new_order]

#####################################################

# df_06 = pd.read_csv( file_location + 'villageGramPanchayatMapping2024:06:23:00:50:11:226.csv')

# df_comb_07 = pd.merge(df_comb_06, df_06, on='Village Code')

# df_comb_07 = df_comb_07.drop(["S.No.","District Code_y","District Name","District Census 2011 Code_y","District Census 2001 Code_y","Subdistrict Code","Subdistrict Name","Subdistrict Census 2011 Code","Subdistrict Census 2001 Code","Village Name","Village Census 2011 Code_y","Village Census 2001 Code_y"], axis=1)

# df_comb_07 = df_comb_07.rename(columns={'District Code_x': 'District Code'})
# df_comb_07 = df_comb_07.rename(columns={'District Census 2001 Code_x': 'District Census 2001 Code'})
# df_comb_07 = df_comb_07.rename(columns={'District Census 2011 Code_x': 'District Census 2011 Code'})
# df_comb_07 = df_comb_07.rename(columns={'Village Census 2001 Code_x': 'Village Census 2001 Code'})
# df_comb_07 = df_comb_07.rename(columns={'Village Census 2011 Code_x': 'Village Census 2011 Code'})

#####################################################







#####################################################

df_comb_06.drop_duplicates(subset=None, keep='first', inplace=False)
df_comb_06.to_csv(file_location + "merged_land_region_revenue.csv", index=False)