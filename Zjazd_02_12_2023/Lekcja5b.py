browser_speed = {"Chrome" : 100, "Opera" : 20, "Firefox" : 75, "Safari" : 60, "Edge" : 45}

print(list(browser_speed.keys()))
print(list(browser_speed.values()))
print(list(browser_speed.items()))

print(list(browser_speed.keys())[list(browser_speed.values()).index(75)])

