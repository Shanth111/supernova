
def rate(oldmax,oldmin,newmax,newmin,value):
    if value is 0:
        return(0)
    else:    
        oldrange = (oldmax-oldmin)
        newrange = (newmax-newmin)
        new_value = (((value-oldmin)*newrange)/oldrange)+newmin
        return(new_value)

def avgrate(opinion,popularity):
    print(opinion)
    avg = (opinion+popularity)/2
    return(int(avg))

# Value Methods
def senti_value(value):
    oldmax = 200
    oldmin = -200
    newmax = 100
    newmin = 0
    return(rate(oldmax,oldmin,newmax,newmin,value))

def popularity_value(value):
    if value > 20000:
        oldmax = 200000
        oldmin = 20000
        newmax = 100
        newmin = 91
        return(rate(oldmax,oldmin,newmax,newmin,value))

    elif value > 10000:
        oldmax = 20000
        oldmin = 10000
        newmax = 90
        newmin = 81
        return(rate(oldmax,oldmin,newmax,newmin,value))

    elif value > 1000:
        oldmax = 10000
        oldmin = 1000
        newmax = 80
        newmin = 51
        return(rate(oldmax,oldmin,newmax,newmin,value))

    elif value > 100:
        oldmax = 1000
        oldmin = 100
        newmax = 50
        newmin = 31
        return(rate(oldmax,oldmin,newmax,newmin,value))

    elif value > 50:
        oldmax = 100
        oldmin = 50
        newmax = 30
        newmin = 21
        return(rate(oldmax,oldmin,newmax,newmin,value))

    elif value > 15:
        oldmax = 50
        oldmin = 15
        newmax = 20
        newmin = 16
        return(rate(oldmax,oldmin,newmax,newmin,value))
                   
    elif value > 0:
        oldmax = 15
        oldmin = 1
        newmax = 15
        newmin = 5
        return(rate(oldmax,oldmin,newmax,newmin,value))

    else:
        return(rate(0,0,0,0,0))
        
