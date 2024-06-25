import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv("BKB_WaterQualityData_2020084.csv")
df['Read_Date'] = pd.to_datetime(df.Read_Date)
df = df.sort_values(by = 'Read_Date', ascending = True)

df = df.drop(['Air Temp-Celsius', 'Field_Tech', 'DateVerified', 'WhoVerified', 'Unit_Id'], axis=1)
df.dropna(how='any', inplace=True)
df.to_csv("new_water_quality.csv")

columns_to_describe = df.drop(columns=['Read_Date']).columns
desc1 = df[columns_to_describe].describe()
print("Опис значень таблиці:")
print(desc1.to_string())

corrM = df.corr(numeric_only=True)
print("\nКореляційна матриця:")
print(corrM.to_string())

f = plt.figure(figsize=(8, 20))
plt.matshow(corrM, fignum=f.number)
plt.xticks(range(df.select_dtypes(['number']).shape[1]), df.select_dtypes(['number']).columns, fontsize=8, rotation=45)
plt.yticks(range(df.select_dtypes(['number']).shape[1]), df.select_dtypes(['number']).columns, fontsize=8)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=8)
plt.title('Матриця кореляції', fontsize=8);

years_unique = list(df.Year.unique())
#print(years_unique)

total_mean = list(df.mean(numeric_only=True))
total_mean_double = list(np.repeat(total_mean, 2))
#print(total_mean)


dfBay = df[df['Site_Id'] == "Bay"]
Bay_total_mean = list(df.mean(numeric_only=True))
Bay_total_mean_double = list(np.repeat(Bay_total_mean, 2))

Bay_sal_by_year1 = list(dfBay.groupby(dfBay.Read_Date.dt.year)["Salinity (ppt)"].mean())
Bay_sal_by_year_1 = list(np.repeat(Bay_sal_by_year1, 2))

Bay_dis_oxy_by_year1 = list(dfBay.groupby(dfBay.Read_Date.dt.year)["Dissolved Oxygen (mg/L)"].mean())
Bay_dis_oxy_by_year_1 = list(np.repeat(Bay_dis_oxy_by_year1, 2))

Bay_ph_by_year1 = list(dfBay.groupby(dfBay.Read_Date.dt.year)["pH (standard units)"].mean())
Bay_ph_by_year_1 = list(np.repeat(Bay_ph_by_year1, 2))

Bay_secchi_d_by_year1 = list(dfBay.groupby(dfBay.Read_Date.dt.year)["Secchi Depth (m)"].mean())
Bay_secchi_d_by_year_1 = list(np.repeat(Bay_secchi_d_by_year1, 2))

Bay_water_d_by_year1 = list(dfBay.groupby(dfBay.Read_Date.dt.year)["Water Depth (m)"].mean())
Bay_water_d_by_year_1 = list(np.repeat(Bay_water_d_by_year1, 2))

Bay_w_temp_C_by_year1 = list(dfBay.groupby(dfBay.Read_Date.dt.year)["Water Temp (?C)"].mean())
Bay_w_temp_C_by_year_1 = list(np.repeat(Bay_w_temp_C_by_year1, 2))

Bay_air_t_F_by_year1 = list(dfBay.groupby(dfBay.Read_Date.dt.year)["Air Temp (?F)"].mean())
Bay_air_t_F_by_year_1 = list(np.repeat(Bay_air_t_F_by_year1, 2))

Bay_air_t_C_by_year1 = list(dfBay.groupby(dfBay.Read_Date.dt.year)["AirTemp (C)"].mean())
Bay_air_t_C_by_year_1 = list(np.repeat(Bay_air_t_C_by_year1, 2))
#print(Bay_sal_by_year1)

dfA = df[df['Site_Id'] == "A"]
A_total_mean = list(df.mean(numeric_only=True))
A_total_mean_double = list(np.repeat(A_total_mean, 2))

A_sal_by_year1 = list(dfA.groupby(dfA.Read_Date.dt.year)["Salinity (ppt)"].mean())
A_sal_by_year_1 = list(np.repeat(A_sal_by_year1, 2))

A_dis_oxy_by_year1 = list(dfA.groupby(dfA.Read_Date.dt.year)["Dissolved Oxygen (mg/L)"].mean())
A_dis_oxy_by_year_1 = list(np.repeat(A_dis_oxy_by_year1, 2))

A_ph_by_year1 = list(dfA.groupby(dfA.Read_Date.dt.year)["pH (standard units)"].mean())
A_ph_by_year_1 = list(np.repeat(A_ph_by_year1, 2))

A_secchi_d_by_year1 = list(dfA.groupby(dfA.Read_Date.dt.year)["Secchi Depth (m)"].mean())
A_secchi_d_by_year_1 = list(np.repeat(A_secchi_d_by_year1, 2))

A_water_d_by_year1 = list(dfA.groupby(dfA.Read_Date.dt.year)["Water Depth (m)"].mean())
A_water_d_by_year_1 = list(np.repeat(A_water_d_by_year1, 2))

A_w_temp_C_by_year1 = list(dfA.groupby(dfA.Read_Date.dt.year)["Water Temp (?C)"].mean())
A_w_temp_C_by_year_1 = list(np.repeat(A_w_temp_C_by_year1, 2))

A_air_t_F_by_year1 = list(dfA.groupby(dfA.Read_Date.dt.year)["Air Temp (?F)"].mean())
A_air_t_F_by_year_1 = list(np.repeat(A_air_t_F_by_year1, 2))

A_air_t_C_by_year1 = list(dfA.groupby(dfA.Read_Date.dt.year)["AirTemp (C)"].mean())
A_air_t_C_by_year_1 = list(np.repeat(A_air_t_C_by_year1, 2))
#print(A_sal_by_year1)

dfB = df[df['Site_Id'] == "B"]
B_total_mean = list(df.mean(numeric_only=True))
B_total_mean_double = list(np.repeat(B_total_mean, 2))

B_sal_by_year1 = list(dfB.groupby(dfB.Read_Date.dt.year)["Salinity (ppt)"].mean())
B_sal_by_year_1 = list(np.repeat(B_sal_by_year1, 2))

B_dis_oxy_by_year1 = list(dfB.groupby(dfB.Read_Date.dt.year)["Dissolved Oxygen (mg/L)"].mean())
B_dis_oxy_by_year_1 = list(np.repeat(B_dis_oxy_by_year1, 2))

B_ph_by_year1 = list(dfB.groupby(dfB.Read_Date.dt.year)["pH (standard units)"].mean())
B_ph_by_year_1 = list(np.repeat(B_ph_by_year1, 2))

B_secchi_d_by_year1 = list(dfB.groupby(dfB.Read_Date.dt.year)["Secchi Depth (m)"].mean())
B_secchi_d_by_year_1 = list(np.repeat(B_secchi_d_by_year1, 2))

B_water_d_by_year1 = list(dfB.groupby(dfB.Read_Date.dt.year)["Water Depth (m)"].mean())
B_water_d_by_year_1 = list(np.repeat(B_water_d_by_year1, 2))

B_w_temp_C_by_year1 = list(dfB.groupby(dfB.Read_Date.dt.year)["Water Temp (?C)"].mean())
B_w_temp_C_by_year_1 = list(np.repeat(B_w_temp_C_by_year1, 2))

B_air_t_F_by_year1 = list(dfB.groupby(dfB.Read_Date.dt.year)["Air Temp (?F)"].mean())
B_air_t_F_by_year_1 = list(np.repeat(B_air_t_F_by_year1, 2))

B_air_t_C_by_year1 = list(dfB.groupby(dfB.Read_Date.dt.year)["AirTemp (C)"].mean())
B_air_t_C_by_year_1 = list(np.repeat(B_air_t_C_by_year1, 2))
#print(B_sal_by_year1)

dfC = df[df['Site_Id'] == "C"]
C_total_mean = list(df.mean(numeric_only=True))
C_total_mean_double = list(np.repeat(C_total_mean, 2))

C_sal_by_year1 = list(dfC.groupby(dfC.Read_Date.dt.year)["Salinity (ppt)"].mean())
C_sal_by_year_1 = list(np.repeat(C_sal_by_year1, 2))

C_dis_oxy_by_year1 = list(dfC.groupby(dfC.Read_Date.dt.year)["Dissolved Oxygen (mg/L)"].mean())
C_dis_oxy_by_year_1 = list(np.repeat(C_dis_oxy_by_year1, 2))

