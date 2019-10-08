# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 09:06:22 2019
 
@author: lancernik
"""
 
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 23:35:43 2019
 
@author: lancernik
"""
 
 
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import string
import re
from itertools import groupby
import pandas as pd
import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kde
import seaborn as sns
from sklearn.linear_model import LinearRegression
 




#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------



audi = ["100","200","80","a1","a2","a3","a4","a4-allroad","a5","a6","a6-allroad","a7","a8","coupe","e-tron","q2","q3","q5","q7","q8","r8","rs-q3","rs3","rs4","rs5","rs6","rs7","s1","s2","s3","s4","s5","s6","s7","s8","sq5","sq7","tt"]
volksvagen = ["181","amarok","arteon","beetle","bora","buggy","caddy","california","caravelle","cc","corrado","crafter","eos","fox","garbus","golf","golf-plus","golf-sportsvan","golf-sportvan","iltis","jetta","karmann-ghia","lupo","multivan","new-beetle","other","passat","passat-cc","phaeton","polo","routan","scirocco","sharan","t-cross","t-roc","tiguan","tiguan-allspace","touareg","touran","transporter","up","vento"]
bmw = ["m","3gt","5gt","6gt","i3","i8","m2","m3","m4","m5","m6","other","seria-1","seria-2","seria-3","seria-4","seria-5","seria-6","seria-7","seria-8","x1","x2","x3","x4","x5","x5-m","x6","x6-m","x7","z1","z3","z4","z4-m"]
opel = ["adam","agila","ampera","antara","ascona","astra","calibra","campo","cascada","combo","commodore","corsa","crossland-x","frontera","grandland-x","gt","insignia","kadett","karl","manta","meriva","mokka","monterey","monza","movano","omega","other","rekord","signum","sintra","speedster","tigra","vectra","vivaro","zafira"]
mercedes = ["280","amg-gt","ce-klasa","citan","cl-klasa","cla-klasa","cls","cls-klasa","clk-klasa","cls-klasa","gl-klasa","gla-klasa","glc-klasa","gle-klasa","glk-klasa","gls-klasa","klasa-a","klasa-b","klasa-c","klasa-e","klasa-g","klasa-r","klasa-s","klasa-v","mb-100","ml","other","sl","slc","slk","slr","sls","sprinter","vaneo","vario","viano","vito","w123","w124-1984-1993","w201-190","x-klasa"]
alfa = ["145","146","147","155","156","159","164","166","33","90","alfasud","brera","crosswagon","giulia","giulietta","gt","gtv","mito","spider","stelvio"]
chevrolet = ["1500","3500"",""alero"",""apache","astro","avalanche","aveo","blazer","c-10","camaro","caprice","captiva","chevelle","chevy-van","colorado","corvette","cruze","el-camino","epica","equinox","evanda","express","hhr","impala","kalos","lacetti","malibu","matiz","monte-carlo","nubira","orlando","other","rezzo","s-10","silverado","spark","ssr","suburban","tacuma","tahoe","trailblazer","trans-sport","trax","volt"]
citroen = ["2-cv","ax","berlingo","bx","c-crosser","c-elysee","c1","c2","c3","c3-aircross","c3-picasso","c3-pluriel","c4","c4-aircross","c4-cactus","c4-grand-picasso","c4-picasso","c5","c5-aircross","c6","c8","cx","ds","ds3","ds4","ds5","evasion","gsa","jumper","jumpy-combi","nemo","other","saxo","spacetourer","visa","xantia","xm","xsara","xsara-picasso","zx"]
fiat = ["124-spider","125p","126","127","128","130","132","500","500l","500x","600","850","albea","barchetta","brava","bravo","cinquecento","coupe","croma","doblo","ducato","fiorino","freemont","fullback","grande-punto","idea","linea","marea","multipla","other","palio","panda","punto","punto-2012","punto-evo","qubo","ritmo","scudo","sedici","seicento","siena","stilo","strada","talento","tipo","ulysse","uno","x-1"]
ford= ["b-max","bronco","c-max","capri","cougar","courier","crown","econoline","ecosport","edge","escape","escort","excursion","expedition","explorer","f150","f250","f350","festiva","fiesta","focus","focus-c-max","freestyle","fusion","galaxy","granada","grand-c-max","ka","ka+","kuga","maverick","mercury","mondeo","mustang","orion","other","probe","puma","ranchero","ranger","s-max","scorpio","sierra","streetka","taunus","taurus","tempo","thunderbird","tourneo-connect","tourneo-courier","tourneo-custom","transit","transit-connect","transit-courier","transit-custom","windstar"]
honda= ["accord","aerodeck","city","civic","concerto","cr-v","cr-z","crx","fr-v","hr-v","insight","integra","jazz","legend","logo","nsx","odyssey","pilot","prelude","ridgeline","s-2000","shuttle","stream"]
hiundai= ["accent","atos","avante","azera","coupe","elantra","equus","galloper","genesis","genesis-coupe","getz","grand-santa-fe","grandeur","h-1","h-1-starex","i10","i20","i30","i30-n","i40","ioniq","ix20","ix35","ix55","kona","lantra","matrix","other","pony","s-coupe","santa-fe","santamo","sonata","terracan","trajet","tucson","veloster","xg-30","xg-350"]
kia= ["asia-rocsta","carens","carnival","ceed","cerato","clarus","magentis","mentor","niro","opirus","optima","other","picanto","pregio","pride","pro-ceed","retona","rio","sedona","sephia","shuma","sorento","soul","spectra","sportage","stinger","stonic","venga"]
mazda= ["121","2","3","323","323f","5","6","626","929","bt-50","cx-3","cx-5","cx-7","cx-9","demio","mpv","mx-3","mx-5","mx-6","other","premacy","protege","rx-7","rx-8","seria-b","tribute","xedos"]
reno = ["11","12","18","19","25","4","5","alpine-a110","avantime","captur","clio","coupe","espace","fluence","fuego","grand-espace","grand-scenic","kadjar","kangoo","koleos","laguna","latitude","master","megane","modus","other","safrane","scenic","scenic-conquest","scenic-rx4","talisman","thalia","trafic","twingo","twizy","vel-satis","wind","zoe"]
skoda = ["100","105","120","citigo","fabia","favorit","felicia","karoq","kodiaq","octavia","other","praktik","rapid","roomster","scala","superb","yeti"]



