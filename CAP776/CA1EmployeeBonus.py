def bonusInSalary(salary,yos):
    if yos > 10:
        return salary*0.1
        
    elif yos >= 6 and yos <= 10:
        return salary*0.08
        
    else:
        return salary*0.05
    
if __name__ == "__main__":
    salary = int(input("Enter your salary:"))
    yos = int(input("Enter number of years in service:"))
    bonus = bonusInSalary(salary,yos)
    new_salary = salary + bonus
    print("Salary after bonus is :",new_salary)
