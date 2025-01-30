#Ül. 11

def pikim_sona(s): 
    sona = ""
    for i in s:
        if len(sona)<len(i):
             sona= i
             print(i)
    print("Pikim sõna on: "+sona)

   


sonad = ["viisnurk", "ring", "ruut", "suvaline"]
pikim_sona(sonad)