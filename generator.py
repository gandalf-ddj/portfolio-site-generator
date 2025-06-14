from jinja2 import Environment, FileSystemLoader
import markdown
import os
import json
import zipfile

def zip_output_folder(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, folder_path)
                zipf.write(abs_path, rel_path)

# env setup
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('base.html')

# bio.md file managment
with open('content/bio.md', 'r', encoding='utf-8') as file:
    data = file.read()
    if not data:
        raise ValueError('bio.md is empty. Add some content.')
    else:
        bio_html = markdown.markdown(data)
bio_page = template.render(
    title = 'About Me',
    heading = 'My Bio',
    content = bio_html
)
with open('output/index.html', 'w', encoding='utf-8') as file:
    file.write(bio_page)

# projects.json file managment
with open('content/projects.json', 'r', encoding='utf-8') as file:
    projects_data = json.load(file)
    if not projects_data:
        raise ValueError('projects.json is empty. Add some content.')
projects_page=template.render(
    title='Projects',
    heading='My Projects',
    projects=projects_data
)
with open('output/projects.html', 'w', encoding='utf-8') as file:
    file.write(projects_page)

# skills.md file managment
with open('content/skills.md', 'r', encoding='utf-8') as file:
    data = file.read()
    if not data:
        raise ValueError('skills.md is empty. Add some content.')
    else:
        skills_html = markdown.markdown(data)
skills_page = template.render(
    title = 'About Me',
    heading = 'Skills',
    content = skills_html
)
with open('output/skills.html', 'w', encoding='utf-8') as file:
    file.write(skills_page)

# contact.md file managment
with open('content/contact.md', 'r', encoding='utf-8') as file:
    data = file.read()
    if not data:
        raise ValueError('contact.md is empty. Add some content.')
    else:
        contact_html = markdown.markdown(data)
contact_page = template.render(
    title = 'About Me',
    heading = 'Contact Info',
    content = contact_html
)
with open('output/contact.html', 'w', encoding='utf-8') as file:
    file.write(contact_page)

zip_output_folder('output', 'output/site.zip')
print("✅ Site exported as output/site.zip")