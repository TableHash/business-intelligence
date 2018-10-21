import numpy as np

#student[height,weight,Vital capacity,timeOf50m,timeOf1000m,gender,single,province,hair condition,grade]
student1=[183,155,4000,7.0,345,1,1,'henan','good','junior']
student2=[170,130,3500,8.0,428,1,0,'hubei','limited','sophmore']
student3=[168,120,3200,8.8,440,0,1,'hunan','fair','freshmen']
student4=[160,100,3400,9.1,450,0,1,'zhejiang','good','senior']
attribute_nums=len(student1)

grade_map={}
grade_map['freshmen']=1
grade_map['sophmore']=2
grade_map['junior']=3
grade_map['senior']=4
map_num=4

students=[student1,student2,student3,student4]
students=np.array(students)
student_nums=len(students)

dissimilarity=np.zeros(shape=(student_nums,student_nums))

numeric_attribute=np.array(students[:,:5],dtype=float)
diff=np.max(numeric_attribute,axis=0)-np.min(numeric_attribute,axis=0)
for i in range(student_nums):
    for j in range(i+1,student_nums):
        distance=abs(numeric_attribute[i]-numeric_attribute[j])/diff
        distance=np.sum(distance)
        dissimilarity[i,j]+=distance
        dissimilarity[j,i]+=distance

for i in range(student_nums):
    for j in range(i+1,student_nums):
        distance=0
        for k in range(5,9):
            if students[i,k]!=students[j,k]:
                distance+=1
        dissimilarity[i,j]+=distance
        dissimilarity[j,i]+=distance

temp=np.zeros(shape=(student_nums,))
for i in range(student_nums):
    attr=students[i,9]
    temp[i]=(grade_map[attr]-1)/(map_num-1)
diff=np.max(temp)-np.min(temp)
for i in range(student_nums):
    for j in range(i+1,student_nums):
        distance=abs(temp[i]-temp[j])/diff
        dissimilarity[i,j]+=distance
        dissimilarity[j,i]+=distance

dissimilarity/=attribute_nums
print (dissimilarity)