#         ^^^            ^^^             ^^^            ^^^            ^^^            ^^^            ^^^
#     
#                                M A R K I     I     M O D E L E    A U T
#
#         ^^^            ^^^             ^^^            ^^^            ^^^            ^^^            ^^^









#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------


 
def simple_get(url):
    #Zwraca none, w przypadku problemu z pobraniem danych
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
 
    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None
   
def is_good_response(resp):
    #Zwaraca True, jeżeli HTMl
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)
   
def log_error(e):
    print(e)
 
#def lastpage(page):
#    lastepage_out=0
#    lastpage = str(page.find_all(class_="page"))
#    lastpage_all = [int(s) for s in re.findall(r'\b\d+\b',lastpage)]
#    lastpage_out = lastpage_all[-1]
#    return lastepage_out
   
def LoadCarData(filename):
    
    #Wczytuje plik do dataframe
    
    dataset_out = pd.read_csv('{}.csv'.format(filename))          
    return dataset_out 

def scrappy(page,marka,model):  #Pobiera dane z konretnej strony
   
    datadict = {'Marka':'Marka','Model':'Model','Milage':[0],'Age':[0],'Price':[0],'Engine capacity':[0],'Fuel type':[0]}
    dataset = pd.DataFrame(data=datadict)
   
   
    #Zdobywa numer ostatniej strony
   
