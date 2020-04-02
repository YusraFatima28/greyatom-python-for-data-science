# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data=np.genfromtxt(path,delimiter=",", skip_header=1)
print("\nData: \n\n", data)
print("\nType of data: \n\n", type(data))


#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
census=np.concatenate((new_record,data))
#Code starts here



# --------------
#Code starts here
age=census[:,0]
print(age)
max_age=age.max()
min_age=age.min()
age_mean=age.mean()
age_std=np.std(age)
print(age_mean,age_std)


# --------------
#Code starts here
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]


#Finding the length of the above created subsets
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

#Printing the length of the above created subsets
print('Race_0: ', len_0)
print('Race_1: ', len_1)
print('Race_2: ', len_2)
print('Race_3: ', len_3)
print('Race_4: ', len_4)

#Storing the different race lengths with appropriate indexes
race_list=[len_0, len_1,len_2, len_3, len_4]

#Storing the race with minimum length into a variable 
minority_race=race_list.index(min(race_list))

#Code ends here


# --------------
#Code starts here
senior_citizens=census[census[:,0]>60]
print(senior_citizens)
working_hours_sum=np.sum(senior_citizens,axis=0)
working_hours_sum=working_hours_sum[6]
senior_citizens_len=len(senior_citizens)
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)
#working_hours_sum=


# --------------
#Code starts here
high,low=census[census[:,1]>10],census[census[:,1]<=10]
avg_pay_high=np.mean(high,0)
avg_pay_high=avg_pay_high[7]
avg_pay_low=np.mean(low,0)
avg_pay_low=avg_pay_low[7]
if avg_pay_high==avg_pay_low:
    print('better education leads to better pay')