C_ph_by_year1 = list(dfC.groupby(dfC.Read_Date.dt.year)["pH (standard units)"].mean())
C_ph_by_year_1 = list(np.repeat(C_ph_by_year1, 2))

C_secchi_d_by_year1 = list(dfC.groupby(dfC.Read_Date.dt.year)["Secchi Depth (m)"].mean())
C_secchi_d_by_year_1 = list(np.repeat(C_secchi_d_by_year1, 2))

C_water_d_by_year1 = list(dfC.groupby(dfC.Read_Date.dt.year)["Water Depth (m)"].mean())
C_water_d_by_year_1 = list(np.repeat(C_water_d_by_year1, 2))

C_w_temp_C_by_year1 = list(dfC.groupby(dfC.Read_Date.dt.year)["Water Temp (?C)"].mean())
C_w_temp_C_by_year_1 = list(np.repeat(C_w_temp_C_by_year1, 2))

C_air_t_F_by_year1 = list(dfC.groupby(dfC.Read_Date.dt.year)["Air Temp (?F)"].mean())
C_air_t_F_by_year_1 = list(np.repeat(C_air_t_F_by_year1, 2))

C_air_t_C_by_year1 = list(dfC.groupby(dfC.Read_Date.dt.year)["AirTemp (C)"].mean())
C_air_t_C_by_year_1 = list(np.repeat(C_air_t_C_by_year1, 2))
#print(C_sal_by_year1)

dfD = df[df['Site_Id'] == "D"]
D_total_mean = list(df.mean(numeric_only=True))
D_total_mean_double = list(np.repeat(D_total_mean, 2))

D_sal_by_year1 = list(dfD.groupby(dfD.Read_Date.dt.year)["Salinity (ppt)"].mean())
D_sal_by_year_1 = list(np.repeat(D_sal_by_year1, 2))

D_dis_oxy_by_year1 = list(dfD.groupby(dfD.Read_Date.dt.year)["Dissolved Oxygen (mg/L)"].mean())
D_dis_oxy_by_year_1 = list(np.repeat(D_dis_oxy_by_year1, 2))

D_ph_by_year1 = list(dfD.groupby(dfD.Read_Date.dt.year)["pH (standard units)"].mean())
D_ph_by_year_1 = list(np.repeat(D_ph_by_year1, 2))

D_secchi_d_by_year1 = list(dfD.groupby(dfD.Read_Date.dt.year)["Secchi Depth (m)"].mean())
D_secchi_d_by_year_1 = list(np.repeat(D_secchi_d_by_year1, 2))

D_water_d_by_year1 = list(dfD.groupby(dfD.Read_Date.dt.year)["Water Depth (m)"].mean())
D_water_d_by_year_1 = list(np.repeat(D_water_d_by_year1, 2))

D_w_temp_C_by_year1 = list(dfD.groupby(dfD.Read_Date.dt.year)["Water Temp (?C)"].mean())
D_w_temp_C_by_year_1 = list(np.repeat(D_w_temp_C_by_year1, 2))

D_air_t_F_by_year1 = list(dfD.groupby(dfD.Read_Date.dt.year)["Air Temp (?F)"].mean())
D_air_t_F_by_year_1 = list(np.repeat(D_air_t_F_by_year1, 2))

D_air_t_C_by_year1 = list(dfD.groupby(dfD.Read_Date.dt.year)["AirTemp (C)"].mean())
D_air_t_C_by_year_1 = list(np.repeat(D_air_t_C_by_year1, 2))
#print(D_sal_by_year1)


sal_by_year1 = list(df.groupby(df.Read_Date.dt.year)["Salinity (ppt)"].mean())
dis_oxy_by_year1 = list(df.groupby(df.Read_Date.dt.year)["Dissolved Oxygen (mg/L)"].mean())
ph_by_year1 = list(df.groupby(df.Read_Date.dt.year)["pH (standard units)"].mean())
secchi_d_by_year1 = list(df.groupby(df.Read_Date.dt.year)["Secchi Depth (m)"].mean())
water_d_by_year1 = list(df.groupby(df.Read_Date.dt.year)["Water Depth (m)"].mean())
w_temp_C_d_by_year1 = list(df.groupby(df.Read_Date.dt.year)["Water Temp (?C)"].mean())
air_t_F_by_year1 = list(df.groupby(df.Read_Date.dt.year)["Air Temp (?F)"].mean())
air_t_C_by_year1 = list(df.groupby(df.Read_Date.dt.year)["AirTemp (C)"].mean())


Bay_years_unique = list(dfBay.Year.unique())

Bay_year_date_1 = []
for i in range(len(Bay_years_unique)):
    Bay_year_date = str(Bay_years_unique[i]) + '-01-01'
    Bay_year_date_1.append(datetime.strptime(Bay_year_date, '%Y-%m-%d').date())
    Bay_year_date = str(Bay_years_unique[i]) + '-12-31'
    Bay_year_date_1.append(datetime.strptime(Bay_year_date, '%Y-%m-%d').date())
    #print(year_date_1[i])
#print(year_date_1)
n = len(Bay_year_date_1)


A_years_unique = list(dfA.Year.unique())

A_year_date_1 = []
for i in range(len(A_years_unique)):
    A_year_date = str(A_years_unique[i]) + '-01-01'
    A_year_date_1.append(datetime.strptime(A_year_date, '%Y-%m-%d').date())
    A_year_date = str(A_years_unique[i]) + '-12-31'
    A_year_date_1.append(datetime.strptime(A_year_date, '%Y-%m-%d').date())
    #print(year_date_1[i])
#print(year_date_1)
nA = len(A_year_date_1)


B_years_unique = list(dfB.Year.unique())

B_year_date_1 = []
for i in range(len(B_years_unique)):
    B_year_date = str(B_years_unique[i]) + '-01-01'
    B_year_date_1.append(datetime.strptime(B_year_date, '%Y-%m-%d').date())
    B_year_date = str(B_years_unique[i]) + '-12-31'
    B_year_date_1.append(datetime.strptime(B_year_date, '%Y-%m-%d').date())
    #print(year_date_1[i])
#print(year_date_1)
nB = len(B_year_date_1)


C_years_unique = list(dfC.Year.unique())

C_year_date_1 = []
for i in range(len(C_years_unique)):
    C_year_date = str(C_years_unique[i]) + '-01-01'
    C_year_date_1.append(datetime.strptime(C_year_date, '%Y-%m-%d').date())
    C_year_date = str(C_years_unique[i]) + '-12-31'
    C_year_date_1.append(datetime.strptime(C_year_date, '%Y-%m-%d').date())
    #print(year_date_1[i])
#print(year_date_1)
nC = len(C_year_date_1)

D_years_unique = list(dfD.Year.unique())

D_year_date_1 = []
for i in range(len(D_years_unique)):
    D_year_date = str(D_years_unique[i]) + '-01-01'
    D_year_date_1.append(datetime.strptime(D_year_date, '%Y-%m-%d').date())
    D_year_date = str(D_years_unique[i]) + '-12-31'
    D_year_date_1.append(datetime.strptime(D_year_date, '%Y-%m-%d').date())
    #print(year_date_1[i])
#print(year_date_1)
nD = len(D_year_date_1)




#створення списків даних
site_id = df["Site_Id"].tolist()

salinity = df["Salinity (ppt)"].tolist()
dis_oxy = df["Dissolved Oxygen (mg/L)"].tolist()
ph = df["pH (standard units)"].tolist()
secchi_d = df["Secchi Depth (m)"].tolist()
water_d = df["Water Depth (m)"].tolist()
w_temp_C = df["Water Temp (?C)"].tolist()
air_t_F = df["Air Temp (?F)"].tolist()
air_t_C = df["AirTemp (C)"].tolist()
r_date = df["Read_Date"].tolist()
year = df["Year"].tolist()

year_date_1 = []
for i in range(len(years_unique)):
    year_date = str(years_unique[i]) + '-01-01'
    year_date_1.append(datetime.strptime(year_date, '%Y-%m-%d').date())
    year_date = str(years_unique[i]) + '-12-31'
    year_date_1.append(datetime.strptime(year_date, '%Y-%m-%d').date())
    #print(year_date_1[i])
#print(year_date_1)
n = len(year_date_1)

