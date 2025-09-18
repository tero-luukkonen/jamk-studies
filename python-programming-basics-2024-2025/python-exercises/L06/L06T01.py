# Define function "showtime(sec)"
def showtime(sec):
    hours = sec // 3600                                 # Counts whole hours
    remaining_seconds = sec % 3600                      # Counts remaining seconds
    minutes = remaining_seconds // 60                   # Counts whole minutes from remaining seconds
    seconds = remaining_seconds % 60                    # Counts the seconds that remain
    return f"{hours:02}:{minutes:02}:{seconds:02}"

# Test function "showtime(sec)"
print(showtime(500))
print(showtime(10000))
print(showtime(121000))