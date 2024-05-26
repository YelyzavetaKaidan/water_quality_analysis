import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("BKB_WaterQualityData_2020084.csv")
df['Read_Date'] = pd.to_datetime(df.Read_Date)
df = df.sort_values(by = 'Read_Date', ascending = True)

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

#видалення порожніх значень
salinity_n = [x for x in salinity if not np.isnan(x)]
dis_oxy_n = [x for x in dis_oxy if not np.isnan(x)]
ph_n = [x for x in ph if not np.isnan(x)]
secchi_d_n = [x for x in secchi_d if not np.isnan(x)]
water_d_n = [x for x in water_d if not np.isnan(x)]
w_temp_C_n = [x for x in w_temp_C if not np.isnan(x)]
air_t_F_n = [x for x in air_t_F if not np.isnan(x)]
air_t_C_n = [x for x in air_t_C if not np.isnan(x)]
year_n = [x for x in year if not np.isnan(x)]

#кількість значень
N_salinity_n = len(salinity_n)
N_dis_oxy_n = len(dis_oxy_n)
N_ph_n = len(ph_n)
N_secchi_d_n = len(secchi_d_n)
N_water_d_n = len(water_d_n)
N_w_temp_C_n = len(w_temp_C_n)
N_air_t_F_n = len(air_t_F_n)
N_air_t_C_n = len(air_t_C_n)
N_year_n = len(year_n)

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

Bay_salinity = Bay1(Bay, salinity)
Bay_dis_oxy = Bay1(Bay, dis_oxy)
Bay_ph = Bay1(Bay, ph)
Bay_secchi_d = Bay1(Bay, secchi_d)
Bay_water_d = Bay1(Bay, water_d)
Bay_w_temp_C = Bay1(Bay, w_temp_C)
Bay_air_t_F = Bay1(Bay, air_t_F)
Bay_air_t_C = Bay1(Bay, air_t_C)
Bay_r_date = Bay1(Bay, r_date)

#видалення порожніх значень
Bay_salinity_n = [x for x in Bay_salinity if not np.isnan(x)]
Bay_dis_oxy_n = [x for x in Bay_dis_oxy if not np.isnan(x)]
Bay_ph_n = [x for x in Bay_ph if not np.isnan(x)]
Bay_secchi_d_n = [x for x in Bay_secchi_d if not np.isnan(x)]
Bay_water_d_n = [x for x in Bay_water_d if not np.isnan(x)]
Bay_w_temp_C_n = [x for x in Bay_w_temp_C if not np.isnan(x)]
Bay_air_t_F_n = [x for x in Bay_air_t_F if not np.isnan(x)]
Bay_air_t_C_n = [x for x in Bay_air_t_C if not np.isnan(x)]

A_salinity = A1(A, salinity)
A_dis_oxy = A1(A, dis_oxy)
A_ph = A1(A, ph)
A_secchi_d = A1(A, secchi_d)
A_water_d = A1(A, water_d)
A_w_temp_C = A1(A, w_temp_C)
A_air_t_F = A1(A, air_t_F)
A_air_t_C = A1(A, air_t_C)
A_r_date = A1(A, r_date)

#видалення порожніх значень
A_salinity_n = [x for x in A_salinity if not np.isnan(x)]
A_dis_oxy_n = [x for x in A_dis_oxy if not np.isnan(x)]
A_ph_n = [x for x in A_ph if not np.isnan(x)]
A_secchi_d_n = [x for x in A_secchi_d if not np.isnan(x)]
A_water_d_n = [x for x in A_water_d if not np.isnan(x)]
A_w_temp_C_n = [x for x in A_w_temp_C if not np.isnan(x)]
A_air_t_F_n = [x for x in A_air_t_F if not np.isnan(x)]
A_air_t_C_n = [x for x in A_air_t_C if not np.isnan(x)]

B_salinity = B1(B, salinity)
B_dis_oxy = B1(B, dis_oxy)
B_ph = B1(B, ph)
B_secchi_d = B1(B, secchi_d)
B_water_d = B1(B, water_d)
B_w_temp_C = B1(B, w_temp_C)
B_air_t_F = B1(B, air_t_F)
B_air_t_C = B1(B, air_t_C)
B_r_date = B1(B, r_date)

