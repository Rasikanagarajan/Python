import pandas as pandy
# 1st
data={
    'Orderid':[101,102,103,104,105],
    'Customer':["Rasika","indhu","mathi","anu","muthu"],
    'city':["chennai","coimbatore","chennai","madurai","ERode"],
    'category':["elecronics","fashion","IT","electronics","Groceries"],
    'Amount':[2500,3000,24000,56000,6700]
}
# only shows customer,category,amount
print("\n only shows customer,category,amount")
df=pandy.DataFrame(data)
print(df[['Customer','category','Amount']])

# filter rows
print("\n filter amount > 5000")
print(df[df['Amount']>5000])

print("\n filter city=chennai")
print(df[df['city']=='chennai'])

# group by & aggregate
print("\n sum of city")
grp=df.groupby('city')['Amount'].sum()
print(grp)

print("\n Avg of category")
grp=df.groupby('category')['Amount'].mean()
print(grp)

print("\n max of each customer")
grp=df.groupby('Customer')['Amount'].max()
print(grp)

# 2nd
data={
    'Patient':["Rasika","indhu","mathi","anu","muthu"],
    'Age':[22,34,33,24,45],
    'Department':["cardiology","diabetology","cardiology","neurology","ortho"],
    'Disease':["heart","sugar","heart","stroke","fracture"],
    'Bill':[2500,3000,24000,56000,6700]
}
df=pandy.DataFrame(data)


# only shows patient,disease,bill
print("\n only shows patient,disease,bill")
df=pandy.DataFrame(data)
print(df[['Patient','Disease','Bill']])

# filter rows
print("\n Patient & Bill amount > 5000")
print(df[df['Bill']>5000][['Patient', 'Bill']])

# filter patient fromm cardiology dept 
print("\n Patients from cardiology department")
print(df[df['Department'] == "cardiology"])

# aged between 40 and 60 
print("\n aged between 40 and 60")
print(df[df['Age']>40 & 60])

# group by & aggregate
print("\n Avg of dept bill")
grp=df.groupby('Department')['Bill'].mean()
print(grp)

print("\n sum of Disease")
grp=df.groupby('Disease')['Bill'].sum()
print(grp)

grp=df.groupby('Department').agg({'Bill':['max','min']})
print(grp)

# 3rd
data={
    'Name':["Rasika","indhu","mathi","anu","muthu"],
    'Department':["CSE","It","CSE","ESE","BE"],
    'Sem':[5,5,5,5,5],
    'Subject':["maths","python","maths","os","networks"],
    'Marks':[87,90,89,67,78]
}
df=pandy.DataFrame(data)


# only shows name,subject,marks
print("\n only shows name,subject,marks")
df=pandy.DataFrame(data)
print(df[['Name','Subject','Marks']])

# filter marks
print("\n mark > 80")
print(df[df['Marks']>80])

# rows only cse dept
print("\n rows only CSE dept")
print(df[df['Department']=="CSE"])

# rows only python sub
print("\n rows only python sub")
print(df[df['Subject']=="python"])

print("\naverage marks per subject")
print(df.groupby('Subject')['Marks'].mean())

print("\nhighest marks per Department")
print(df.groupby('Department')['Marks'].max())

print("\n count of students per Department")
print(df.groupby('Department')['Name'].count())
