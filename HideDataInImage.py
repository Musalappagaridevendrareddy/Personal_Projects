# Hide data in image

from stegano import lsb

image = 'background.png'  # Taking any image
new_image = 'hidden.png'  # New image with hidden data
msg = 'I love python'  # Message to store in image
lsb.hide(image, message=msg).save(new_image)  # Storing data in image and saving that image

message = lsb.reveal(new_image)  # Revealing data from image
print('Message hidden in image is:', message)  # Printing the hidden data or message
