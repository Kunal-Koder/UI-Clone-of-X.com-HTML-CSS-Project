# Load the third image
from PIL import Image


input_path3 = "/Icons/sidebar/Explore"
output_path3 = "/Icons/sidebar/Explore_transparent.png"

# Open the image and convert to RGBA
image3 = Image.open("/Icons/sidebar/Explore").convert("RGBA")

# Get data
datas3 = image3.getdata()

# Remove black background
newData3 = []
for item in datas3:
    if item[0] == 0 and item[1] == 0 and item[2] == 0:
        newData3.append((0, 0, 0, 0))  # Transparent
    else:
        newData3.append(item)

# Update image data and save
image3.putdata(newData3)
image3.save(output_path3, "PNG")

output_path3
