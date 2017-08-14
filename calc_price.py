#!/usr/bin/python

import sys

if __name__ == '__main__':
    buyPrice = float(raw_input("Buy price: "))
    sellPrice = float(raw_input("Sell price: "))
    units = float(raw_input("Total units: "))

    bittrexFeeRaw = 0.25 #percentage
    bittrexFee = bittrexFeeRaw / 100

    #cost to buy:
    unitsExcludingFee = buyPrice * units
    fee = (buyPrice * units) * bittrexFee
    totalToBuy = unitsExcludingFee + fee

    print("\n\tBuy costs")
    print("Raw  : "+str(unitsExcludingFee)+" (excluding fee)")
    print("Fee  : "+str(fee))
    print("Total: "+str(totalToBuy)+" (including fee)\n")

    #cost to sell
    unitsExcludingFee = sellPrice * units
    fee = (sellPrice * units) * bittrexFee
    totalToSell = unitsExcludingFee - fee

    print("\tSell amounts")
    print("Raw  : "+str(unitsExcludingFee)+" (excluding fee)")
    print("Fee  : "+str(fee))
    print("Total: "+str(totalToSell)+" (minus fee)\n")

    profitLoss = totalToSell - totalToBuy
    print("Profit/loss: "+str(profitLoss))