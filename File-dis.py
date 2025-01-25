import os
import shutil

# Define download folder path
download_folder = 'Directory_Paths'

# Define file categories with their extensions
file_categories = {
    'videos': ['.mp4', '.mkv', '.avi'],
    'images': ['.jpg', '.jpeg', '.png', '.gif'],
    'documents': ['.pdf', '.docx', '.xlsx', '.pptx', '.txt', '.csv', '.html', '.md'],
    'music': ['.mp3', '.wav'],
    'other': ['.*']  # Catch-all for unknown file types
}

# Check if download folder exists; create it if necessary
if not os.path.exists(download_folder):
    try:
        os.makedirs(download_folder)
        print(f"Created download folder: {download_folder}")
    except Exception as e:
        print(f"Error creating download folder: {e}")
        exit(1)

# Create subdirectories for each category
for category, extensions in file_categories.items():
    category_path = os.path.join(download_folder, category)
    
    try:
        # Check if category directory exists; create it if necessary
        if not os.path.exists(category_path):
            os.makedirs(category_path)
            print(f"Created directory: {category_path}")
        else:
            print(f"Directory already exists: {category_path}")
    except Exception as e:
        print(f"Error creating directory '{category}': {e}")

# Function to move and copy files to appropriate directories
def move_files():
    # List all files in the download folder
    for file_name in os.listdir(download_folder):
        file_path = os.path.join(download_folder, file_name)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Determine file extension
        file_ext = os.path.splitext(file_name)[1].lower()
        found_category = False
        
        # Check each category and move the file accordingly
        for category, extensions in file_categories.items():
            if file_ext in extensions or extensions == ['.*']:
                category_path = os.path.join(download_folder, category)
                dest_file_path = os.path.join(category_path, file_name)
                
                # Copy file to category folder
                try:
                    shutil.copy(file_path, dest_file_path)
                    print(f"Copied {file_name} to {category} folder.")
                except Exception as e:
                    print(f"Error copying {file_name} to {category}: {e}")
                found_category = True
                break
        
        # If file doesn't match any known category, move it to 'other'
        if not found_category:
            other_folder = os.path.join(download_folder, 'other')
            dest_file_path = os.path.join(other_folder, file_name)
            try:
                shutil.copy(file_path, dest_file_path)
                print(f"Copied {file_name} to 'other' folder.")
            except Exception as e:
                print(f"Error copying {file_name} to 'other': {e}")

# Run the move and copy files function
move_files()