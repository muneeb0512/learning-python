import statistics
import hfpy_utils
CHARTS="charts/"
FOLDER= "swimdata/"

def read_swim_data(filename):
    swimmer,age,distance,stroke = filename.removesuffix(".txt").split("-")
    with open(FOLDER+filename) as file:
        lines=file.readlines() 
        times= lines[0].strip().split(",") 

    alltimes=[]

    for t in times:
        if ":"in t:
            min,rest= t.split(":")
            seconds,hundreths = rest.split(".")
            alltimes.append( (int(min)*60*100)+ (int(seconds)*100) + int(hundreths))
        else:
            minutes=0
            seconds,hundreths = t.split(".")
            alltimes.append( int(minutes)*60*100+(int(seconds)*100) + int(hundreths))

        
      

    average= statistics.mean(alltimes)

   # mins_secs,hundreds= str(round(average/100,2)).split(".") #take value of avergae,divide by 100 and then round to 2 dp. convert rounded vaue to str and round the result to 2 decimal places 
    mins_secs,hundreds= f"{(average/100):.2f}".split(".") #2f says floating number created by dividing average by 100 should be diplayed to 2 dp ,we removed the round 
    mins_secs=int(mins_secs)
    minutes= mins_secs // 60 #// is floor divison which means it chops off everything after .

    seconds= mins_secs- minutes*60

    average= str(minutes)+ ":"+ f"{seconds:0>2}"+ "."+ hundreds #if its just 2 seconds so rather than showing just 2 we wanna show 02 so we left pad the seconds value with zero if needs to be

    return swimmer,age,distance,stroke,times,average,alltimes





def produce_bar_chart(FN):
    swimmer,age,distance,stroke,times,average,converts=read_swim_data(FN)
    from_max= max(converts)
    times.reverse()
    converts.reverse()
    #these methods modify the list in place
    title= f"{swimmer} (Under {age}) {distance} - {stroke}"
    header=f""" <!DOCTYPE html>
    <html>
        <head>
            <title>
            {title}
            </title>
        </head>
        <body>
        <h3>{title}</h3>
    """
    body=""

    for n,t in enumerate(times):
        bar_width=hfpy_utils.convert2range(converts[n], 0, from_max, 0, 350) 
        body=body+ f"""
        <svg height="30" width="400">
            <rect height="30" width="{bar_width}" style="fill:rgb(0,0,255);" />
        </svg>{t}<br />
    """
        
    footer= f""" <p>Average time: {average}</p>
        </body>
    </html>
    """
    page=header+body+footer
    save_to= f"""{CHARTS}{FN.removesuffix(".txt")}.html"""

    with open(save_to,"w") as myfile:
        print(page,file=myfile)

    return save_to