#видалення порожніх значень
B_salinity_n = [x for x in B_salinity if not np.isnan(x)]
B_dis_oxy_n = [x for x in B_dis_oxy if not np.isnan(x)]
B_ph_n = [x for x in B_ph if not np.isnan(x)]
B_secchi_d_n = [x for x in B_secchi_d if not np.isnan(x)]
B_water_d_n = [x for x in B_water_d if not np.isnan(x)]
B_w_temp_C_n = [x for x in B_w_temp_C if not np.isnan(x)]
B_air_t_F_n = [x for x in B_air_t_F if not np.isnan(x)]
B_air_t_C_n = [x for x in B_air_t_C if not np.isnan(x)]

C_salinity = C1(C, salinity)
C_dis_oxy = C1(C, dis_oxy)
C_ph = C1(C, ph)
C_secchi_d = C1(C, secchi_d)
C_water_d = C1(C, water_d)
C_w_temp_C = C1(C, w_temp_C)
C_air_t_F = C1(C, air_t_F)
C_air_t_C = C1(C, air_t_C)
C_r_date = C1(C, r_date)

#видалення порожніх значень
C_salinity_n = [x for x in C_salinity if not np.isnan(x)]
C_dis_oxy_n = [x for x in C_dis_oxy if not np.isnan(x)]
C_ph_n = [x for x in C_ph if not np.isnan(x)]
C_secchi_d_n = [x for x in C_secchi_d if not np.isnan(x)]
C_water_d_n = [x for x in C_water_d if not np.isnan(x)]
C_w_temp_C_n = [x for x in C_w_temp_C if not np.isnan(x)]
C_air_t_F_n = [x for x in C_air_t_F if not np.isnan(x)]
C_air_t_C_n = [x for x in C_air_t_C if not np.isnan(x)]

D_salinity = D1(D, salinity)
D_dis_oxy = D1(D, dis_oxy)
D_ph = D1(D, ph)
D_secchi_d = D1(D, secchi_d)
D_water_d = D1(D, water_d)
D_w_temp_C = D1(D, w_temp_C)
D_air_t_F = D1(D, air_t_F)
D_air_t_C = D1(D, air_t_C)
D_r_date = A1(D, r_date)

#видалення порожніх значень
D_salinity_n = [x for x in D_salinity if not np.isnan(x)]
D_dis_oxy_n = [x for x in D_dis_oxy if not np.isnan(x)]
D_ph_n = [x for x in D_ph if not np.isnan(x)]
D_secchi_d_n = [x for x in D_secchi_d if not np.isnan(x)]
D_water_d_n = [x for x in D_water_d if not np.isnan(x)]
D_w_temp_C_n = [x for x in D_w_temp_C if not np.isnan(x)]
D_air_t_F_n = [x for x in D_air_t_F if not np.isnan(x)]
D_air_t_C_n = [x for x in D_air_t_C if not np.isnan(x)]

def Median(n, a):
    if (n % 2) == 1:
     n1 = int((n - 1) / 2)
     Me = a[n1 + 1]
    else:
     n1 = int(n / 2)
     Me = ((a[n1] + a[n1 + 1]) / 2)
    return Me

def Arithmetic_Mean(n, b):
    arm = 0
    for i in range(len(b)):
        arm = arm + b[i]
    ArM = arm / n
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
print("\nЗагальна мода (солоність) відносно всіх водойм: ", Mode(salinity_n))
print("Загальна мода (розчинений кисень) відносно всіх водойм: ", Mode(dis_oxy_n))
print("Загальна мода (водневий показник pH) відносно всіх водойм: ", Mode(ph_n))
print("Загальна мода (глибина Секкі) відносно всіх водойм: ", Mode(secchi_d_n))
print("Загальна мода (глибина води) відносно всіх водойм: ", Mode(water_d_n))
print("Загальна мода (температура води °C) відносно всіх водойм: ", Mode(w_temp_C_n))
print("Загальна мода (температура води °F) відносно всіх водойм: ", Mode(air_t_F_n))
print("Загальна мода (температура повітря °C) відносно всіх водойм: ", Mode(air_t_C_n))

#виведення значень (сер. арифм.)
print("\nЗагальне середнє арифметичне (солоність) відносно всіх водойм: ", Arithmetic_Mean(N_salinity_n, salinity_n))
print("Загальне середнє арифметичне (розчинений кисень) відносно всіх водойм: ", Arithmetic_Mean(N_dis_oxy_n, dis_oxy_n))
print("Загальне середнє арифметичне (водневий показник pH) відносно всіх водойм: ", Arithmetic_Mean(N_ph_n, ph_n))
print("Загальне середнє арифметичне (глибина Секкі) відносно всіх водойм: ", Arithmetic_Mean(N_secchi_d_n, secchi_d_n))
print("Загальне середнє арифметичне (глибина води) відносно всіх водойм: ", Arithmetic_Mean(N_water_d_n, water_d_n))
print("Загальне середнє арифметичне (температура води °C) відносно всіх водойм: ", Arithmetic_Mean(N_w_temp_C_n, w_temp_C_n))
print("Загальне середнє арифметичне (температура води °F) відносно всіх водойм: ", Arithmetic_Mean(N_air_t_F_n, air_t_F_n))
print("Загальне середнє арифметичне (температура повітря °C) відносно всіх водойм: ", Arithmetic_Mean(N_air_t_C_n, air_t_C_n))

