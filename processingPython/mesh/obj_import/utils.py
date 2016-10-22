def timeStamp():
    # returns a unique filename 
    return str(year()) + str(nf(month(),2)) + str(nf(day(),2)) + "-" + str(nf(hour(),2)) + str(nf(minute(),2)) + str(nf(second(),2))