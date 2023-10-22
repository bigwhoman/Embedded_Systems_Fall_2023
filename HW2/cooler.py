State = "S1"
Heater = ""
Cooler = ""
CRS = 0
Heat = 0

def wait_for_event():
    pass 

def super_state_hot(Heat) : 
    super_state_state = "S1"
    while super_state_state != "OUT" : 
        Next_State = super_state_state
        if super_state_state == "S1":
            Heat = 1
            event = wait_for_event()
            if event == "T<5":
                Next_State = "S2"
            elif event =="T>30":
                Next_State = "OUT"
        elif super_state_state == "S2":
            Heat = 2
            event = wait_for_event()
            if event == "T>10":
                Next_State = "S1"
        
        super_state_state = Next_State
    Heat = 0

def super_state_cold(CRS) : 
    super_state_state = "S1"
    while super_state_state != "OUT" : 
        Next_State = super_state_state
        if super_state_state == "S1":
            CRS = 4
            event = wait_for_event()
            if event == "T>40":
                Next_State = "S2"
            elif event =="T<25":
                Next_State = "OUT"
        elif super_state_state == "S2":
            CRS = 6
            event = wait_for_event()
            if event == "T>45":
                Next_State = "S3"
            elif event == "T<35":
                Next_State = "S1"
        elif super_state_state == "S3":
            CRS = 8 
            event = wait_for_event()
            if event == "T<40" :
                Next_State = "S2"

        super_state_state = Next_State


while True :
    Next_State = State
    if State == "S1" :
        Heater = "OFF"
        Cooler = "OFF" 
        event = wait_for_event()
        if event == "T>35" :
            Next_State = "S2" 
        elif event == "T<15" :
            Next_State = "S3"

    elif State == "S2" :
        Heater = "OFF"
        Cooler = "ON"
        super_state_cold(CRS)
        Next_State = "S1"
    
    elif State == "S3" :
        Heater = "ON"
        Cooler = "OFF"
        super_state_hot(Heat)
        Next_State = "S1"
    State = Next_State
    