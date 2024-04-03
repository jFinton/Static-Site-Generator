from textnode import TextNode
from htmlnode import HTMLNode, ParentNode, LeafNode
import os, shutil

file_path_public = "./public"
file_path_static = "./static"


def main():
    print("Deleting public directory")
    if os.path.exists(file_path_public):
        shutil.rmtree(file_path_public)
    
    print("Copying static over to public")
    copy_files(file_path_static, file_path_public)


def copy_files(source_file_path, dest_file_path):
    if not os.path.exists(source_file_path):
        raise Exception("Source Path does not exist.")
    
    if not os.path.exists(dest_file_path):
        os.mkdir(dest_file_path)
    
    for file in os.listdir(source_file_path):
        original_file = os.path.join(source_file_path, file)
        dest_file = os.path.join(dest_file_path, file)
        print(f"Copying {original_file} towards {dest_file}")
        if os.path.isfile(original_file):
            shutil.copy(original_file, dest_file)
        else:
            copy_files(original_file, dest_file)


main()