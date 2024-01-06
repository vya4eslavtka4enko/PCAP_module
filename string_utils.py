def halve_string(input_string):
    counter = int(len(input_string)/2)
    if len(input_string)%2==0:
        return(input_string[0:counter],input_string[counter:])
    else:
        return(input_string[0:counter+1],input_string[counter:])
        
