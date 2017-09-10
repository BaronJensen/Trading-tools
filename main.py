import datamvp
start = 671.40

amount = 0.03923

low = start - 0.02 #Risk of 
#lowtobuy()
currents = datamvp.val
import time


direction = ["up","down", "--"]
def  getPredictedDirection():
		return direction[0]

for current in currents: #Simulates real time market
	current_tmp = current["y"]

	

	stop_p = current["y"] - (current["y"]*0.09) #Stop limit wth profit
	stop_s = start + (start*0.02)  #Stop limit safe

	colchon = 0.00

	profit =  stop_p  - stop_s
	total_profit = 0


	
	print "Current price: ", current["y"]
	print "Starting price: ", start
	print "(stop_p, stop_s)", stop_p, " , ",stop_s
	print ">>>Profit on game: ", profit
	print "total profit: ", total_profit
	print "colchon: ", colchon
	print "Direccion del mercado", "UP"
	print "==============================================="


	if current["y"] <= stop_s and profit > 0:
		print "[Mantener o  Salir] - Ganancia segura"

		if (current["y"] *0.01 + stop_p) >= current["y"] and profit > 0: #if goes up and 
			tlr =  current["y"] - stop_p
			colchon = colchon + tlr
			print "[Compra] - me dio pal colchon: ", tlr

	elif current["y"] > stop_s and profit > 0:
		print "[RetiCon, retirar profit, retirar todo, pivotear ] - solo profit"
	else:
		print "[Mercada abajo] Mantener o rendirme"

	#print "==============================================="
	#print "Lista de opciones"
	#Opcion handler
	#print "==============================================="
	#print "Ganancia en esta operacion 0.0001btc"

	time.sleep(0.5)
