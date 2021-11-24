# Increase or Decrease volume using python
# Importing the required library
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

print("How much Percentage You required to Increase or Decrease:")
vol = int(input(
	"Enter volume percentage:"))  # Asking the user to enter the percentage of volume he required to increase or decrease
print("Do you want to increase or decrease volume?")
print("Choose 1.To Increase 2.To Decrease",
	  sep='\n')  # Asking the user to choose the option to increase or decrease volume
ch = int(input("Your choice:"))

vol = vol * -1 if ch == 2 else vol  # If user choose to increase volume then vol will be multiplied by -1
# here -1 is used to decrease the volume and 1 is used to increase the volume
# Get default audio device using PyCAW
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
	IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Get current volume
currentVolumeDb = volume.GetMasterVolumeLevel()
volume.SetMasterVolumeLevel(currentVolumeDb + vol, None)  # Increase or decrease the volume
# NOTE: -6.0 dB = half volume !

print("Now go and check volume changed!")  # Nothifying the user that the volume has been changed