#виведення значень (медіана)
print("\nЗагальна медіана (солоність) відносно всіх водойм: ", Median(N_salinity_n, salinity_n))
print("Загальна медіана (розчинений кисень) відносно всіх водойм: ", Median(N_dis_oxy_n, dis_oxy_n))
print("Загальна медіана (водневий показник pH) відносно всіх водойм: ", Median(N_ph_n, ph_n))
print("Загальна медіана (глибина Секкі) відносно всіх водойм: ", Median(N_secchi_d_n, secchi_d_n))
print("Загальна медіана (глибина води) відносно всіх водойм: ", Median(N_water_d_n, water_d_n))
print("Загальна медіана (температура води °C) відносно всіх водойм: ", Median(N_w_temp_C_n, w_temp_C_n))
print("Загальна медіана (температура води °F) відносно всіх водойм: ", Median(N_air_t_F_n, air_t_F_n))
print("Загальна медіана (температура повітря °C) відносно всіх водойм: ", Median(N_air_t_C_n, air_t_C_n))

#побудова графіків всі водойми
fig, asal = plt.subplots()
asal.plot(r_date, salinity)
asal.set_title("Зміна показника солоності відносно всіх водойм 1989-2019")
asal.set_xlabel("Час")
asal.set_ylabel("Показник солоності (‰)")
plt.show()

fig, aoxy = plt.subplots()
aoxy.plot(r_date, dis_oxy)
aoxy.set_title("Зміна показника розчиненого кисню (мг/л) відносно всіх водойм 1989-2019")
aoxy.set_xlabel("Час")
aoxy.set_ylabel("Показник розчиненого кисню (мг/л)")
plt.show()

fig, aph = plt.subplots()
aph.plot(r_date, ph)
aph.set_title("Зміна водневого показника (pH) відносно всіх водойм 1989-2019")
aph.set_xlabel("Час")
aph.set_ylabel("Показник pH")
plt.show()

fig, asec = plt.subplots()
asec.plot(r_date, secchi_d)
asec.set_title("Зміна глибини Секкі відносно всіх водойм 1989-2019")
asec.set_xlabel("Час")
asec.set_ylabel("Глибина Секкі (м)")
plt.show()

fig, awat = plt.subplots()
awat.plot(r_date, water_d)
awat.set_title("Зміна глибини води відносно всіх водойм 1989-2019")
awat.set_xlabel("Час")
awat.set_ylabel("Глибина води (м)")
plt.show()

fig, awtc = plt.subplots()
awtc.plot(r_date, w_temp_C)
awtc.set_title("Зміна температури води (°C) відносно всіх водойм 1989-2019")
awtc.set_xlabel("Час")
awtc.set_ylabel("Температура води (°C)")
plt.show()

fig, awtf = plt.subplots()
awtf.plot(r_date, air_t_F)
awtf.set_title("Зміна температури води (°F) відносно всіх водойм 1989-2019")
awtf.set_xlabel("Час")
awtf.set_ylabel("Температура води (°F)")
plt.show()

fig, aatc = plt.subplots()
aatc.plot(r_date, air_t_C)
aatc.set_title("Зміна температури повітря (°C) відносно всіх водойм 1989-2019")
aatc.set_xlabel("Час")
aatc.set_ylabel("Температура повітря (°C)")
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
print("\nСереднє арифметичне (солоність) відносно водойми Bay: ", Arithmetic_Mean(len(Bay_salinity_n), Bay_salinity_n))
print("Середнє арифметичне (розчинений кисень) відносно водойми Bay: ", Arithmetic_Mean(len(Bay_dis_oxy_n), Bay_dis_oxy_n))
print("Середнє арифметичне (водневий показник pH) відносно водойми Bay: ", Arithmetic_Mean(len(Bay_ph_n), Bay_ph_n))
print("Середнє арифметичне (глибина Секкі) відносно водойми Bay: ", Arithmetic_Mean(len(Bay_secchi_d_n), Bay_secchi_d_n))
print("Середнє арифметичне (глибина води) відносно водойми Bay: ", Arithmetic_Mean(len(Bay_water_d_n), Bay_water_d_n))
print("Середнє арифметичне (температура води °C) відносно водойми Bay: ", Arithmetic_Mean(len(Bay_w_temp_C_n), Bay_w_temp_C_n))
print("Середнє арифметичне (температура води °F) відносно водойми Bay: ", Arithmetic_Mean(len(Bay_air_t_F_n), Bay_air_t_F_n))
print("Середнє арифметичне (температура повітря °C) відносно водойми Bay: ", Arithmetic_Mean(len(Bay_air_t_C_n), Bay_air_t_C_n))

