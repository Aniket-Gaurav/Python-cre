# Required Module:- pip install sketchify
 
# import the sketch module
from sketchify import sketch
 
# Give the path of original image with file Name and Extension
colored_image_path = "W:\Firefox/photo1620582104.jpeg"
 
# Give the path for saving sketch without file Name and Extension
sketch_saving_path = 'W:\Firefox/'
 
# Give a Name to sketch Image
sketch_name = 'sketch.jpg'
 
# Now call the above variables in Below Method
sketch.normalsketch(colored_image_path, sketch_saving_path, sketch_name)
 
# When your Image convert this message will Print
print("Your Image Converted Successfully!")
 