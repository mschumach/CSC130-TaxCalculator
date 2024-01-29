purchaseAmount = int(input("Insert purchase amount:"))
countyTaxAmount = purchaseAmount * 0.025
stateTaxAmount = purchaseAmount * 0.05
totalTaxAmount = countyTaxAmount + stateTaxAmount
totalSaleAmount = purchaseAmount + purchaseAmount * 0.075

print(f"Total Sale Amount: ${totalSaleAmount}")
print(f"County Tax Amount: ${countyTaxAmount}")
print(f"State Tax Amount: ${stateTaxAmount}")      