def Division(v):
    Bay = []
    A = []
    B = []
    C = []
    D = []
    for i in range(len(v)):
        if v[i] == "Bay":
            Bay.append(i)
        if v[i] == "A":
            A.append(i)
        if v[i] == "B":
            B.append(i)
        if v[i] == "C":
            C.append(i)
        if v[i] == "D":
            D.append(i)
    return Bay, A, B, C, D

Bay, A, B, C, D = Division(site_id)

#для Bay
def Bay1(u, r):
    o1 = []
    temp = 0
    for i in range(len(u)):
        temp = u[i]
        o1.append(r[temp])
    return o1

#для A
def A1(u, r):
    o2 = []
    temp = 0
    for i in range(len(u)):
        temp = u[i]
        o2.append(r[temp])
    return o2

#для B
def B1(u, r):
    o3 = []
    temp = 0
    for i in range(len(u)):
        temp = u[i]
        o3.append(r[temp])
    return o3

#для C
def C1(u, r):
    o4 = []
    temp = 0
    for i in range(len(u)):
        temp = u[i]
        o4.append(r[temp])
    return o4

#для D
def D1(u, r):
    o5 = []
    temp = 0
    for i in range(len(u)):
        temp = u[i]
        o5.append(r[temp])
    return o5

Bay_salinity_n = Bay1(Bay, salinity)
Bay_dis_oxy_n = Bay1(Bay, dis_oxy)
Bay_ph_n = Bay1(Bay, ph)
Bay_secchi_d_n = Bay1(Bay, secchi_d)
Bay_water_d_n = Bay1(Bay, water_d)
Bay_w_temp_C_n = Bay1(Bay, w_temp_C)
Bay_air_t_F_n = Bay1(Bay, air_t_F)
Bay_air_t_C_n = Bay1(Bay, air_t_C)
Bay_r_date_n = Bay1(Bay, r_date)

A_salinity_n = A1(A, salinity)
A_dis_oxy_n = A1(A, dis_oxy)
A_ph_n = A1(A, ph)
A_secchi_d_n = A1(A, secchi_d)
A_water_d_n = A1(A, water_d)
A_w_temp_C_n = A1(A, w_temp_C)
A_air_t_F_n = A1(A, air_t_F)
A_air_t_C_n = A1(A, air_t_C)
A_r_date_n = A1(A, r_date)

B_salinity_n = B1(B, salinity)
B_dis_oxy_n = B1(B, dis_oxy)
B_ph_n = B1(B, ph)
B_secchi_d_n = B1(B, secchi_d)
B_water_d_n = B1(B, water_d)
B_w_temp_C_n = B1(B, w_temp_C)
B_air_t_F_n = B1(B, air_t_F)
B_air_t_C_n = B1(B, air_t_C)
B_r_date_n = B1(B, r_date)

C_salinity_n = C1(C, salinity)
C_dis_oxy_n = C1(C, dis_oxy)
C_ph_n = C1(C, ph)
C_secchi_d_n = C1(C, secchi_d)
C_water_d_n = C1(C, water_d)
C_w_temp_C_n = C1(C, w_temp_C)
C_air_t_F_n = C1(C, air_t_F)
C_air_t_C_n = C1(C, air_t_C)
C_r_date_n = C1(C, r_date)

D_salinity_n = D1(D, salinity)
D_dis_oxy_n = D1(D, dis_oxy)
D_ph_n = D1(D, ph)
D_secchi_d_n = D1(D, secchi_d)
D_water_d_n = D1(D, water_d)
D_w_temp_C_n = D1(D, w_temp_C)
D_air_t_F_n = D1(D, air_t_F)
D_air_t_C_n = D1(D, air_t_C)
D_r_date_n = A1(D, r_date)

def Median(a):
    Me= np.median(a)
    return Me

def Arithmetic_Mean(b):
    ArM = np.mean(b)
    return ArM

def Mode(c):
    max = 0
    Mo = c[0]
    for i in c:
        freq = c.count(i)
        if freq > max:
            max = freq
            Mo = i
    return Mo

#виведення значень (мода)
print("\nЗагальна мода (солоність) відносно всіх водойм: ", Mode(salinity))
print("Загальна мода (розчинений кисень) відносно всіх водойм: ", Mode(dis_oxy))
print("Загальна мода (водневий показник pH) відносно всіх водойм: ", Mode(ph))
print("Загальна мода (глибина Секкі) відносно всіх водойм: ", Mode(secchi_d))
print("Загальна мода (глибина води) відносно всіх водойм: ", Mode(water_d))
print("Загальна мода (температура води °C) відносно всіх водойм: ", Mode(w_temp_C))
print("Загальна мода (температура води °F) відносно всіх водойм: ", Mode(air_t_F))
print("Загальна мода (температура повітря °C) відносно всіх водойм: ", Mode(air_t_C))

#виведення значень (сер. арифм.)
print("\nЗагальне середнє арифметичне (солоність) відносно всіх водойм: ", Arithmetic_Mean(salinity))
print("Загальне середнє арифметичне (розчинений кисень) відносно всіх водойм: ", Arithmetic_Mean(dis_oxy))
print("Загальне середнє арифметичне (водневий показник pH) відносно всіх водойм: ", Arithmetic_Mean(ph))
print("Загальне середнє арифметичне (глибина Секкі) відносно всіх водойм: ", Arithmetic_Mean(secchi_d))
print("Загальне середнє арифметичне (глибина води) відносно всіх водойм: ", Arithmetic_Mean(water_d))
print("Загальне середнє арифметичне (температура води °C) відносно всіх водойм: ", Arithmetic_Mean(w_temp_C))
print("Загальне середнє арифметичне (температура води °F) відносно всіх водойм: ", Arithmetic_Mean(air_t_F))
print("Загальне середнє арифметичне (температура повітря °C) відносно всіх водойм: ", Arithmetic_Mean(air_t_C))

#виведення значень (медіана)
print("\nЗагальна медіана (солоність) відносно всіх водойм: ", Median(salinity))
print("Загальна медіана (розчинений кисень) відносно всіх водойм: ", Median(dis_oxy))
print("Загальна медіана (водневий показник pH) відносно всіх водойм: ", Median(ph))
print("Загальна медіана (глибина Секкі) відносно всіх водойм: ", Median(secchi_d))
print("Загальна медіана (глибина води) відносно всіх водойм: ", Median(water_d))
print("Загальна медіана (температура води °C) відносно всіх водойм: ", Median(w_temp_C))
print("Загальна медіана (температура води °F) відносно всіх водойм: ", Median(air_t_F))
print("Загальна медіана (температура повітря °C) відносно всіх водойм: ", Median(air_t_C))


sal_by_year1 = list(df.groupby(df.Read_Date.dt.year)["Salinity (ppt)"].mean())
sal_by_year_1 = list(np.repeat(sal_by_year1, 2))

dis_oxy_by_year1 = list(df.groupby(df.Read_Date.dt.year)["Dissolved Oxygen (mg/L)"].mean())
dis_oxy_by_year_1 = list(np.repeat(dis_oxy_by_year1, 2))

ph_by_year1 = list(df.groupby(df.Read_Date.dt.year)["pH (standard units)"].mean())
ph_by_year_1 = list(np.repeat(ph_by_year1, 2))

secchi_d_by_year1 = list(df.groupby(df.Read_Date.dt.year)["Secchi Depth (m)"].mean())
secchi_d_by_year_1 = list(np.repeat(secchi_d_by_year1, 2))

water_d_by_year1 = list(df.groupby(df.Read_Date.dt.year)["Water Depth (m)"].mean())
water_d_by_year_1 = list(np.repeat(water_d_by_year1, 2))

w_temp_C_d_by_year1 = list(df.groupby(df.Read_Date.dt.year)["Water Temp (?C)"].mean())
w_temp_C_d_by_year_1 = list(np.repeat(w_temp_C_d_by_year1, 2))

air_t_F_by_year1 = list(df.groupby(df.Read_Date.dt.year)["Air Temp (?F)"].mean())
air_t_F_by_year_1 = list(np.repeat(air_t_F_by_year1, 2))

air_t_C_by_year1 = list(df.groupby(df.Read_Date.dt.year)["AirTemp (C)"].mean())
air_t_C_by_year_1 = list(np.repeat(air_t_C_by_year1, 2))