#виведення значень (медіана) Bay
print("\nМедіана (солоність) відносно водойми Bay: ", Median(len(Bay_salinity_n), Bay_salinity_n))
print("Медіана (розчинений кисень) відносно водойми Bay: ", Median(len(Bay_dis_oxy_n), Bay_dis_oxy_n))
print("Медіана (водневий показник pH) відносно водойми Bay: ", Median(len(Bay_ph_n), Bay_ph_n))
print("Медіана (глибина Секкі) відносно водойми Bay: ", Median(len(Bay_secchi_d_n), Bay_secchi_d_n))
print("Медіана (глибина води) відносно водойми Bay: ", Median(len(Bay_water_d_n), Bay_water_d_n))
print("Медіана (температура води °C) відносно водойми Bay: ", Median(len(Bay_w_temp_C_n), Bay_w_temp_C_n))
print("Медіана (температура води °F) відносно водойми Bay: ", Median(len(Bay_air_t_F_n), Bay_air_t_F_n))
print("Медіана (температура повітря °C) відносно водойми Bay: ", Median(len(Bay_air_t_C_n), Bay_air_t_C_n))

#побудова графіків для водойми Bay

fig, asal = plt.subplots()
asal.plot(Bay_r_date, Bay_salinity)
asal.set_title("Зміна показника солоності відносно водойми Bay 1989-2019")
asal.set_xlabel("Час")
asal.set_ylabel("Показник солоності (‰)")
plt.show()

fig, aoxy = plt.subplots()
aoxy.plot(Bay_r_date, Bay_dis_oxy)
aoxy.set_title("Зміна показника розчиненого кисню (мг/л) відносно водойми Bay 1989-2019")
aoxy.set_xlabel("Час")
aoxy.set_ylabel("Показник розчиненого кисню (мг/л)")
plt.show()

fig, aph = plt.subplots()
aph.plot(Bay_r_date, Bay_ph)
aph.set_title("Зміна водневого показника (pH) відносно водойми Bay 1989-2019")
aph.set_xlabel("Час")
aph.set_ylabel("Показник pH")
plt.show()

fig, asec = plt.subplots()
asec.plot(Bay_r_date, Bay_secchi_d)
asec.set_title("Зміна глибини Секкі відносно водойми Bay 1989-2019")
asec.set_xlabel("Час")
asec.set_ylabel("Глибина Секкі (м)")
plt.show()

fig, awat = plt.subplots()
awat.plot(Bay_r_date, Bay_water_d)
awat.set_title("Зміна глибини води відносно водойми Bay 1989-2019")
awat.set_xlabel("Час")
awat.set_ylabel("Глибина води (м)")
plt.show()

fig, awtc = plt.subplots()
awtc.plot(Bay_r_date, Bay_w_temp_C)
awtc.set_title("Зміна температури води (°C) відносно водойми Bay 1989-2019")
awtc.set_xlabel("Час")
awtc.set_ylabel("Температура води (°C)")
plt.show()

fig, awtf = plt.subplots()
awtf.plot(Bay_r_date, Bay_air_t_F)
awtf.set_title("Зміна температури води (°F) відносно водойми Bay 1989-2019")
awtf.set_xlabel("Час")
awtf.set_ylabel("Температура води (°F)")
plt.show()

