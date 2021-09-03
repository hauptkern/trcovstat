import json,random,sys
from trcovstat import covdata
if len(sys.argv)<2:
    print("Usage : python3 "+sys.argv[0]+ " <days>")
    sys.exit()
daycount=int(sys.argv[1])
weekdata=covdata.range(0,daycount)
weekdata.reverse()
red='\033[31m'
green='\033[32m'
print("Turkey "+str(daycount)+" Days COVID-19 Case Statistics")
for i in range(0,len(weekdata)):
    info=json.loads(weekdata[i])
    color=None
    date=info["tarih"]
    casecount=info["gunluk_vaka"]
    casecount=int(casecount.replace(".",""))
    if i==0:
        nextcountdata=json.loads(weekdata[i+1])
        nextcasecount=nextcountdata["gunluk_vaka"]
        nextcasecount=int(nextcasecount.replace(".",""))
        if casecount>nextcasecount:
            color=red
        else:
            color=green
    elif i>=1:
        prevcountdata=json.loads(weekdata[i-1])
        prevcasecount=prevcountdata["gunluk_vaka"]
        prevcasecount=int(prevcasecount.replace(".",""))
        if prevcasecount>casecount:
            color=green
        elif casecount>prevcasecount:
            color=red
    barcount=round(casecount/1000)
    print(color+date+"   :   "+("█"*barcount)+" "+str(casecount))
print('\033[39m') # reset colors