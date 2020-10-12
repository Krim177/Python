print("Air Quality Index Calculator")
numLocations = int(input("How many locations for this report? \n"))
i = 0
highName = ""   #THIS VARIABLE KEEPS TRACK OF THE LOCATION NAME AND EACH TIME THE LOCATION'S AQI IS GREATER THAN THE PREVIOUS AQI IT CHANGES THE LOCATION ACCORDING TO THE AQI VALUE.
totalPM2_5 = 0
negPM2_5 = 0
maximum = -1

while numLocations <= 0:
    numLocations = int(input("How many locations for this report? \n"))
    

while (i < numLocations):
    i += 1

    location = input(f"What is the name of Location {i}? \n")

    #THIS IS AQI FOR PM2.5
    PM2_5 = ((((float((input("-> Enter PM-2.5 concentration: \n")))) * 10)//1) /10) 
    if(0<= PM2_5 <= 12.0):
        clow, chigh, ilow, ihigh = 0, 12.0, 0, 50    
    elif(12.1<= PM2_5 <= 35.4):
        clow, chigh, ilow, ihigh = 12.1, 35.4, 51, 100      
    
    elif(35.5<= PM2_5 <= 55.4):
        clow, chigh, ilow, ihigh = 35.5, 55.4, 101, 150      
    
    elif(55.5<= PM2_5 <= 150.4):
        clow, chigh, ilow, ihigh = 55.5, 150.4, 151, 200      
        
    elif(150.5<= PM2_5 <= 250.4):
        clow, chigh, ilow, ihigh = 150.5, 250.4, 201, 300      
       
    elif(250.5<= PM2_5 <= 500.4):
        clow, chigh, ilow, ihigh = 250.5, 500.4, 301, 500      
    
    if(PM2_5 >=0):
        Ip = float(((((ihigh-ilow)/(chigh-clow))*(PM2_5 - clow))+ilow))
        print("   PM-2.5 concentration of", PM2_5, "is index level", round(Ip))
        totalPM2_5 = totalPM2_5 + PM2_5
    else:
        negPM2_5 += 1 #USED THIS VARIABLE TO COUNT THE NUMBER OF NEGATIVE PM2.5 SO THAT IT CAN BE SUBTRACTED IN THE END TO FIND THE AVERAGE WITHOUT HAVING TO TAKE INTO ACCOUNT THE NEGATIVE NUMBERS.
        Ip = 0
        
    
    #THIS IS AQI FOR PM10
    PM10 = (float((input("-> Enter PM-10 concentration: \n")))//1)
    if(PM10 <= 54):
        clow, chigh, ilow, ihigh = 0, 54, 0, 50      
           
    elif(PM10 <= 154):
        clow, chigh, ilow, ihigh = 55, 154, 51, 100      
    
    elif(PM10 <= 254):
        clow, chigh, ilow, ihigh = 155, 245, 101, 150      
    
    elif(PM10 <= 354):
        clow, chigh, ilow, ihigh = 255, 354, 151, 200      
         
    elif(PM10 <= 424):
        clow, chigh, ilow, ihigh = 355, 424, 201, 300      
    
    elif(PM10 <= 604):
        clow, chigh, ilow, ihigh = 425, 604, 301, 500      

    if (PM10 >= 0):   
        Ip2 = round(((((ihigh-ilow)/(chigh-clow))*(PM10 - clow))+ilow))
        print("   PM-10 concentration of", int(PM10), "is index level", Ip2)
    else:
        Ip2 = 0
    
    #THIS IS AQI FOR N02
    NO2 = (float((input("-> Enter NO-2 concentration: \n")))//1)
    if(NO2 <= 53):
        clow, chigh, ilow, ihigh = 0, 53, 0, 50      
    elif(NO2 <= 100):
        clow, chigh, ilow, ihigh = 54, 100, 51, 100        
    elif(NO2 <= 360):
        clow, chigh, ilow, ihigh = 101, 360, 101, 150        
    elif(NO2 <= 649):
        clow, chigh, ilow, ihigh = 361, 649, 151, 200       
    elif(NO2 <= 1249):
        clow, chigh, ilow, ihigh = 650, 1249, 201, 300        
    elif(NO2 <= 2049):
        clow, chigh, ilow, ihigh = 1250, 2049, 301, 500

    if(NO2 >=0):
        Ip3=float(((ihigh-ilow)/(chigh-clow)*(NO2 - clow)+ilow))
        print(f"   NO-2 concentration of {int(NO2)} is index level {round(Ip3)} \n")
    else:
        Ip3 = 0

    #THIS IS AQI FOR SO2
    SO2 = (float((input("-> Enter SO-2 concentration: \n")))//1)
    if(SO2 <= 35):
        clow, chigh, ilow, ihigh = 0, 35, 0, 50      
    elif(SO2 <= 75):
        clow, chigh, ilow, ihigh = 36, 75, 51, 100        
    elif(SO2 <= 185):
        clow, chigh, ilow, ihigh = 76, 185, 101, 150        
    elif(SO2 <= 304):
        clow, chigh, ilow, ihigh = 186, 304, 151, 200       
    elif(SO2 <= 604):
        clow, chigh, ilow, ihigh = 305, 604, 201, 300        
    elif(SO2 <= 1004):
        clow, chigh, ilow, ihigh = 605, 1004, 301, 500

    if(SO2 >=0):
        Ip4=float(((ihigh-ilow)/(chigh-clow)*(SO2 - clow)+ilow))
        print(f"   SO-2 concentration of {int(SO2)} is index level {round(Ip4)} \n")
    else:
        Ip4 = 0

    #THIS IS THE AQI FOR CO:
    CO = ((((float((input("-> Enter CO concentration: \n")))) * 10)//1) /10)
    if(CO <= 4.4):
        clow, chigh, ilow, ihigh = 0, 4.4, 0, 50      
    elif(CO <= 9.4):
        clow, chigh, ilow, ihigh = 4.5, 9.4, 51, 100        
    elif(CO <= 12.4):
        clow, chigh, ilow, ihigh = 9.5, 12.4, 101, 150        
    elif(CO <= 15.4):
        clow, chigh, ilow, ihigh = 12.5, 15.4, 151, 200       
    elif(CO <= 30.4):
        clow, chigh, ilow, ihigh = 15.5, 30.4, 201, 300        
    elif(CO <= 50.4):
        clow, chigh, ilow, ihigh = 30.5, 50.4, 301, 500

    if(CO >=0):
        Ip5=float(((ihigh-ilow)/(chigh-clow)*(CO - clow)+ilow))
        print(f"   CO concentration of {CO} is index level {round(Ip5)} \n")
    else:
        Ip5 = 0

    #THIS IS THE AQI FOR O3:
    O3 = (float((input("-> Enter O3 concentration: \n")))//1)
    if(O3 <= 125):
        clow, chigh, ilow, ihigh = 1, 2, 1, 1      
    elif(O3 <= 164):
        clow, chigh, ilow, ihigh = 125, 164, 101, 150        
    elif(O3 <= 204):
        clow, chigh, ilow, ihigh = 165, 204, 151, 200        
    elif(O3 <= 404):
        clow, chigh, ilow, ihigh = 205, 404, 201, 300       
    elif(O3 <= 604):
        clow, chigh, ilow, ihigh = 405, 604, 301, 500
        
    if(O3 > 125):
        Ip6=float(((ihigh-ilow)/(chigh-clow)*(O3 - clow)+ilow))
        print(f"   O3 concentration of {int(O3)} is index level {round(Ip6)} \n \n")
    else:
        print()
        Ip6 = 0
    
        
    #TOTAL AQI FOR THE WHOLE LOCATION IS:
    AQI = max(Ip, Ip2, Ip3,Ip4,Ip5, Ip6)
    print("AQI for", location, "is", round(AQI))

    #BELOW IS THE QUALITY LABEL FOR THE CALCULATED AQI:
    if(0<= AQI <= 50):
        air = 'Good'
    elif(51<= AQI <= 100):
        air = 'Moderate'
    elif(101<= AQI <= 150):
        air = 'Unhealthy for Sensitive Groups'
    elif(151<= AQI <= 200):
        air = 'Unhealthy'
    elif(201<= AQI <= 300):
        air = 'Very Unhealthy'
    elif(301<= AQI <= 500):
        air = 'Hazardous'
    
    print("Air Quality:", air,"\n \n")

    #TO FIND THE HIGHEST AQI FOR ALL LOCATIONS, WE CREATED A VARIABLE CALLED MAXIMUM AND THEN EACH TIME IT WOULD STORE THE HIGHEST AQI OF ALL THE LOCATIONS.
    
    if(AQI > maximum):
        maximum = AQI
        highName = location


print("Summary:")
print(f"    Location with highest AQI is {highName} ({round(maximum)})")

if(numLocations - negPM2_5 != 0):
    print(f"    Average PM-2.5 concentration: {((((totalPM2_5/ (numLocations - negPM2_5))*10)//1)/10)}") 
    



