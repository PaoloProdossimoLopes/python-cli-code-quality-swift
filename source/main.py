import os

K_SWIFT_EXTENSION = '.swift'
READ_FILE_MODE = 'r'


class Analiser:
    
    def __init__(self, page) -> None:
        self.page = page

    def count_number_of_imports(self) -> int:
        return self.page.count('import ')

    def count_number_of_class_declaration(self) -> int:
        return self.page.count('class ')

    def count_number_of_extensions_declared(self) -> int:
        return self.page.count('extension ')

    def count_number_of_lines(self) -> int:
        lines = self.page.split('\n')
        return len(lines)

    def count_effective_number_of_code_lines(self) -> int:
        lines = self.page.replace(' ', '').split('\n')
        while('' in lines):
            lines.remove('')
        return len(lines)

    def count_number_of_methods(self) -> int:
        return self.page.count('func ')

    def count_number_of_forceUnwrap(self) -> int:
        return self.page.count('! ')

    def count_number_of_comments(self) -> int:
        return self.page.count('//')

    def count_number_of_todo_comments(self) -> int:
        return self.page.replace(' ', '').lower().count('//todo')

    def count_number_of_fix_comments(self) -> int:
        return self.page.replace(' ', '').lower().count('//fix')

    def count_number_of_unowned_reference(self) -> int:
        return self.page.replace(' ', '').lower().count('[unowned')

    def count_number_of_variable_assinging(self) -> int:
        return self.page.count('var ')

    def count_number_of_constant_assinging(self) -> int:
        return self.page.count('let ')

    def statistic(self, name):
        object = {}
        object['file_name'] = name
        object['number_of_imports'] = self.count_number_of_imports()
        object['number_of_class_namespaces'] = self.count_number_of_class_declaration()
        object['number_of_extensions'] = self.count_number_of_extensions_declared()
        object['number_of_lines'] = self.count_number_of_lines()
        object['number_of_effective_line_of_code'] = self.count_effective_number_of_code_lines()
        object['number_of_methods'] = self.count_number_of_methods()
        object['number_of_force_unwrap'] = self.count_number_of_forceUnwrap()
        object['number_of_comments'] = self.count_number_of_comments()
        object['number_of_todo_commnets'] = self.count_number_of_todo_comments()
        object['number_of_fix_commnets'] = self.count_number_of_fix_comments()
        object['number_of_unowned'] = self.count_number_of_unowned_reference()
        object['number_of_variable_declaration'] = self.count_number_of_variable_assinging()
        object['number_of_constant_declaration'] = self.count_number_of_constant_assinging()
        return object


# route => /Users/prols/Arquivos/dev/github-repos/swift/health-tracker-app/health-tracker/App/FitFica/Source/Features/Scenes/Login/Model/
route = input('Path: ')
initial_directory = "."
file_with_properties = []
for root, dirs, files in os.walk(route + initial_directory):
    for name in files:
        if name.endswith(K_SWIFT_EXTENSION):
            path = f'{root}/{name}'
            with open(path, READ_FILE_MODE) as file:
                page = file.read()
                analiser = Analiser(page)
                object = analiser.statistic(name)
                file_with_properties.append(object)


# IMPROMINDO
for file in file_with_properties:
    print(file)
            