#побудова графіків всі водойми
fig, asal = plt.subplots()
asal.plot(r_date, salinity, label = "Кожне значення")
asal.plot(year_date_1, sal_by_year_1, label = "Середнє річне значення")
asal.plot([year_date_1[0], year_date_1[n-1]], total_mean_double[:2],
          color = 'red', label = "Загальне середнє значення")
asal.set_title("Зміна показника солоності відносно всіх водойм 1989-2019")
asal.set_xlabel("Час")
asal.set_ylabel("Показник солоності (‰)")
asal.legend()
plt.show()

fig, aoxy = plt.subplots()
aoxy.plot(r_date, dis_oxy, label = "Кожне значення")
aoxy.plot(year_date_1, dis_oxy_by_year_1, label = "Середнє річне значення")
aoxy.plot([year_date_1[0], year_date_1[n-1]], total_mean_double[2:4], color = 'red', label = "Загальне середнє значення")
aoxy.set_title("Зміна показника розчиненого кисню (мг/л) відносно всіх водойм 1989-2019")
aoxy.set_xlabel("Час")
aoxy.set_ylabel("Показник розчиненого кисню (мг/л)")
aoxy.legend()
plt.show()

fig, aph = plt.subplots()
aph.plot(r_date, ph, label = "Кожне значення")
aph.plot(year_date_1, ph_by_year_1, label = "Середнє річне значення")
aph.plot([year_date_1[0], year_date_1[n-1]], total_mean_double[4:6], color = 'red', label = "Загальне середнє значення")
aph.set_title("Зміна водневого показника (pH) відносно всіх водойм 1989-2019")
aph.set_xlabel("Час")
aph.set_ylabel("Показник pH")
aph.legend()
plt.show()

fig, asec = plt.subplots()
asec.plot(r_date, secchi_d, label = "Кожне значення")
asec.plot(year_date_1, secchi_d_by_year_1, label = "Середнє річне значення")
asec.plot([year_date_1[0], year_date_1[n-1]], total_mean_double[6:8], color = 'red', label = "Загальне середнє значення")
asec.set_title("Зміна глибини Секкі відносно всіх водойм 1989-2019")
asec.set_xlabel("Час")
asec.set_ylabel("Глибина Секкі (м)")
asec.legend()
plt.show()

fig, awat = plt.subplots()
awat.plot(r_date, water_d, label = "Кожне значення")
awat.plot(year_date_1, water_d_by_year_1, label = "Середнє річне значення")
awat.plot([year_date_1[0], year_date_1[n-1]], total_mean_double[8:10], color = 'red', label = "Загальне середнє значення")
awat.set_title("Зміна глибини води відносно всіх водойм 1989-2019")
awat.set_xlabel("Час")
awat.set_ylabel("Глибина води (м)")
awat.legend()
plt.show()

fig, awtc = plt.subplots()
awtc.plot(r_date, w_temp_C, label = "Кожне значення")
awtc.plot(year_date_1, w_temp_C_d_by_year_1, label = "Середнє річне значення")
awtc.plot([year_date_1[0], year_date_1[n-1]], total_mean_double[10:12], color = 'red', label = "Загальне середнє значення")
awtc.set_title("Зміна температури води (°C) відносно всіх водойм 1989-2019")
awtc.set_xlabel("Час")
awtc.set_ylabel("Температура води (°C)")
awtc.legend()
plt.show()

fig, awtf = plt.subplots()
awtf.plot(r_date, air_t_F, label = "Кожне значення")
awtf.plot(year_date_1, air_t_F_by_year_1, label = "Середнє річне значення")
awtf.plot([year_date_1[0], year_date_1[n-1]], total_mean_double[12:14], color = 'red', label = "Загальне середнє значення")
awtf.set_title("Зміна температури води (°F) відносно всіх водойм 1989-2019")
awtf.set_xlabel("Час")
awtf.set_ylabel("Температура води (°F)")
awtf.legend()
plt.show()

fig, aatc = plt.subplots()
aatc.plot(r_date, air_t_C, label = "Кожне значення")
aatc.plot(year_date_1, air_t_C_by_year_1, label = "Середнє річне значення")
aatc.plot([year_date_1[0], year_date_1[n-1]], total_mean_double[14:16], color = 'red', label = "Загальне середнє значення")
aatc.set_title("Зміна температури повітря (°C) відносно всіх водойм 1989-2019")
aatc.set_xlabel("Час")
aatc.set_ylabel("Температура повітря (°C)")
aatc.legend()
plt.show()

#--------------------------------------------------------------------------------

#виведення значень (мода) Bay
print("\nМода (солоність) відносно водойми Bay: ", Mode(Bay_salinity_n))
print("Мода (розчинений кисень) відносно водойми Bay: ", Mode(Bay_dis_oxy_n))
print("Мода (водневий показник pH) відносно водойми Bay: ", Mode(Bay_ph_n))
print("Мода (глибина Секкі) відносно водойми Bay: ", Mode(Bay_secchi_d_n))
print("Мода (глибина води) відносно водойми Bay: ", Mode(Bay_water_d_n))
print("Мода (температура води °C) відносно водойми Bay: ", Mode(Bay_w_temp_C_n))
print("Мода (температура води °F) відносно водойми Bay: ", Mode(Bay_air_t_F_n))
print("Мода (температура повітря °C) відносно водойми Bay: ", Mode(Bay_air_t_C_n))

#виведення значень (сер. арифм.) Bay
print("\nСереднє арифметичне (солоність) відносно водойми Bay: ", Arithmetic_Mean(Bay_salinity_n))
print("Середнє арифметичне (розчинений кисень) відносно водойми Bay: ", Arithmetic_Mean(Bay_dis_oxy_n))
print("Середнє арифметичне (водневий показник pH) відносно водойми Bay: ", Arithmetic_Mean(Bay_ph_n))
print("Середнє арифметичне (глибина Секкі) відносно водойми Bay: ", Arithmetic_Mean(Bay_secchi_d_n))
print("Середнє арифметичне (глибина води) відносно водойми Bay: ", Arithmetic_Mean(Bay_water_d_n))
print("Середнє арифметичне (температура води °C) відносно водойми Bay: ", Arithmetic_Mean(Bay_w_temp_C_n))
print("Середнє арифметичне (температура води °F) відносно водойми Bay: ", Arithmetic_Mean(Bay_air_t_F_n))
print("Середнє арифметичне (температура повітря °C) відносно водойми Bay: ", Arithmetic_Mean(Bay_air_t_C_n))

#виведення значень (медіана) Bay
print("\nМедіана (солоність) відносно водойми Bay: ", Median(Bay_salinity_n))
print("Медіана (розчинений кисень) відносно водойми Bay: ", Median(Bay_dis_oxy_n))
print("Медіана (водневий показник pH) відносно водойми Bay: ", Median(Bay_ph_n))
print("Медіана (глибина Секкі) відносно водойми Bay: ", Median(Bay_secchi_d_n))
print("Медіана (глибина води) відносно водойми Bay: ", Median(Bay_water_d_n))
print("Медіана (температура води °C) відносно водойми Bay: ", Median(Bay_w_temp_C_n))
print("Медіана (температура води °F) відносно водойми Bay: ", Median(Bay_air_t_F_n))
print("Медіана (температура повітря °C) відносно водойми Bay: ", Median(Bay_air_t_C_n))

#побудова графіків для водойми Bay

fig, asal = plt.subplots()
asal.plot(Bay_r_date_n, Bay_salinity_n, label = "Кожне значення")
asal.plot(Bay_year_date_1, Bay_sal_by_year_1, label = "Середнє річне значення")
asal.plot([Bay_year_date_1[0], Bay_year_date_1[n-1]], Bay_total_mean_double[:2], color = 'red', label = "Загальне середнє значення")
asal.set_title("Зміна показника солоності відносно водойми Bay 1989-2019")
asal.set_xlabel("Час")
asal.set_ylabel("Показник солоності (‰)")
asal.legend()
plt.show()

fig, aoxy = plt.subplots()
aoxy.plot(Bay_r_date_n, Bay_dis_oxy_n, label = "Кожне значення")
aoxy.plot(Bay_year_date_1, Bay_dis_oxy_by_year_1, label = "Середнє річне значення")
aoxy.plot([Bay_year_date_1[0], Bay_year_date_1[n-1]], Bay_total_mean_double[2:4], color = 'red', label = "Загальне середнє значення")
aoxy.set_title("Зміна показника розчиненого кисню (мг/л) відносно водойми Bay 1989-2019")
aoxy.set_xlabel("Час")
aoxy.set_ylabel("Показник розчиненого кисню (мг/л)")
aoxy.legend()
plt.show()

