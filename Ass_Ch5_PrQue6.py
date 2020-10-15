# Assignment Ch5 File Handling

# Que 6

# Display the state names start with M

def MSEARCH(STATES):
    for i in range (len(STATES)):
        if STATES[i][0] == "M" :
            print (STATES[i])
STATES=["MP","UP","WB","TN","MH","MZ","DL","BH","RJ","HR"]
MSEARCH(STATES)