fig, aatc = plt.subplots()
aatc.plot(Bay_r_date, Bay_air_t_C)
aatc.set_title("Зміна температури повітря (°C) відносно водойми Bay 1989-2019")
aatc.set_xlabel("Час")
aatc.set_ylabel("Температура повітря (°C)")
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
print("\nСереднє арифметичне (солоність) відносно водойми A: ", Arithmetic_Mean(len(A_salinity_n), A_salinity_n))
print("Середнє арифметичне (розчинений кисень) відносно водойми A: ", Arithmetic_Mean(len(A_dis_oxy_n), A_dis_oxy_n))
print("Середнє арифметичне (водневий показник pH) відносно водойми A: ", Arithmetic_Mean(len(A_ph_n), A_ph_n))
print("Середнє арифметичне (глибина Секкі) відносно водойми A: ", Arithmetic_Mean(len(A_secchi_d_n), A_secchi_d_n))
print("Середнє арифметичне (глибина води) відносно водойми A: ", Arithmetic_Mean(len(A_water_d_n), A_water_d_n))
print("Середнє арифметичне (температура води °C) відносно водойми A: ", Arithmetic_Mean(len(A_w_temp_C_n), A_w_temp_C_n))
print("Середнє арифметичне (температура води °F) відносно водойми A: ", Arithmetic_Mean(len(A_air_t_F_n), A_air_t_F_n))
print("Середнє арифметичне (температура повітря °C) відносно водойми A: ", Arithmetic_Mean(len(A_air_t_C_n), A_air_t_C_n))

#виведення значень (медіана) A
print("\nМедіана (солоність) відносно водойми A: ", Median(len(A_salinity_n), A_salinity_n))
print("Медіана (розчинений кисень) відносно водойми A: ", Median(len(A_dis_oxy_n), A_dis_oxy_n))
print("Медіана (водневий показник pH) відносно водойми A: ", Median(len(A_ph_n), A_ph_n))
print("Медіана (глибина Секкі) відносно водойми A: ", Median(len(A_secchi_d_n), A_secchi_d_n))
print("Медіана (глибина води) відносно водойми A: ", Median(len(A_water_d_n), A_water_d_n))
print("Медіана (температура води °C) відносно водойми A: ", Median(len(A_w_temp_C_n), A_w_temp_C_n))
print("Медіана (температура води °F) відносно водойми A: ", Median(len(A_air_t_F_n), A_air_t_F_n))
print("Медіана (температура повітря °C) відносно водойми A: ", Median(len(A_air_t_C_n), A_air_t_C_n))

#побудова графіків для водойми A

fig, asal = plt.subplots()
asal.plot(A_r_date, A_salinity)
asal.set_title("Зміна показника солоності відносно водойми A 1989-2019")
asal.set_xlabel("Час")
asal.set_ylabel("Показник солоності (‰)")
plt.show()

fig, aoxy = plt.subplots()
aoxy.plot(A_r_date, A_dis_oxy)
aoxy.set_title("Зміна показника розчиненого кисню (мг/л) відносно водойми A 1989-2019")
aoxy.set_xlabel("Час")
aoxy.set_ylabel("Показник розчиненого кисню (мг/л)")
plt.show()

fig, aph = plt.subplots()
aph.plot(A_r_date, A_ph)
aph.set_title("Зміна водневого показника (pH) відносно водойми A 1989-2019")
aph.set_xlabel("Час")
aph.set_ylabel("Показник pH")
plt.show()

fig, asec = plt.subplots()
asec.plot(A_r_date, A_secchi_d)
asec.set_title("Зміна глибини Секкі відносно водойми A 1989-2019")
asec.set_xlabel("Час")
asec.set_ylabel("Глибина Секкі (м)")
plt.show()

fig, awat = plt.subplots()
awat.plot(A_r_date, A_water_d)
awat.set_title("Зміна глибини води відносно водойми A 1989-2019")
awat.set_xlabel("Час")
awat.set_ylabel("Глибина води (м)")
plt.show()

fig, awtc = plt.subplots()
awtc.plot(A_r_date, A_w_temp_C)
awtc.set_title("Зміна температури води (°C) відносно водойми A 1989-2019")
awtc.set_xlabel("Час")
awtc.set_ylabel("Температура води (°C)")
plt.show()

fig, awtf = plt.subplots()
awtf.plot(A_r_date, A_air_t_F)
awtf.set_title("Зміна температури води (°F) відносно водойми A 1989-2019")
awtf.set_xlabel("Час")
awtf.set_ylabel("Температура води (°F)")
plt.show()

