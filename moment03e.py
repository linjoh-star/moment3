print('\033[1m'"Skattkalkylator 3000"'\033[1m'"\n")

def calculate_taxes(annual_salary):
    kskatt = 0
    lskatt = 0
    sskatt = 0
    vskatt = 0

    if annual_salary < 19247:
        pass
    elif annual_salary < 468700:
        kskatt = 0.2136
        lskatt = 0.1148
    elif annual_salary < 675700:
        kskatt = 0.2136
        lskatt = 0.1148
        sskatt = 0.2
    else:
        kskatt = 0.2136
        lskatt = 0.1148
        sskatt = 0.2
        vskatt = 0.05

    total_tax = annual_salary * (kskatt + lskatt + sskatt + vskatt)
    net_income = annual_salary - total_tax

    return {
        "annual_salary": annual_salary, 
        "total_tax": total_tax, 
        "net_income": net_income, 
        "kskatt": kskatt, 
        "lskatt": lskatt, 
        "sskatt": sskatt, 
        "vskatt": vskatt, 
        "total_tax_percent": total_tax / annual_salary
    }

salaries = [1500, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000]

cols = "| {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<12} | {:<10} | {:<10} | {:<15} |"
print(cols.format("Årslön", "Månadslön", "Totalskatt", "Netto/mån", "Kommunals.", "Landstingss.", "Statlig s.", "Värnskatt", "Total skatt i %"))

for salary in salaries:
    taxes = calculate_taxes(salary)
    print(cols.format(
        int(taxes["annual_salary"]), 
        int(salary), 
        int(taxes["total_tax"]), 
        int(taxes["net_income"]), 
        int(taxes["kskatt"] * salary), 
        int(taxes["lskatt"] * salary), 
        int(taxes["sskatt"] * salary), 
        int(taxes["vskatt"] * salary), 
        int(taxes["total_tax_percent"] * 100)
    ))
