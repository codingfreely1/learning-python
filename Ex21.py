file_name = raw_input('File Name :')
content = raw_input('Content:')

with open(file_name, 'w') as open_file:
    open_file.write(content)