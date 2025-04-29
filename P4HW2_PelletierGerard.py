# Gerard Pelletier
# 3/13/2025
# P3HW2
# Modifying P3HW2 to use looks.
employee_name = "start"
run_count = 0
regpaylist = []
grosspaylist = []
overtimepaylist = []
while employee_name != "Done":
    employee_name = input("Enter Employee's name or 'Done' to terminate: ")
    if employee_name != "Done":
        hours_worked = float(input("Enter number of hours worked: "))
        pay_rate = float(input("Enter employee's pay rate: "))
        if hours_worked > 40:
            overtime_hours = hours_worked - 40 
            reg_pay = 40 * pay_rate
            overtime_pay_rate = pay_rate * 1.5
            overtime_pay = overtime_hours * overtime_pay_rate
            total_pay = reg_pay + overtime_pay
            reg_pay = 40 * pay_rate
        else:
            overtime_hours = 0
            reg_pay = hours_worked * pay_rate
            overtime_pay = 0
            total_pay = reg_pay


        print("-----"*8)
        print(f"{'Employee name:':<18}{employee_name}")
        print("")
        print(f"{'Hours Worked':<17} {'Pay Rate':<17} {'OverTime':<17} {'OverTime Pay':<17} {'RegHour Pay':<17} {'Gross Pay':<17}")
        print("-----"*20)
        print(f"{hours_worked:<17} ${pay_rate:<17.2f} {overtime_hours:<17} ${overtime_pay:<17.2f} ${reg_pay:<17.2f} ${total_pay:<17.2f}")
        run_count = run_count+1 
        overtimepaylist.append(overtime_pay)
        regpaylist.append(reg_pay)
        grosspaylist.append(total_pay)
    else:
        print("Program Ending! here are your results.")
print("")
print(f"Total number of employees entered: {run_count}")
print(f"Total amount paid for overtime: ${sum(overtimepaylist):.2f}")
print(f"Total amount paid for regular hours: ${sum(regpaylist):.2f}")
print(f"Total amount paid for gross: ${sum(grosspaylist):.2f}")