#    lastpage = str(page.find_all(class_="page"))
#    lastpage_all = [int(s) for s in re.findall(r'\b\d+\b',lastpage)]
#    lastpage_out = lastpage_all[-1]

    #Scrapowanie przebiegu
 
    milage_from_page = ''.join(map(str,(page.find_all("li", {"data-code" : "mileage"}))))
    milage_from_page_nospace = milage_from_page.translate({ord(c): None for c in string.whitespace})
    milage_page_out = [int(''.join(i)) for is_digit, i in groupby(milage_from_page_nospace, str.isdigit) if is_digit]
   
    #Scrapowanie roku z danej strony
   
    age_from_page = str(page.find_all(class_="offer-item__params-item"))
    age_from_page_nospace = age_from_page.translate({ord(c): None for c in string.whitespace})
    age_from_page_out = [int(s) for s in re.findall(r'\b\d+\b',age_from_page_nospace)]
   
    # Scrapowanie cen z danej strony
   
    price_from_page = str(page.find_all(class_="offer-price__number"))
    price_from_page_nospace = price_from_page.translate({ord(c): None for c in string.whitespace})
    price_from_page_out = [int(s) for s in re.findall(r'\b\d+\b',price_from_page_nospace)]
   
    # Scrapowanie pojemnosci silnika
   
    capacity_from_page = ''.join(map(str,(page.find_all("li", {"data-code" : "engine_capacity"}))))
    capacity_from_page_nospace = capacity_from_page.translate({ord(c): None for c in string.whitespace})
    capacity_page_out1 = [int(''.join(i)) for is_digit, i in groupby(capacity_from_page_nospace, str.isdigit) if is_digit]
    capacity_page_out = [cap for cap in capacity_page_out1 if cap !=3]
 
    # Scrapowanie rodaju paliwa
   
    fueltype_from_page = ''.join(map(str,(page.find_all("li", {"data-code" : "fuel_type"}))))
    fueltype_from_page_nospace = fueltype_from_page.translate({ord(c): None for c in string.whitespace})
    fueltype_from_page_nospace = fueltype_from_page_nospace.replace("Benzyna","1")
    fueltype_from_page_nospace = fueltype_from_page_nospace.replace("Diesel","2")
    fueltype_from_page_nospace = fueltype_from_page_nospace.replace("Benzyna+LPG","3")
    fueltype_from_page_nospace = fueltype_from_page_nospace.replace("Elektryczny","4")
    fueltype_from_page_nospace = fueltype_from_page_nospace.replace("Hybryda","5")
    fueltype_from_page_nospace = fueltype_from_page_nospace.replace("Etanol","6")
    fueltype_from_page_nospace = fueltype_from_page_nospace.replace("Benzyna+CNG ","6")
    fueltype_from_page_nospace = fueltype_from_page_nospace.replace("Wodór ","6") 
    fueltype_from_page_out = [int(s) for s in re.findall(r'\b\d+\b',fueltype_from_page_nospace)]
    
    

    marka_out=["{}".format(marka)] * len(age_from_page_out)
    model_out=["{}".format(model)] * len(age_from_page_out)
        
 
    if len(milage_page_out) == len(age_from_page_out) == len(price_from_page_out) == len(capacity_page_out) ==len(model_out) == len(marka_out) ==len(fueltype_from_page_out):
        df = pd.DataFrame(
        {'Milage':milage_page_out,
         'Age': age_from_page_out,
         'Price': price_from_page_out,
         'Engine capacity':capacity_page_out,
         'Fuel type':fueltype_from_page_out,
         'Marka':marka_out,
         'Model':model_out})

        dataset = dataset.append(df,ignore_index=True)

#    dataset = dataset['Marka', 'Model','Age', 'Engine capacity', 'Fuel type', 'Milage', 'Price']
    return dataset
 
 
def ScrapPage(marka,model,start,stop):  #Oczyszcza dane, wyznacza zares stron
    datadict = {'Milage':[0],'Age':[0],'Price':[0]}
    dataset_out = pd.DataFrame(data=datadict)

    #Zdobywa ostatnia strone
    url1 = simple_get('https://www.otomoto.pl/osobowe/{}/{}/?search%5Bfilter_float_mileage%3Afrom%5D=0&search%5Bfilter_float_engine_capacity%3Afrom%5D=0&search%5Bbrand_program_id%5D%5B0%5D=&search%5Bcountry%5D=&page=1'.format(marka,model))
