import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("Book1.csv")
# print(df["age"].mean())
# print(round(df["age"].var(),3))
# print(round(df["age"].std(),3))
a=round(df.final[df.final>90].count()/df.final.count(),3)
b=round(df.age[df.age<25].count()/df.age.count(),3)
c=len(df[(df.age<25) & (df.final>90)])
c/=len(df)
print(a)
print(b)
print(c)

correlation = df['age'].corr(df['final'])
print(correlation)















# df=pd.read_csv("Bike_sharing_data.csv")
# # count_mnt=df["cnt"].value_counts().sort_index(ascending=False)
# # print(f"from {22} to {22+(8714-22)/5}")
# # for i in range(1,5):
# #     print(f"from {22+i*((8714-22)/5)} to {22+(8714-22)/5*(i+1)}")

# # print(count_mnt)
# # avg_casual=df["casual"]
# # print(avg_casual.mean())

# # std_casual=df["casual"]
# # print(std_casual.std())

# # hum_prob=df.hum[df.hum>0.7].count()/df.hum.count()
# # avail_bike=df.cnt[df.cnt==0].count()
# weather_sit=df.weathersit[df.weathersit==1].count()/df.weathersit.count()
# print(weather_sit)