fig, aatc = plt.subplots()
aatc.plot(A_r_date, A_air_t_C)
aatc.set_title("Зміна температури повітря (°C) відносно водойми A 1989-2019")
aatc.set_xlabel("Час")
aatc.set_ylabel("Температура повітря (°C)")
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
print("\nСереднє арифметичне (солоність) відносно водойми B: ", Arithmetic_Mean(len(B_salinity_n), B_salinity_n))
print("Середнє арифметичне (розчинений кисень) відносно водойми B: ", Arithmetic_Mean(len(B_dis_oxy_n), B_dis_oxy_n))
print("Середнє арифметичне (водневий показник pH) відносно водойми B: ", Arithmetic_Mean(len(B_ph_n), B_ph_n))
print("Середнє арифметичне (глибина Секкі) відносно водойми B: ", Arithmetic_Mean(len(B_secchi_d_n), B_secchi_d_n))
print("Середнє арифметичне (глибина води) відносно водойми B: ", Arithmetic_Mean(len(B_water_d_n), B_water_d_n))
print("Середнє арифметичне (температура води °C) відносно водойми B: ", Arithmetic_Mean(len(B_w_temp_C_n), B_w_temp_C_n))
print("Середнє арифметичне (температура води °F) відносно водойми B: ", Arithmetic_Mean(len(B_air_t_F_n), B_air_t_F_n))
print("Середнє арифметичне (температура повітря °C) відносно водойми B: ", Arithmetic_Mean(len(B_air_t_C_n), B_air_t_C_n))

#виведення значень (медіана) B
print("\nМедіана (солоність) відносно водойми B: ", Median(len(B_salinity_n), B_salinity_n))
print("Медіана (розчинений кисень) відносно водойми B: ", Median(len(B_dis_oxy_n), B_dis_oxy_n))
print("Медіана (водневий показник pH) відносно водойми B: ", Median(len(B_ph_n), B_ph_n))
print("Медіана (глибина Секкі) відносно водойми B: ", Median(len(B_secchi_d_n), B_secchi_d_n))
print("Медіана (глибина води) відносно водойми B: ", Median(len(B_water_d_n), B_water_d_n))
print("Медіана (температура води °C) відносно водойми B: ", Median(len(B_w_temp_C_n), B_w_temp_C_n))
print("Медіана (температура води °F) відносно водойми B: ", Median(len(B_air_t_F_n), B_air_t_F_n))
print("Медіана (температура повітря °C) відносно водойми B: ", Median(len(B_air_t_C_n), B_air_t_C_n))

#побудова графіків для водойми B

fig, asal = plt.subplots()
asal.plot(B_r_date, B_salinity)
asal.set_title("Зміна показника солоності відносно водойми B 1989-2019")
asal.set_xlabel("Час")
asal.set_ylabel("Показник солоності (‰)")
plt.show()

fig, aoxy = plt.subplots()
aoxy.plot(B_r_date, B_dis_oxy)
aoxy.set_title("Зміна показника розчиненого кисню (мг/л) відносно водойми B 1989-2019")
aoxy.set_xlabel("Час")
aoxy.set_ylabel("Показник розчиненого кисню (мг/л)")
plt.show()

fig, aph = plt.subplots()
aph.plot(B_r_date, B_ph)
aph.set_title("Зміна водневого показника (pH) відносно водойми B 1989-2019")
aph.set_xlabel("Час")
aph.set_ylabel("Показник pH")
plt.show()

fig, asec = plt.subplots()
asec.plot(B_r_date, B_secchi_d)
asec.set_title("Зміна глибини Секкі відносно водойми B 1989-2019")
asec.set_xlabel("Час")
asec.set_ylabel("Глибина Секкі (м)")
plt.show()

fig, awat = plt.subplots()
awat.plot(B_r_date, B_water_d)
awat.set_title("Зміна глибини води відносно водойми B 1989-2019")
awat.set_xlabel("Час")
awat.set_ylabel("Глибина води (м)")
plt.show()

fig, awtc = plt.subplots()
awtc.plot(B_r_date, B_w_temp_C)
awtc.set_title("Зміна температури води (°C) відносно водойми B 1989-2019")
awtc.set_xlabel("Час")
awtc.set_ylabel("Температура води (°C)")
plt.show()

fig, awtf = plt.subplots()
awtf.plot(B_r_date, B_air_t_F)
awtf.set_title("Зміна температури води (°F) відносно водойми B 1989-2019")
awtf.set_xlabel("Час")
awtf.set_ylabel("Температура води (°F)")
plt.show()

