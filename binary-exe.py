import pandas as pd
from emplyee_bin import Employee 
#assuming already have data into excel file into a datafram df
df = pd.read_excel('employee.xlsx')
print("\n before the sort\n")

print("%-20s%-20s%-10s" %("id", "name", "salary"))
print("-"*50)
pList = []

for index, row in df.iterrows():
    employeeName = row['name']
    eid = row['id']
    salary = row['salary']
    
    currentemployee = Employee(employeeName,eid, salary)
    pList.append(currentemployee)
    #print(currentemployee.descripe())
    #print("after: ", currentemployee.descripe())
    
#outside loop'

for employee in pList:
  #print( employee.descripe())
    print("%-20s%-20s%-10.2f" %(employee.getid(),employee.getName(),employee.getsalary()))

print(len(pList))
print("\n after the sort\n")
print(df.sort_values('id',ascending=True,ignore_index=True))
dd=df.sort_values('id',ascending=True,ignore_index=True)
def binary_search(arr, target):
    arr=list(dd.id)
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Test case
def main():


    target_element = 4
    result_index = binary_search(dd, target_element)
    print("\n the result is:")

    if result_index != -1:
        print(f"Element {target_element} found at index {result_index}.")
    else:
        print(f"Element {target_element} not found in the list.")
main()
