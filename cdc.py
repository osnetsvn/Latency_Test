import csv


def convert(string):
        list_var=list(string.split("\t"))
        return list_var


file_name=input("Enter the trace's file name:")
f=open(file_name,"r")    
latency_list=[]
line_num=0

while line_num<11:
    f.readline()
    line_num=line_num+1
while True:
    content=f.readline()
    if not content:
        break
    latency_list.append(convert(content).pop())


##### Latency Value Calculation in Microseconds
latency_list=[int (i) for i in latency_list]
latency_list.sort()
final_latency_list=[]
for i in latency_list:
    i=i*0.001
    final_latency_list.append(i)

#### Cumulative distribution calculation

cumulative_list=[]
list_length=len(final_latency_list)
rep_value=1.0/list_length

cumulative_list.append(rep_value)


for i in range(1,list_length-1):
    value=rep_value+ cumulative_list[i-1]
    cumulative_list.append(value)
cumulative_list.append(1)



final_csv=[]

for i in range(0,list_length):
        temp_list=[]
        temp_list.append(final_latency_list[i])
        temp_list.append(cumulative_list[i])
        final_csv.append(temp_list) 




csv_file=open('timer_CDC.csv','w+')

with csv_file:
    write=csv.writer(csv_file)
    write.writerows(final_csv)



f.close()