fig, aph = plt.subplots()
aph.plot(Bay_r_date_n, Bay_ph_n, label = "Кожне значення")
aph.plot(Bay_year_date_1, Bay_ph_by_year_1, label = "Середнє річне значення")
aph.plot([Bay_year_date_1[0], Bay_year_date_1[n-1]], Bay_total_mean_double[4:6], color = 'red', label = "Загальне середнє значення")
aph.set_title("Зміна водневого показника (pH) відносно водойми Bay 1989-2019")
aph.set_xlabel("Час")
aph.set_ylabel("Показник pH")
aph.legend()
plt.show()

fig, asec = plt.subplots()
asec.plot(Bay_r_date_n, Bay_secchi_d_n, label = "Кожне значення")
asec.plot(Bay_year_date_1, Bay_secchi_d_by_year_1, label = "Середнє річне значення")
asec.plot([Bay_year_date_1[0], Bay_year_date_1[n-1]], Bay_total_mean_double[6:8], color = 'red', label = "Загальне середнє значення")
asec.set_title("Зміна глибини Секкі відносно водойми Bay 1989-2019")
asec.set_xlabel("Час")
asec.set_ylabel("Глибина Секкі (м)")
asec.legend()
plt.show()

fig, awat = plt.subplots()
awat.plot(Bay_r_date_n, Bay_water_d_n, label = "Кожне значення")
awat.plot(Bay_year_date_1, Bay_water_d_by_year_1, label = "Середнє річне значення")
awat.plot([Bay_year_date_1[0], Bay_year_date_1[n-1]], Bay_total_mean_double[8:10], color = 'red', label = "Загальне середнє значення")
awat.set_title("Зміна глибини води відносно водойми Bay 1989-2019")
awat.set_xlabel("Час")
awat.set_ylabel("Глибина води (м)")
awat.legend()
plt.show()

fig, awtc = plt.subplots()
awtc.plot(Bay_r_date_n, Bay_w_temp_C_n, label = "Кожне значення")
awtc.plot(Bay_year_date_1, Bay_w_temp_C_by_year_1, label = "Середнє річне значення")
awtc.plot([Bay_year_date_1[0], Bay_year_date_1[n-1]], Bay_total_mean_double[10:12], color = 'red', label = "Загальне середнє значення")
awtc.set_title("Зміна температури води (°C) відносно водойми Bay 1989-2019")
awtc.set_xlabel("Час")
awtc.set_ylabel("Температура води (°C)")
awtc.legend()
plt.show()

fig, awtf = plt.subplots()
awtf.plot(Bay_r_date_n, Bay_air_t_F_n, label = "Кожне значення")
awtf.plot(Bay_year_date_1, Bay_air_t_F_by_year_1, label = "Середнє річне значення")
awtf.plot([Bay_year_date_1[0], Bay_year_date_1[n-1]], Bay_total_mean_double[12:14], color = 'red', label = "Загальне середнє значення")
awtf.set_title("Зміна температури води (°F) відносно водойми Bay 1989-2019")
awtf.set_xlabel("Час")
awtf.set_ylabel("Температура води (°F)")
awtf.legend()
plt.show()

fig, aatc = plt.subplots()
aatc.plot(Bay_r_date_n, Bay_air_t_C_n, label = "Кожне значення")
aatc.plot(Bay_year_date_1, Bay_air_t_C_by_year_1, label = "Середнє річне значення")
aatc.plot([Bay_year_date_1[0], Bay_year_date_1[n-1]], Bay_total_mean_double[14:16], color = 'red', label = "Загальне середнє значення")
aatc.set_title("Зміна температури повітря (°C) відносно водойми Bay 1989-2019")
aatc.set_xlabel("Час")
aatc.set_ylabel("Температура повітря (°C)")
aatc.legend()
plt.show()

#--------------------------------------------------------------------------------

#виведення значень (мода) A
print("\nМода (солоність) відносно водойми A: ", Mode(A_salinity_n))
print("Мода (розчинений кисень) відносно водойми A: ", Mode(A_dis_oxy_n))
print("Мода (водневий показник pH) відносно водойми A: ", Mode(A_ph_n))
print("Мода (глибина Секкі) відносно водойми A: ", Mode(A_secchi_d_n))
print("Мода (глибина води) відносно водойми A: ", Mode(A_water_d_n))
print("Мода (температура води °C) відносно водойми A: ", Mode(A_w_temp_C_n))
print("Мода (температура води °F) відносно водойми A: ", Mode(A_air_t_F_n))
print("Мода (температура повітря °C) відносно водойми A: ", Mode(A_air_t_C_n))

#виведення значень (сер. арифм.) A
print("\nСереднє арифметичне (солоність) відносно водойми A: ", Arithmetic_Mean(A_salinity_n))
print("Середнє арифметичне (розчинений кисень) відносно водойми A: ", Arithmetic_Mean(A_dis_oxy_n))
print("Середнє арифметичне (водневий показник pH) відносно водойми A: ", Arithmetic_Mean(A_ph_n))
print("Середнє арифметичне (глибина Секкі) відносно водойми A: ", Arithmetic_Mean(A_secchi_d_n))
print("Середнє арифметичне (глибина води) відносно водойми A: ", Arithmetic_Mean(A_water_d_n))
print("Середнє арифметичне (температура води °C) відносно водойми A: ", Arithmetic_Mean(A_w_temp_C_n))
print("Середнє арифметичне (температура води °F) відносно водойми A: ", Arithmetic_Mean(A_air_t_F_n))
print("Середнє арифметичне (температура повітря °C) відносно водойми A: ", Arithmetic_Mean(A_air_t_C_n))

#виведення значень (медіана) A
print("\nМедіана (солоність) відносно водойми A: ", Median(A_salinity_n))
print("Медіана (розчинений кисень) відносно водойми A: ", Median(A_dis_oxy_n))
print("Медіана (водневий показник pH) відносно водойми A: ", Median(A_ph_n))
print("Медіана (глибина Секкі) відносно водойми A: ", Median(A_secchi_d_n))
print("Медіана (глибина води) відносно водойми A: ", Median(A_water_d_n))
print("Медіана (температура води °C) відносно водойми A: ", Median(A_w_temp_C_n))
print("Медіана (температура води °F) відносно водойми A: ", Median(A_air_t_F_n))
print("Медіана (температура повітря °C) відносно водойми A: ", Median(A_air_t_C_n))

#побудова графіків для водойми A

fig, asal = plt.subplots()
asal.plot(A_r_date_n, A_salinity_n, label = "Кожне значення")
asal.plot(A_year_date_1, A_sal_by_year_1, label = "Середнє річне значення")
asal.plot([A_year_date_1[0], A_year_date_1[nA-1]], A_total_mean_double[:2], color = 'red', label = "Загальне середнє значення")
asal.set_title("Зміна показника солоності відносно водойми A 1989-2019")
asal.set_xlabel("Час")
asal.set_ylabel("Показник солоності (‰)")
asal.legend()
plt.show()

fig, aoxy = plt.subplots()
aoxy.plot(A_r_date_n, A_dis_oxy_n, label = "Кожне значення")
aoxy.plot(A_year_date_1, A_dis_oxy_by_year_1, label = "Середнє річне значення")
aoxy.plot([A_year_date_1[0], A_year_date_1[nA-1]], A_total_mean_double[2:4], color = 'red', label = "Загальне середнє значення")
aoxy.set_title("Зміна показника розчиненого кисню (мг/л) відносно водойми A 1989-2019")
aoxy.set_xlabel("Час")
aoxy.set_ylabel("Показник розчиненого кисню (мг/л)")
aoxy.legend()
plt.show()

fig, aph = plt.subplots()
aph.plot(A_r_date_n, A_ph_n, label = "Кожне значення")
aph.plot(A_year_date_1, A_ph_by_year_1, label = "Середнє річне значення")
aph.plot([A_year_date_1[0], A_year_date_1[nA-1]], A_total_mean_double[4:6], color = 'red', label = "Загальне середнє значення")
aph.set_title("Зміна водневого показника (pH) відносно водойми A 1989-2019")
aph.set_xlabel("Час")
aph.set_ylabel("Показник pH")
aph.legend()
plt.show()