fig, aatc = plt.subplots()
aatc.plot(B_r_date, B_air_t_C)
aatc.set_title("Зміна температури повітря (°C) відносно водойми B 1989-2019")
aatc.set_xlabel("Час")
aatc.set_ylabel("Температура повітря (°C)")
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
print("\nСереднє арифметичне (солоність) відносно водойми C: ", Arithmetic_Mean(len(C_salinity_n), C_salinity_n))
print("Середнє арифметичне (розчинений кисень) відносно водойми C: ", Arithmetic_Mean(len(C_dis_oxy_n), C_dis_oxy_n))
print("Середнє арифметичне (водневий показник pH) відносно водойми C: ", Arithmetic_Mean(len(C_ph_n), C_ph_n))
print("Середнє арифметичне (глибина Секкі) відносно водойми C: ", Arithmetic_Mean(len(C_secchi_d_n), C_secchi_d_n))
print("Середнє арифметичне (глибина води) відносно водойми C: ", Arithmetic_Mean(len(C_water_d_n), C_water_d_n))
print("Середнє арифметичне (температура води °C) відносно водойми C: ", Arithmetic_Mean(len(C_w_temp_C_n), C_w_temp_C_n))
print("Середнє арифметичне (температура води °F) відносно водойми C: ", Arithmetic_Mean(len(C_air_t_F_n), C_air_t_F_n))
print("Середнє арифметичне (температура повітря °C) відносно водойми C: ", Arithmetic_Mean(len(C_air_t_C_n), C_air_t_C_n))

#виведення значень (медіана) C
print("\nМедіана (солоність) відносно водойми C: ", Median(len(C_salinity_n), C_salinity_n))
print("Медіана (розчинений кисень) відносно водойми C: ", Median(len(C_dis_oxy_n), C_dis_oxy_n))
print("Медіана (водневий показник pH) відносно водойми C: ", Median(len(C_ph_n), C_ph_n))
print("Медіана (глибина Секкі) відносно водойми C: ", Median(len(C_secchi_d_n), C_secchi_d_n))
print("Медіана (глибина води) відносно водойми C: ", Median(len(C_water_d_n), C_water_d_n))
print("Медіана (температура води °C) відносно водойми C: ", Median(len(C_w_temp_C_n), C_w_temp_C_n))
print("Медіана (температура води °F) відносно водойми C: ", Median(len(C_air_t_F_n), C_air_t_F_n))
print("Медіана (температура повітря °C) відносно водойми C: ", Median(len(C_air_t_C_n), C_air_t_C_n))

#побудова графіків для водойми C

fig, asal = plt.subplots()
asal.plot(C_r_date, C_salinity)
asal.set_title("Зміна показника солоності відносно водойми C 1989-2019")
asal.set_xlabel("Час")
asal.set_ylabel("Показник солоності (‰)")
plt.show()

fig, aoxy = plt.subplots()
aoxy.plot(C_r_date, C_dis_oxy)
aoxy.set_title("Зміна показника розчиненого кисню (мг/л) відносно водойми C 1989-2019")
aoxy.set_xlabel("Час")
aoxy.set_ylabel("Показник розчиненого кисню (мг/л)")
plt.show()

fig, aph = plt.subplots()
aph.plot(C_r_date, C_ph)
aph.set_title("Зміна водневого показника (pH) відносно водойми C 1989-2019")
aph.set_xlabel("Час")
aph.set_ylabel("Показник pH")
plt.show()

fig, asec = plt.subplots()
asec.plot(C_r_date, C_secchi_d)
asec.set_title("Зміна глибини Секкі відносно водойми C 1989-2019")
asec.set_xlabel("Час")
asec.set_ylabel("Глибина Секкі (м)")
plt.show()

fig, awat = plt.subplots()
awat.plot(C_r_date, C_water_d)
awat.set_title("Зміна глибини води відносно водойми C 1989-2019")
awat.set_xlabel("Час")
awat.set_ylabel("Глибина води (м)")
plt.show()

fig, awtc = plt.subplots()
awtc.plot(C_r_date, C_w_temp_C)
awtc.set_title("Зміна температури води (°C) відносно водойми C 1989-2019")
awtc.set_xlabel("Час")
awtc.set_ylabel("Температура води (°C)")
plt.show()

fig, awtf = plt.subplots()
awtf.plot(C_r_date, C_air_t_F)
awtf.set_title("Зміна температури води (°F) відносно водойми C 1989-2019")
awtf.set_xlabel("Час")
awtf.set_ylabel("Температура води (°F)")
plt.show()

