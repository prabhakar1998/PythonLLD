def ms_to_hr(duration_ms):
    seconds = duration_ms // 10 # it should be 1000 in ideal world for simulation set to 10
    minutes = seconds // 60 
    hrs = minutes // 60
    return hrs