fig, asec = plt.subplots()
asec.plot(A_r_date_n, A_secchi_d_n, label = "Кожне значення")
asec.plot(A_year_date_1, A_secchi_d_by_year_1, label = "Середнє річне значення")
asec.plot([A_year_date_1[0], A_year_date_1[nA-1]], A_total_mean_double[6:8], color = 'red', label = "Загальне середнє значення")
asec.set_title("Зміна глибини Секкі відносно водойми A 1989-2019")
asec.set_xlabel("Час")
asec.set_ylabel("Глибина Секкі (м)")
asec.legend()
plt.show()

fig, awat = plt.subplots()
awat.plot(A_r_date_n, A_water_d_n, label = "Кожне значення")
awat.plot(A_year_date_1, A_water_d_by_year_1, label = "Середнє річне значення")
awat.plot([A_year_date_1[0], A_year_date_1[nA-1]], A_total_mean_double[8:10], color = 'red', label = "Загальне середнє значення")
awat.set_title("Зміна глибини води відносно водойми A 1989-2019")
awat.set_xlabel("Час")
awat.set_ylabel("Глибина води (м)")
awat.legend()
plt.show()

fig, awtc = plt.subplots()
awtc.plot(A_r_date_n, A_w_temp_C_n, label = "Кожне значення")
awtc.plot(A_year_date_1, A_w_temp_C_by_year_1, label = "Середнє річне значення")
awtc.plot([A_year_date_1[0], A_year_date_1[nA-1]], A_total_mean_double[10:12], color = 'red', label = "Загальне середнє значення")
awtc.set_title("Зміна температури води (°C) відносно водойми A 1989-2019")
awtc.set_xlabel("Час")
awtc.set_ylabel("Температура води (°C)")
awtc.legend()
plt.show()

fig, awtf = plt.subplots()
awtf.plot(A_r_date_n, A_air_t_F_n, label = "Кожне значення")
awtf.plot(A_year_date_1, A_air_t_F_by_year_1, label = "Середнє річне значення")
awtf.plot([A_year_date_1[0], A_year_date_1[nA-1]], A_total_mean_double[12:14], color = 'red', label = "Загальне середнє значення")
awtf.set_title("Зміна температури води (°F) відносно водойми A 1989-2019")
awtf.set_xlabel("Час")
awtf.set_ylabel("Температура води (°F)")
awtf.legend()
plt.show()

fig, aatc = plt.subplots()
aatc.plot(A_r_date_n, A_air_t_C_n, label = "Кожне значення")
aatc.plot(A_year_date_1, A_air_t_C_by_year_1, label = "Середнє річне значення")
aatc.plot([A_year_date_1[0], A_year_date_1[nA-1]], A_total_mean_double[14:16], color = 'red', label = "Загальне середнє значення")
aatc.set_title("Зміна температури повітря (°C) відносно водойми A 1989-2019")
aatc.set_xlabel("Час")
aatc.set_ylabel("Температура повітря (°C)")
aatc.legend()
plt.show()

#--------------------------------------------------------------------------------

#виведення значень (мода) B
print("\nМода (солоність) відносно водойми B: ", Mode(B_salinity_n))
print("Мода (розчинений кисень) відносно водойми B: ", Mode(B_dis_oxy_n))
print("Мода (водневий показник pH) відносно водойми B: ", Mode(B_ph_n))
print("Мода (глибина Секкі) відносно водойми B: ", Mode(B_secchi_d_n))
print("Мода (глибина води) відносно водойми B: ", Mode(B_water_d_n))
print("Мода (температура води °C) відносно водойми B: ", Mode(B_w_temp_C_n))
print("Мода (температура води °F) відносно водойми B: ", Mode(B_air_t_F_n))
print("Мода (температура повітря °C) відносно водойми B: ", Mode(B_air_t_C_n))

#виведення значень (сер. арифм.) B
print("\nСереднє арифметичне (солоність) відносно водойми B: ", Arithmetic_Mean(B_salinity_n))
print("Середнє арифметичне (розчинений кисень) відносно водойми B: ", Arithmetic_Mean(B_dis_oxy_n))
print("Середнє арифметичне (водневий показник pH) відносно водойми B: ", Arithmetic_Mean(B_ph_n))
print("Середнє арифметичне (глибина Секкі) відносно водойми B: ", Arithmetic_Mean(B_secchi_d_n))
print("Середнє арифметичне (глибина води) відносно водойми B: ", Arithmetic_Mean(B_water_d_n))
print("Середнє арифметичне (температура води °C) відносно водойми B: ", Arithmetic_Mean(B_w_temp_C_n))
print("Середнє арифметичне (температура води °F) відносно водойми B: ", Arithmetic_Mean(B_air_t_F_n))
print("Середнє арифметичне (температура повітря °C) відносно водойми B: ", Arithmetic_Mean(B_air_t_C_n))

#виведення значень (медіана) B
print("\nМедіана (солоність) відносно водойми B: ", Median(B_salinity_n))
print("Медіана (розчинений кисень) відносно водойми B: ", Median(B_dis_oxy_n))
print("Медіана (водневий показник pH) відносно водойми B: ", Median(B_ph_n))
print("Медіана (глибина Секкі) відносно водойми B: ", Median(B_secchi_d_n))
print("Медіана (глибина води) відносно водойми B: ", Median(B_water_d_n))
print("Медіана (температура води °C) відносно водойми B: ", Median(B_w_temp_C_n))
print("Медіана (температура води °F) відносно водойми B: ", Median(B_air_t_F_n))
print("Медіана (температура повітря °C) відносно водойми B: ", Median(B_air_t_C_n))

#побудова графіків для водойми B

fig, asal = plt.subplots()
asal.plot(B_r_date_n, B_salinity_n, label = "Кожне значення")
asal.plot(B_year_date_1, B_sal_by_year_1, label = "Середнє річне значення")
asal.plot([B_year_date_1[0], B_year_date_1[nB-1]], B_total_mean_double[:2], color = 'red', label = "Загальне середнє значення")
asal.set_title("Зміна показника солоності відносно водойми B 1989-2019")
asal.set_xlabel("Час")
asal.set_ylabel("Показник солоності (‰)")
asal.legend()
plt.show()

fig, aoxy = plt.subplots()
aoxy.plot(B_r_date_n, B_dis_oxy_n, label = "Кожне значення")
aoxy.plot(B_year_date_1, B_dis_oxy_by_year_1, label = "Середнє річне значення")
aoxy.plot([B_year_date_1[0], B_year_date_1[nB-1]], B_total_mean_double[2:4], color = 'red', label = "Загальне середнє значення")
aoxy.set_title("Зміна показника розчиненого кисню (мг/л) відносно водойми B 1989-2019")
aoxy.set_xlabel("Час")
aoxy.set_ylabel("Показник розчиненого кисню (мг/л)")
aoxy.legend()
plt.show()

fig, aph = plt.subplots()
aph.plot(B_r_date_n, B_ph_n, label = "Кожне значення")
aph.plot(B_year_date_1, B_ph_by_year_1, label = "Середнє річне значення")
aph.plot([B_year_date_1[0], B_year_date_1[nB-1]], B_total_mean_double[4:6], color = 'red', label = "Загальне середнє значення")
aph.set_title("Зміна водневого показника (pH) відносно водойми B 1989-2019")
aph.set_xlabel("Час")
aph.set_ylabel("Показник pH")
aph.legend()
plt.show()

fig, asec = plt.subplots()
asec.plot(B_r_date_n, B_secchi_d_n, label = "Кожне значення")
asec.plot(B_year_date_1, B_secchi_d_by_year_1, label = "Середнє річне значення")
asec.plot([B_year_date_1[0], B_year_date_1[nB-1]], B_total_mean_double[6:8], color = 'red', label = "Загальне середнє значення")
asec.set_title("Зміна глибини Секкі відносно водойми B 1989-2019")
asec.set_xlabel("Час")
asec.set_ylabel("Глибина Секкі (м)")
asec.legend()
plt.show()

fig, awat = plt.subplots()
awat.plot(B_r_date_n, B_water_d_n, label = "Кожне значення")
awat.plot(B_year_date_1, B_water_d_by_year_1, label = "Середнє річне значення")
awat.plot([B_year_date_1[0], B_year_date_1[nB-1]], B_total_mean_double[8:10], color = 'red', label = "Загальне середнє значення")
awat.set_title("Зміна глибини води відносно водойми B 1989-2019")
awat.set_xlabel("Час")
awat.set_ylabel("Глибина води (м)")
awat.legend()
plt.show()

