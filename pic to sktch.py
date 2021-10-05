# Required Module:- pip install sketchify
 
# import the sketch module
from sketchify import sketch
 
# Give the path of original image with file Name and Extension
colored_image_path = "//select the image location you want to conver"
 
# Give the path for saving sketch without file Name and Extension
sketch_saving_path = '//location to save the converted file'
 
# Give a Name to sketch Image
sketch_name = '//rename image'
 
# Now call the above variables in Below Method
sketch.normalsketch(colored_image_path, sketch_saving_path, sketch_name)
 
# When your Image convert this message will Print
print("Your Image Converted Successfully!")
 
