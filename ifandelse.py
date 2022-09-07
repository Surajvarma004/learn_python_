from difflib import Differ


floor = 22
current_floor = input()
suraj_floor = input()
different = int(current_floor) - int(suraj_floor)

if different > 0 and different <= 22:
    print("heading up")

elif different > 22:
    print("limited floors")

elif different < 0:
    print("going niche")

elif different == 0:
    print("atak gaya bhaiya")