fig, awtc = plt.subplots()
awtc.plot(B_r_date_n, B_w_temp_C_n, label = "Кожне значення")
awtc.plot(B_year_date_1, B_w_temp_C_by_year_1, label = "Середнє річне значення")
awtc.plot([B_year_date_1[0], B_year_date_1[nB-1]], B_total_mean_double[10:12], color = 'red', label = "Загальне середнє значення")
awtc.set_title("Зміна температури води (°C) відносно водойми B 1989-2019")
awtc.set_xlabel("Час")
awtc.set_ylabel("Температура води (°C)")
awtc.legend()
plt.show()

fig, awtf = plt.subplots()
awtf.plot(B_r_date_n, B_air_t_F_n, label = "Кожне значення")
awtf.plot(B_year_date_1, B_air_t_F_by_year_1, label = "Середнє річне значення")
awtf.plot([B_year_date_1[0], B_year_date_1[nB-1]], B_total_mean_double[12:14], color = 'red', label = "Загальне середнє значення")
awtf.set_title("Зміна температури води (°F) відносно водойми B 1989-2019")
awtf.set_xlabel("Час")
awtf.set_ylabel("Температура води (°F)")
awtf.legend()
plt.show()

fig, aatc = plt.subplots()
aatc.plot(B_r_date_n, B_air_t_C_n, label = "Кожне значення")
aatc.plot(B_year_date_1, B_air_t_C_by_year_1, label = "Середнє річне значення")
aatc.plot([B_year_date_1[0], B_year_date_1[nB-1]], B_total_mean_double[14:16], color = 'red', label = "Загальне середнє значення")
aatc.set_title("Зміна температури повітря (°C) відносно водойми B 1989-2019")
aatc.set_xlabel("Час")
aatc.set_ylabel("Температура повітря (°C)")
aatc.legend()
plt.show()


#--------------------------------------------------------------------------------

#виведення значень (мода) C
print("\nМода (солоність) відносно водойми C: ", Mode(C_salinity_n))
print("Мода (розчинений кисень) відносно водойми C: ", Mode(C_dis_oxy_n))
print("Мода (водневий показник pH) відносно водойми C: ", Mode(C_ph_n))
print("Мода (глибина Секкі) відносно водойми C: ", Mode(C_secchi_d_n))
print("Мода (глибина води) відносно водойми C: ", Mode(C_water_d_n))
print("Мода (температура води °C) відносно водойми C: ", Mode(C_w_temp_C_n))
print("Мода (температура води °F) відносно водойми C: ", Mode(C_air_t_F_n))
print("Мода (температура повітря °C) відносно водойми C: ", Mode(C_air_t_C_n))

#виведення значень (сер. арифм.) C
print("\nСереднє арифметичне (солоність) відносно водойми C: ", Arithmetic_Mean(C_salinity_n))
print("Середнє арифметичне (розчинений кисень) відносно водойми C: ", Arithmetic_Mean(C_dis_oxy_n))
print("Середнє арифметичне (водневий показник pH) відносно водойми C: ", Arithmetic_Mean(C_ph_n))
print("Середнє арифметичне (глибина Секкі) відносно водойми C: ", Arithmetic_Mean(C_secchi_d_n))
print("Середнє арифметичне (глибина води) відносно водойми C: ", Arithmetic_Mean(C_water_d_n))
print("Середнє арифметичне (температура води °C) відносно водойми C: ", Arithmetic_Mean(C_w_temp_C_n))
print("Середнє арифметичне (температура води °F) відносно водойми C: ", Arithmetic_Mean(C_air_t_F_n))
print("Середнє арифметичне (температура повітря °C) відносно водойми C: ", Arithmetic_Mean(C_air_t_C_n))

#виведення значень (медіана) C
print("\nМедіана (солоність) відносно водойми C: ", Median(C_salinity_n))
print("Медіана (розчинений кисень) відносно водойми C: ", Median(C_dis_oxy_n))
print("Медіана (водневий показник pH) відносно водойми C: ", Median(C_ph_n))
print("Медіана (глибина Секкі) відносно водойми C: ", Median(C_secchi_d_n))
print("Медіана (глибина води) відносно водойми C: ", Median(C_water_d_n))
print("Медіана (температура води °C) відносно водойми C: ", Median(C_w_temp_C_n))
print("Медіана (температура води °F) відносно водойми C: ", Median(C_air_t_F_n))
print("Медіана (температура повітря °C) відносно водойми C: ", Median(C_air_t_C_n))

#побудова графіків для водойми C

fig, asal = plt.subplots()
asal.plot(C_r_date_n, C_salinity_n, label = "Кожне значення")
asal.plot(C_year_date_1, C_sal_by_year_1, label = "Середнє річне значення")
asal.plot([C_year_date_1[0], C_year_date_1[nC-1]], C_total_mean_double[:2], color = 'red', label = "Загальне середнє значення")
asal.set_title("Зміна показника солоності відносно водойми C 1989-2019")
asal.set_xlabel("Час")
asal.set_ylabel("Показник солоності (‰)")
asal.legend()
plt.show()

fig, aoxy = plt.subplots()
aoxy.plot(C_r_date_n, C_dis_oxy_n, label = "Кожне значення")
aoxy.plot(C_year_date_1, C_dis_oxy_by_year_1, label = "Середнє річне значення")
aoxy.plot([C_year_date_1[0], C_year_date_1[nC-1]], C_total_mean_double[2:4], color = 'red', label = "Загальне середнє значення")
aoxy.set_title("Зміна показника розчиненого кисню (мг/л) відносно водойми C 1989-2019")
aoxy.set_xlabel("Час")
aoxy.set_ylabel("Показник розчиненого кисню (мг/л)")
aoxy.legend()
plt.show()

fig, aph = plt.subplots()
aph.plot(C_r_date_n, C_ph_n, label = "Кожне значення")
aph.plot(C_year_date_1, C_ph_by_year_1, label = "Середнє річне значення")
aph.plot([C_year_date_1[0], C_year_date_1[nC-1]], C_total_mean_double[4:6], color = 'red', label = "Загальне середнє значення")
aph.set_title("Зміна водневого показника (pH) відносно водойми C 1989-2019")
aph.set_xlabel("Час")
aph.set_ylabel("Показник pH")
aph.legend()
plt.show()

fig, asec = plt.subplots()
asec.plot(C_r_date_n, C_secchi_d_n, label = "Кожне значення")
asec.plot(C_year_date_1, C_secchi_d_by_year_1, label = "Середнє річне значення")
asec.plot([C_year_date_1[0], C_year_date_1[nC-1]], C_total_mean_double[6:8], color = 'red', label = "Загальне середнє значення")
asec.set_title("Зміна глибини Секкі відносно водойми C 1989-2019")
asec.set_xlabel("Час")
asec.set_ylabel("Глибина Секкі (м)")
asec.legend()
plt.show()

fig, awat = plt.subplots()
awat.plot(C_r_date_n, C_water_d_n, label = "Кожне значення")
awat.plot(C_year_date_1, C_water_d_by_year_1, label = "Середнє річне значення")
awat.plot([C_year_date_1[0], C_year_date_1[nC-1]], C_total_mean_double[8:10], color = 'red', label = "Загальне середнє значення")
awat.set_title("Зміна глибини води відносно водойми C 1989-2019")
awat.set_xlabel("Час")
awat.set_ylabel("Глибина води (м)")
awat.legend()
plt.show()

fig, awtc = plt.subplots()
awtc.plot(C_r_date_n, C_w_temp_C_n, label = "Кожне значення")
awtc.plot(C_year_date_1, C_w_temp_C_by_year_1, label = "Середнє річне значення")
awtc.plot([C_year_date_1[0], C_year_date_1[nC-1]], C_total_mean_double[10:12], color = 'red', label = "Загальне середнє значення")
awtc.set_title("Зміна температури води (°C) відносно водойми C 1989-2019")
awtc.set_xlabel("Час")
awtc.set_ylabel("Температура води (°C)")
awtc.legend()
plt.show()

