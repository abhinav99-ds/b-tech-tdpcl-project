# optimizer.py

def optimize(params):
    altitude = params["altitude"]
    speed = params["speed"]

    recommendation = {}

    if altitude < 30000:
        recommendation["altitude"] = altitude + 2000
    else:
        recommendation["altitude"] = altitude

    if speed > 800:
        recommendation["speed"] = speed - 50
    else:
        recommendation["speed"] = speed

    return recommendation