#    url1 = simple_get('https://www.otomoto.pl/osobowe/{}/{}/?search%5Bfilter_enum_damaged%5D=0&search%5Bbrand_program_id%5D%5B0%5D=&search%5Bcountry%5D=&page=1'.format(marka,model))
    page1 = BeautifulSoup(url1, 'html.parser')
    try:
        lastpage = str(page1.find_all(class_="page"))
        lastpage_all = [int(s) for s in re.findall(r'\b\d+\b',lastpage)]
        lastpage_out = lastpage_all[-1]+1
        print(lastpage_out)
        
        url2 = simple_get('https://www.otomoto.pl/osobowe/{}/csafasgfags/?search%5Bfilter_float_mileage%3Afrom%5D=0&search%5Bfilter_float_engine_capacity%3Afrom%5D=0&search%5Bbrand_program_id%5D%5B0%5D=&search%5Bcountry%5D=&page=1'.format(marka,model))
        page2 = BeautifulSoup(url2, 'html.parser')
        lastpage1 = str(page2.find_all(class_="page"))
        lastpage_all1 = [int(s) for s in re.findall(r'\b\d+\b',lastpage1)]
        lastpage_out1 = lastpage_all1[-1]+1
        print(lastpage_out1)
        if lastpage_out == lastpage_out1:
            print("Error")
            return None
        
    except:
        return None

    for i in range(start,lastpage_out):  #Docelowo 1, lastpage
        time.sleep(4)
       
        #To w formacie beda kolejne argumenty, tj za opel i corsa
        url = simple_get('https://www.otomoto.pl/osobowe/{}/{}/?search%5Bfilter_float_mileage%3Afrom%5D=0&search%5Bfilter_float_engine_capacity%3Afrom%5D=0&search%5Bbrand_program_id%5D%5B0%5D=&search%5Bcountry%5D=&page={}'.format(marka,model,i))
#        url = simple_get('https://www.otomoto.pl/osobowe/{}/{}/?search%5Bfilter_enum_damaged%5D=0&search%5Bbrand_program_id%5D%5B0%5D=&search%5Bcountry%5D=&page={}'.format(marka,model,i))
#        FORCE SCRAP
#        url = simple_get('https://www.otomoto.pl/osobowe/lexus/is/ii-2005-2012/?search%5Bfilter_float_engine_capacity%3Afrom%5D=2450&search%5Bfilter_float_engine_capacity%3Ato%5D=2550&search%5Bbrand_program_id%5D%5B0%5D=&search%5Bcountry%5D=')
        page = BeautifulSoup(url, 'html.parser')
#        print(scrappy(page))
        dataset_out = dataset_out.append(scrappy(page,marka,model), ignore_index=True)
        print(dataset_out)
        print(i)
    dataset_out.to_csv('{}-{}.csv'.format(marka,model))
    return dataset_out
 
 
def ClearCarData(dataset_out):
    clear = dataset_out.Milage[((dataset_out.Milage - dataset_out.Milage.mean()) / dataset_out.Milage.std()).abs() > 2]
    #Wybiera listę indexow ktore maja byc usuniete
    
    clear = dataset_out.Milage[((dataset_out.Milage - dataset_out.Milage.mean()) / dataset_out.Milage.std()).abs() > 2]
    clear = clear.append(dataset_out.Age[((dataset_out.Age - dataset_out.Age.mean()) / dataset_out.Age.std()).abs() > 2])
    clear = clear.append(dataset_out.Price[((dataset_out.Price - dataset_out.Price.mean()) / dataset_out.Price.std()).abs() > 3])
    test1 = clear.index.get_values()
    
    #Usuwa duplikaty z listy indexów do usunięcia
    
    test = []
    for i in test1:
       if i not in test:
          test.append(i)

    #Usuwa z dataframu wybrane indexy

    for i in range(0,len(test)):
        dataset_out = dataset_out.drop(test[i],axis=0)
        
    return dataset_out
 
    
def regress(x,y):
    model = LinearRegression()
    model.fit(x,y)
    model.predict([[100]])
   
    x_test = np.linspace(0,400000)
    y_pred = model.predict(x_test[:,None])
   
    plt.scatter(x,y,s=2)
    plt.plot(x_test,y_pred,'r')
    plt.legend(['Regresja', 'Kropeczki'])
    plt.show()
 
def Plot1(x,y):
 
    # Evaluate a gaussian kde on a regular grid of nbins x nbins over data extents
    nbins=300
    k = kde.gaussian_kde([x,y])
    xi, yi = np.mgrid[x.min():x.max():nbins*1j, y.min():y.max():nbins*1j]
    zi = k(np.vstack([xi.flatten(), yi.flatten()]))
     
    # Make the plot
    plt.pcolormesh(xi, yi, zi.reshape(xi.shape))
    plt.show()
     
    # Change color palette
    plt.pcolormesh(xi, yi, zi.reshape(xi.shape), cmap=plt.cm.Greens_r)
    plt.show()