fig, awtf = plt.subplots()
awtf.plot(C_r_date_n, C_air_t_F_n, label = "Кожне значення")
awtf.plot(C_year_date_1, C_air_t_F_by_year_1, label = "Середнє річне значення")
awtf.plot([C_year_date_1[0], C_year_date_1[nC-1]], C_total_mean_double[12:14], color = 'red', label = "Загальне середнє значення")
awtf.set_title("Зміна температури води (°F) відносно водойми C 1989-2019")
awtf.set_xlabel("Час")
awtf.set_ylabel("Температура води (°F)")
awtf.legend()
plt.show()

fig, aatc = plt.subplots()
aatc.plot(C_r_date_n, C_air_t_C_n, label = "Кожне значення")
aatc.plot(C_year_date_1, C_air_t_C_by_year_1, label = "Середнє річне значення")
aatc.plot([C_year_date_1[0], C_year_date_1[nC-1]], C_total_mean_double[14:16], color = 'red', label = "Загальне середнє значення")
aatc.set_title("Зміна температури повітря (°C) відносно водойми C 1989-2019")
aatc.set_xlabel("Час")
aatc.set_ylabel("Температура повітря (°C)")
aatc.legend()
plt.show()

#--------------------------------------------------------------------------------

#виведення значень (мода) D
print("\nМода (солоність) відносно водойми D: ", Mode(D_salinity_n))
print("Мода (розчинений кисень) відносно водойми D: ", Mode(D_dis_oxy_n))
print("Мода (водневий показник pH) відносно водойми D: ", Mode(D_ph_n))
print("Мода (глибина Секкі) відносно водойми D: ", Mode(D_secchi_d_n))
print("Мода (глибина води) відносно водойми D: ", Mode(D_water_d_n))
print("Мода (температура води °C) відносно водойми D: ", Mode(D_w_temp_C_n))
print("Мода (температура води °F) відносно водойми D: ", Mode(D_air_t_F_n))
print("Мода (температура повітря °C) відносно водойми D: ", Mode(D_air_t_C_n))

#виведення значень (сер. арифм.) D
print("\nСереднє арифметичне (солоність) відносно водойми D: ", Arithmetic_Mean(D_salinity_n))
print("Середнє арифметичне (розчинений кисень) відносно водойми D: ", Arithmetic_Mean(D_dis_oxy_n))
print("Середнє арифметичне (водневий показник pH) відносно водойми D: ", Arithmetic_Mean(D_ph_n))
print("Середнє арифметичне (глибина Секкі) відносно водойми D: ", Arithmetic_Mean(D_secchi_d_n))
print("Середнє арифметичне (глибина води) відносно водойми D: ", Arithmetic_Mean(D_water_d_n))
print("Середнє арифметичне (температура води °C) відносно водойми D: ", Arithmetic_Mean(D_w_temp_C_n))
print("Середнє арифметичне (температура води °F) відносно водойми D: ", Arithmetic_Mean(D_air_t_F_n))
print("Середнє арифметичне (температура повітря °C) відносно водойми D: ", Arithmetic_Mean(D_air_t_C_n))

#виведення значень (медіана) D
print("\nМедіана (солоність) відносно водойми D: ", Median(D_salinity_n))
print("Медіана (розчинений кисень) відносно водойми D: ", Median(D_dis_oxy_n))
print("Медіана (водневий показник pH) відносно водойми D: ", Median(D_ph_n))
print("Медіана (глибина Секкі) відносно водойми D: ", Median(D_secchi_d_n))
print("Медіана (глибина води) відносно водойми D: ", Median(D_water_d_n))
print("Медіана (температура води °C) відносно водойми D: ", Median(D_w_temp_C_n))
print("Медіана (температура води °F) відносно водойми D: ", Median(D_air_t_F_n))
print("Медіана (температура повітря °C) відносно водойми D: ", Median(D_air_t_C_n))

#побудова графіків для водойми D

fig, asal = plt.subplots()
asal.plot(D_r_date_n, D_salinity_n, label = "Кожне значення")
asal.plot(D_year_date_1, D_sal_by_year_1, label = "Середнє річне значення")
asal.plot([D_year_date_1[0], D_year_date_1[nD-1]], D_total_mean_double[:2], color = 'red', label = "Загальне середнє значення")
asal.set_title("Зміна показника солоності відносно водойми D 1989-2019")
asal.set_xlabel("Час")
asal.set_ylabel("Показник солоності (‰)")
asal.legend()
plt.show()

fig, aoxy = plt.subplots()
aoxy.plot(D_r_date_n, D_dis_oxy_n, label = "Кожне значення")
aoxy.plot(D_year_date_1, D_dis_oxy_by_year_1, label = "Середнє річне значення")
aoxy.plot([D_year_date_1[0], D_year_date_1[nD-1]], D_total_mean_double[2:4], color = 'red', label = "Загальне середнє значення")
aoxy.set_title("Зміна показника розчиненого кисню (мг/л) відносно водойми D 1989-2019")
aoxy.set_xlabel("Час")
aoxy.set_ylabel("Показник розчиненого кисню (мг/л)")
aoxy.legend()
plt.show()

fig, aph = plt.subplots()
aph.plot(D_r_date_n, D_ph_n, label = "Кожне значення")
aph.plot(D_year_date_1, D_ph_by_year_1, label = "Середнє річне значення")
aph.plot([D_year_date_1[0], D_year_date_1[nD-1]], D_total_mean_double[4:6], color = 'red', label = "Загальне середнє значення")
aph.set_title("Зміна водневого показника (pH) відносно водойми D 1989-2019")
aph.set_xlabel("Час")
aph.set_ylabel("Показник pH")
aph.legend()
plt.show()

fig, asec = plt.subplots()
asec.plot(D_r_date_n, D_secchi_d_n, label = "Кожне значення")
asec.plot(D_year_date_1, D_secchi_d_by_year_1, label = "Середнє річне значення")
asec.plot([D_year_date_1[0], D_year_date_1[nD-1]], D_total_mean_double[6:8], color = 'red', label = "Загальне середнє значення")
asec.set_title("Зміна глибини Секкі відносно водойми D 1989-2019")
asec.set_xlabel("Час")
asec.set_ylabel("Глибина Секкі (м)")
asec.legend()
plt.show()

fig, awat = plt.subplots()
awat.plot(D_r_date_n, D_water_d_n, label = "Кожне значення")
awat.plot(D_year_date_1, D_water_d_by_year_1, label = "Середнє річне значення")
awat.plot([D_year_date_1[0], D_year_date_1[nD-1]], D_total_mean_double[8:10], color = 'red', label = "Загальне середнє значення")
awat.set_title("Зміна глибини води відносно водойми D 1989-2019")
awat.set_xlabel("Час")
awat.set_ylabel("Глибина води (м)")
awat.legend()
plt.show()

fig, awtc = plt.subplots()
awtc.plot(D_r_date_n, D_w_temp_C_n, label = "Кожне значення")
awtc.plot(D_year_date_1, D_w_temp_C_by_year_1, label = "Середнє річне значення")
awtc.plot([D_year_date_1[0], D_year_date_1[nD-1]], D_total_mean_double[10:12], color = 'red', label = "Загальне середнє значення")
awtc.set_title("Зміна температури води (°C) відносно водойми D 1989-2019")
awtc.set_xlabel("Час")
awtc.set_ylabel("Температура води (°C)")
awtc.legend()
plt.show()

fig, awtf = plt.subplots()
awtf.plot(D_r_date_n, D_air_t_F_n, label = "Кожне значення")
awtf.plot(D_year_date_1, D_air_t_F_by_year_1, label = "Середнє річне значення")
awtf.plot([D_year_date_1[0], D_year_date_1[nD-1]], D_total_mean_double[12:14], color = 'red', label = "Загальне середнє значення")
awtf.set_title("Зміна температури води (°F) відносно водойми D 1989-2019")
awtf.set_xlabel("Час")
awtf.set_ylabel("Температура води (°F)")
awtf.legend()
plt.show()

fig, aatc = plt.subplots()
aatc.plot(D_r_date_n, D_air_t_C_n, label = "Кожне значення")
aatc.plot(D_year_date_1, D_air_t_C_by_year_1, label = "Середнє річне значення")
aatc.plot([D_year_date_1[0], D_year_date_1[nD-1]], D_total_mean_double[14:16], color = 'red', label = "Загальне середнє значення")
aatc.set_title("Зміна температури повітря (°C) відносно водойми D 1989-2019")
aatc.set_xlabel("Час")
aatc.set_ylabel("Температура повітря (°C)")
aatc.legend()
plt.show()