fig, aatc = plt.subplots()
aatc.plot(C_r_date, C_air_t_C)
aatc.set_title("Зміна температури повітря (°C) відносно водойми C 1989-2019")
aatc.set_xlabel("Час")
aatc.set_ylabel("Температура повітря (°C)")
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
print("\nСереднє арифметичне (солоність) відносно водойми D: ", Arithmetic_Mean(len(D_salinity_n), D_salinity_n))
print("Середнє арифметичне (розчинений кисень) відносно водойми D: ", Arithmetic_Mean(len(D_dis_oxy_n), D_dis_oxy_n))
print("Середнє арифметичне (водневий показник pH) відносно водойми D: ", Arithmetic_Mean(len(D_ph_n), D_ph_n))
print("Середнє арифметичне (глибина Секкі) відносно водойми D: ", Arithmetic_Mean(len(D_secchi_d_n), D_secchi_d_n))
print("Середнє арифметичне (глибина води) відносно водойми D: ", Arithmetic_Mean(len(D_water_d_n), D_water_d_n))
print("Середнє арифметичне (температура води °C) відносно водойми D: ", Arithmetic_Mean(len(D_w_temp_C_n), D_w_temp_C_n))
print("Середнє арифметичне (температура води °F) відносно водойми D: ", Arithmetic_Mean(len(D_air_t_F_n), D_air_t_F_n))
print("Середнє арифметичне (температура повітря °C) відносно водойми D: ", Arithmetic_Mean(len(D_air_t_C_n), D_air_t_C_n))

#виведення значень (медіана) D
print("\nМедіана (солоність) відносно водойми D: ", Median(len(D_salinity_n), D_salinity_n))
print("Медіана (розчинений кисень) відносно водойми D: ", Median(len(D_dis_oxy_n), D_dis_oxy_n))
print("Медіана (водневий показник pH) відносно водойми D: ", Median(len(D_ph_n), D_ph_n))
print("Медіана (глибина Секкі) відносно водойми D: ", Median(len(D_secchi_d_n), D_secchi_d_n))
print("Медіана (глибина води) відносно водойми D: ", Median(len(D_water_d_n), D_water_d_n))
print("Медіана (температура води °C) відносно водойми D: ", Median(len(D_w_temp_C_n), D_w_temp_C_n))
print("Медіана (температура води °F) відносно водойми D: ", Median(len(D_air_t_F_n), D_air_t_F_n))
print("Медіана (температура повітря °C) відносно водойми D: ", Median(len(D_air_t_C_n), D_air_t_C_n))

#побудова графіків для водойми D

fig, asal = plt.subplots()
asal.plot(D_r_date, D_salinity)
asal.set_title("Зміна показника солоності відносно водойми D 1989-2019")
asal.set_xlabel("Час")
asal.set_ylabel("Показник солоності (‰)")
plt.show()

fig, aoxy = plt.subplots()
aoxy.plot(D_r_date, D_dis_oxy)
aoxy.set_title("Зміна показника розчиненого кисню (мг/л) відносно водойми D 1989-2019")
aoxy.set_xlabel("Час")
aoxy.set_ylabel("Показник розчиненого кисню (мг/л)")
plt.show()

fig, aph = plt.subplots()
aph.plot(D_r_date, D_ph)
aph.set_title("Зміна водневого показника (pH) відносно водойми D 1989-2019")
aph.set_xlabel("Час")
aph.set_ylabel("Показник pH")
plt.show()

fig, asec = plt.subplots()
asec.plot(D_r_date, D_secchi_d)
asec.set_title("Зміна глибини Секкі відносно водойми D 1989-2019")
asec.set_xlabel("Час")
asec.set_ylabel("Глибина Секкі (м)")
plt.show()

fig, awat = plt.subplots()
awat.plot(D_r_date, D_water_d)
awat.set_title("Зміна глибини води відносно водойми D 1989-2019")
awat.set_xlabel("Час")
awat.set_ylabel("Глибина води (м)")
plt.show()

fig, awtc = plt.subplots()
awtc.plot(D_r_date, D_w_temp_C)
awtc.set_title("Зміна температури води (°C) відносно водойми D 1989-2019")
awtc.set_xlabel("Час")
awtc.set_ylabel("Температура води (°C)")
plt.show()

fig, awtf = plt.subplots()
awtf.plot(D_r_date, D_air_t_F)
awtf.set_title("Зміна температури води (°F) відносно водойми D 1989-2019")
awtf.set_xlabel("Час")
awtf.set_ylabel("Температура води (°F)")
plt.show()

fig, aatc = plt.subplots()
aatc.plot(D_r_date, D_air_t_C)
aatc.set_title("Зміна температури повітря (°C) відносно водойми D 1989-2019")
aatc.set_xlabel("Час")
aatc.set_ylabel("Температура повітря (°C)")
plt.show()
