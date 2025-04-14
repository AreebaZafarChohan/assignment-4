import os

def main():
    i = 0
    path = "E:/Q3/assignment_4/Assignments_01/06_Bulk_Fire_Renamer/cli_based/files"
    for filename in os.listdir(path):
        my_dest = f"image{i}.jpg"
        my_source = os.path.join(path, filename) # image0.jpg, image1.jpg, etc.
        my_dest = os.path.join(path, my_dest) # E:/.../filename.jpg
        try:
            os.rename(my_source, my_dest) # filename.jpg -->  image0.jpg 
            i += 1
        except FileNotFoundError:
            print(f"File not found: {my_source}")
        except Exception as e:
            print(f"Error renaming {filename}: {e}")
        
if __name__ == "__main__":
    main()