def Plot2(x,y):
    # Make the plot
    plt.hexbin(x, y, gridsize=(15,15) )
    plt.show()
     
    # We can control the size of the bins:
    plt.hexbin(x, y, gridsize=(150,150) )
    plt.show()
def Plot3(x,y):          
    sns.jointplot(x, y, kind='scatter')
    sns.jointplot(x, y, kind='hex')
    sns.jointplot(x, y, kind='kde')
       
    # Then you can pass arguments to each type:
    sns.jointplot(x, y, kind='scatter', s=200, color='m', edgecolor="skyblue", linewidth=2)
     
    # Custom the color
    sns.set(style="white", color_codes=True)
    sns.jointplot(x, y, kind='kde', color="skyblue",xlim={-30000,300000})
   
   
 
 
 
#         ^^^            ^^^             ^^^            ^^^            ^^^            ^^^            ^^^
#     
#                              F U N K C J E     P R O G R A M U
#
#         ^^^            ^^^             ^^^            ^^^            ^^^            ^^^            ^^^   
    
    
    
    
    
    
    
   
 
   
#LoadCarData(filename):  Wczytuje dane z pliku CSV stworzonego przez funkcje ScrapPage,
#dodatkowo oczyszcza z danych odstajcych  
 
#ClearCarData():   Oczyszcza z danych odstajacych, zdiala tylko dla df o nazwie dataset_out
 
 
 
 
# 1)   Scrapuje dane
 
#         Marka,   model, start, stop
#dataset_out = ScrapPage("audi" ,"cabriolet",  1     ,2)
#dataset_out.to_csv('datasetvv40.csv')
#dataset_out = pd.read_csv('datasetgolf.csv')  #9-45
# 
 
# 2)   Wczytuje zeskrapowane dane
# 
##dataset_out = LoadCarData("datasetvv40")
#dataset_out = ClearCarData(dataset_out)
 
#Rozne ploty  
# 
#x=dataset_out['Milage']
#y=dataset_out['Age']
#
#
#Plot1(x,y)
#Plot2(x,y)
#Plot3(x,y)
 
 
 
 
 
 
 
#Regresja przebiegu względem czasu
##
#a=np.array(dataset_out['Milage'].tolist()).reshape(-1,1)
#b=np.array(dataset_out['Age'].tolist()).reshape(-1,1)
#regress(a,b)
# 
 
 
 
 
 
#To sie przyda do wojewodztw
#for i, li in enumerate(page.select('li')):  #To się przyda do wojedzowtw
#    print(i, li.text)








#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------

#
#audi = ["100","200","80","a1","a2","a3","a4","a4-allroad","a5","a6","a6-allroad","a7","a8","coupe","e-tron","q2","q3","q5","q7","q8","r8","rs-q3","rs3","rs4","rs5","rs6","rs7","s1","s2","s3","s4","s5","s6","s7","s8","sq5","sq7","tt"]
#for item in audi:
#    dataset_out = ScrapPage("audi" ,item,  1     ,6)
    
#volksvagen = ["181","amarok","arteon","beetle","bora","buggy","caddy","california","caravelle","cc","corrado","crafter","eos","fox","garbus","golf","golf-plus","golf-sportsvan","golf-sportvan","iltis","jetta","karmann-ghia","lupo","multivan","new-beetle","other","passat","passat-cc","phaeton","polo","routan","scirocco","sharan","t-cross","t-roc","tiguan","tiguan-allspace","touareg","touran","transporter","up","vento"]
#for item in volksvagen:
#    dataset_out = ScrapPage("volkswagen" ,item,  1     ,2)
  
#bmw = ["m","3gt","5gt","6gt","i3","i8","m2","m3","m4","m5","m6","other","seria-1","seria-2","seria-3","seria-4","seria-5","seria-6","seria-7","seria-8","x1","x2","x3","x4","x5","x5-m","x6","x6-m","x7","z1","z3","z4","z4-m"]
#for item in bmw:
#    dataset_out = ScrapPage("bmw" ,item,  1     ,2)
  
