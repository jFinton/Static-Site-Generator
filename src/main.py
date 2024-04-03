from textnode import TextNode
from htmlnode import HTMLNode, ParentNode, LeafNode
from block_markdown import markdown_to_html, markdown_to_blocks
import os, shutil

file_path_public = "./public"
file_path_static = "./static"
file_path_content = "./content"


def main():
    print("Deleting public directory")
    if os.path.exists(file_path_public):
        shutil.rmtree(file_path_public)
    
    print("Copying static over to public")
    copy_files(file_path_static, file_path_public)

    index_file = file_path_public + "/index.html"
    markdown_file = file_path_content + "/index.md"
    template_file = "./template.html"

    generate_page(markdown_file, template_file, index_file)


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


def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("# "):
            text = block.split(" ", 1)
            return text[1]
    raise Exception("All pages need a h1 header for title")
            

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path} as template")

    if os.path.exists(from_path):
        file = open(from_path, "r")
        markdown = file.read()
        file.close()
    else:
        raise Exception("Source File Path does not exist")
    
    if os.path.exists(template_path):
        file = open(template_path, "r")
        template = file.read()
        file.close()
    else:
        raise Exception("Template File Path does not exist")
    
    html_node = markdown_to_html(markdown)
    html_string = html_node.to_html()
    page_title = extract_title(markdown)

    template = template.replace("{{ Title }}", page_title)
    template = template.replace("{{ Content }}", html_string)

    print(template)

    file = open(dest_path, "w")
    file.write(template)
    file.close()


main()