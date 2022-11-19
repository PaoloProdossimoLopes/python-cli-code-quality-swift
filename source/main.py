import os

K_SWIFT_EXTENSION = '.swift'
READ_FILE_MODE = 'r'

def count_number_of_imports(page) -> int:
    return page.count('import ')

def count_number_of_class_declaration(page) -> int:
    return page.count('class ')

def count_number_of_extensions_declared(page) -> int:
    return page.count('extension ')

def count_number_of_lines(page) -> int:
    lines = page.split('\n')
    return len(lines)

def count_effective_number_of_code_lines(page) -> int:
    lines = page.replace(' ', '').split('\n')
    while('' in lines):
        lines.remove('')
    return len(lines)

def count_number_of_methods(page) -> int:
    return page.count('func ')

def count_number_of_forceUnwrap(page) -> int:
    return page.count('! ')

# Runner
route = '/Users/prols/Arquivos/dev/github-repos/swift/health-tracker-app/health-tracker/App/FitFica/Source/Features/Scenes/Login/Model' + '/'
initial_directory = "."
file_with_properties = []
for root, dirs, files in os.walk(route + initial_directory):
    for name in files:
        object = {}
        if name.endswith(K_SWIFT_EXTENSION):
            path = f'{root}/{name}'
            with open(path, READ_FILE_MODE) as file:
                page = file.read()
                object['file_name'] = name
                object['number_of_imports'] = count_number_of_imports(page)
                object['number_of_class_namespaces'] = count_number_of_class_declaration(page)
                object['number_of_extensions'] = count_number_of_extensions_declared(page)
                object['number_of_lines'] = count_number_of_lines(page)
                object['number_of_effective_line_of_code'] = count_effective_number_of_code_lines(page)
                object['number_of_methods_in_file'] = count_number_of_methods(page)
                object['number_of_force_unwrap'] = count_number_of_forceUnwrap(page)

        file_with_properties.append(object)
# print(file_with_properties)


# IMPROMINDO
for file in file_with_properties:
    print(file)
            