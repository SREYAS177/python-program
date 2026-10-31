
try:
    units = float(input("Enter electricity units consumed: "))

    if units < 0:
        raise ValueError("Units cannot be negative.")

except ValueError as e:
    print("Invalid input:", e)

else:
    bill = units * 5
    print("Electricity bill: Rs.", bill)

finally:
    print("Electricity bill calculation completed.")
