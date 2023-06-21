def average(salary: list[int]) -> float:
    salary.sort()
    avg = 0.0
    for i in range(1,len(salary) - 1):
        avg += salary[i]
    return avg / (len(salary) - 2)

def main():
    salary = [600,300,700,100]
    res = average(salary=salary)
    print(res)

main()