#opel = ["adam","agila","ampera","antara","ascona","astra","calibra","campo","cascada","combo","commodore","corsa","crossland-x","frontera","grandland-x","gt","insignia","kadett","karl","manta","meriva","mokka","monterey","monza","movano","omega","other","rekord","signum","sintra","speedster","tigra","vectra","vivaro","zafira"]
#for item in opel:
#    dataset_out = ScrapPage("opel" ,item,  1     ,2)

#for item in mercedes:
#    dataset_out = ScrapPage("mercedes-benz" ,item,  1     ,2)
#    
#for item in alfa:
#    dataset_out = ScrapPage("alfa-romeo" ,item,  1     ,2)
#    
#for item in chevrolet:
#    dataset_out = ScrapPage("chevrolet" ,item,  1     ,2)
#    
#    

#         ^^^            ^^^             ^^^            ^^^            ^^^            ^^^            ^^^
#     
#        Z E S K R A P O W A N E          Z E S K R A P O W A N E           Z E S K R A P O W A N E 
#
#         ^^^            ^^^             ^^^            ^^^            ^^^            ^^^            ^^^
#




    
    
    
    
#for item in citroen:
#    dataset_out = ScrapPage("citroen" ,item,  1     ,2)
##    
#for item in fiat:
#    dataset_out = ScrapPage("fiat" ,item,  1     ,2)

#for item in ford:
#    dataset_out = ScrapPage("ford" ,item,  1     ,2)
#    
#for item in honda:
#    dataset_out = ScrapPage("honda" ,item,  1     ,2)
#    
#for item in hiundai:
#    dataset_out = ScrapPage("hyundai" ,item,  1     ,2)
#    
#for item in kia:
#    dataset_out = ScrapPage("kia" ,item,  1     ,2)
#    
#for item in mazda:
#    dataset_out = ScrapPage("mazda" ,item,  1     ,2)
#
#







# Tu 01.07.2019

toyota = ["yaris","yaris-verso"]
#"4-runner","auris","avalon","avensis","avensis-verso","aygo","c-hr","camry","camry-solara","carina","celica","corolla","corolla-verso","crown","fj","gt86","hiace","highlander","hilux","iq","land-cruiser","matrix","mr2","paseo","previa","prius","prius+","proace","proace-verso","rav4","sequoia","sienna","starlet","supra","tacoma","tercel","tundra","urban-cruiser","venza","verso","verso-s",
volvo = ["245","262","340","744","780","850","855","945","c30","c70","other","s40","s60","s70","s80","s90","seria-200","seria-400","seria-700","seria-900","v40","v50","v60","v70","v90","xc-40","xc-60","xc-70","xc-90"]
    

for item in toyota:
    dataset_out = ScrapPage("toyota" ,item,  1     ,2)
    
for item in volvo:
    dataset_out = ScrapPage("volvo" ,"item",  1     ,2)
    



test = pd.read_csv("0polaczone.csv")



#
#def LoadCarData(filename):
#    
#    #Wczytuje plik do dataframe
#    
#    dataset_out = pd.read_csv('{}.csv'.format(filename))  
#    
#    
#    #Wybiera listę indexow ktore maja byc usuniete
#    
#    clear = dataset_out.Milage[((dataset_out.Milage - dataset_out.Milage.mean()) / dataset_out.Milage.std()).abs() > 2]
#    clear = clear.append(dataset_out.Age[((dataset_out.Age - dataset_out.Age.mean()) / dataset_out.Age.std()).abs() > 2])
#    clear = clear.append(dataset_out.Price[((dataset_out.Price - dataset_out.Price.mean()) / dataset_out.Price.std()).abs() > 3])
#    test1 = clear.index.get_values()
#    
#    #Usuwa duplikaty z listy indexów do usunięcia
#    
#    test = []
#    for i in test1:
#       if i not in test:
#          test.append(i)
#
#    #Usuwa z dataframu wybrane indexy
#
#    for i in range(0,len(test)):
#        dataset_out = dataset_out.drop(test[i],axis=0)
#        
#    return dataset_out
# 