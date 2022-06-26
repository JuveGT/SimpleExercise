from datetime import datetime
from datetime import timedelta

def returnSum(Surahs):
    sum = 0
    remaining = 0
    completed = input("What is the number of the last completed surah you have finished reading? ")
    additional = input("Have you read any additional ayas in the current Surah you are reading? ")
    for k,v in Surahs.items():
        if v[0] <= int(completed):
            sum = sum + v[1]
            remaining = 6236 - sum
    WhenComplete(remaining)
    return sum + int(additional)
##-----
def WhenComplete(remaining):
    speed = input("How many ayas per day do you plan on reading? ")
    finish_days = remaining/int(speed)
    dt = datetime.now()
    td = timedelta(days=finish_days)
    finish_date = dt + td
    print("\nYour finish date is calculated to be: \n", finish_date)



Surahs ={'al-start':[0,0],'fatihah':[1,7],'baqarah':[2,286],'imran':[3,200],'nisa':[4,176],'maidah':[5,120],'anam':[6,165],'araf':[7,206],
'anfal':[8,75],'tawbah':[9,129],'yunus':[10,109],'hud':[11,123],'yusuf':[12,111],'rad':[13,43],'ibrahim':[14,52]
,'hijr':[15,99],'nahl':[16,128],'isra':[17,111],'kahf':[18,110],'maryam':[19,98],'taha':[20,135],'anbiya':[21,112],'hajj':[22,78],
'muminum':[23,118],'nur':[24,64],'furqan':[25,77],'shuara':[26,227],'naml':[27,93],'qasus':[28,88],'ankabut':[29,69]
,'rum':[30,60],'luqman':[31,34],'sajdah':[32,30],'ahzab':[33,73],'saba':[34,54],'fatir':[35,45],'ya.sin':[36,83]
,'saffat,':[37,182],'saad':[38,88],'zumar':[39,75],'ghafir':[40,85],'fussilat':[41,54],'shura':[42,53],'zukhruf':[43,89]
,'dukhan':[44,59],'jathiyah':[45,37],'ahqaf':[46,35],'muhammad':[47,38],'fath':[48,29],'hujurat':[49,18],'qaf':[50,45]
,'dhariyat':[51,60],'tur':[52,49],'najm':[53,62],'qamar':[54,55],'rahman':[55,78],'waqiah':[56,96],'hadeed':[57,29],'mujadilah':[58,22]
,'hashr':[59,24],'mumtahannah':[60,13],'saff':[61,14],'jumuah':[62,11],'munafiqun':[63,11],'taghabun':[64,18],
'talaq':[65,12],'tahreem':[66,12],'mulk':[67,30],'qalam':[68,52],'haqqah':[69,52],'maaarij':[70,44],'nuh':[71,28]
,'jinn':[72,28],'muzzammil':[73,20],'muddaththir':[74,56],'qiyamah':[75,40],'insan':[76,31],'mursalat':[77,50]
,'naba':[78,40],'naziat':[79,46],'abasa':[80,42],'takweer':[81,29],'infitar':[82,19],'mutaffifeen':[83,36]
,'inshiqaq':[84,25],'buruj':[85,22],'tariq':[86,17],'ala':[87,19],'ghashiyah':[88,26],'fajr':[89,30],'balad':[90,20]
,'shams':[91,15],'layl':[92,21],'dhuha':[93,11],'sharh':[94,8],'tin':[95,8],'alaq':[96,19],'qadr':[97,5]
,'bayyinah':[98,8],'zalzalah':[99,8],'adiyat':[100,11],'qariah':[101,11],'takathur':[102,8],'asr':[103,3],'humazah':[104,9]
,'feel':[105,5],'quraish':[106,4],'maun':[107,7],'kawthar':[108,3],'kafiroon':[109,6],'nasr':[110,3],'masad':[111,5],'iklas':[112,4]
,'falaq':[113,5],'nas':[114,6]}


print("The sum of the Ayahs you have read is:", returnSum(Surahs), "out of 6236 Ayahs")
