import os

class FileStatisticDTO:
    def __init__(
        self, path, name, number_of_imports, 
        number_of_class_namespaces, number_of_extensions, 
        number_of_lines, number_of_effective_line_of_code,
        number_of_methods, number_of_force_unwrap,
        number_of_comments, number_of_todo_commnets, 
        number_of_fix_commnets, number_of_unowned,
        number_of_variable_declaration,
        number_of_constant_declaration,
        number_of_prints
    ) -> None:

        self.path = path
        self.name = name
        self.number_of_imports = number_of_imports
        self.number_of_class_namespaces = number_of_class_namespaces
        self.number_of_extensions = number_of_extensions
        self.number_of_lines = number_of_lines
        self.number_of_effective_line_of_code = number_of_effective_line_of_code
        self.number_of_methods = number_of_methods
        self.number_of_force_unwrap = number_of_force_unwrap
        self.number_of_comments = number_of_comments
        self.number_of_todo_commnets = number_of_todo_commnets
        self.number_of_fix_commnets = number_of_fix_commnets
        self.number_of_unowned = number_of_unowned
        self.number_of_variable_declaration = number_of_variable_declaration
        self.number_of_constant_declaration = number_of_constant_declaration
        self.number_of_prints = number_of_prints

    def __str__(self) -> str:
        header = f'* {self.name} *'
        separator = len(header) * '*'
        return f'''
        {header}
        {separator}
        - PATH: {self.path}
        - NUMBER OF IMPORTS: {self.number_of_imports}
        - NUMBER OF CLASSES: {self.number_of_class_namespaces}
        - NUMBER OF EXTENSIONS: {self.number_of_extensions}
        - NUMBER OF LINES (LOC): {self.number_of_lines}
        - NUMBER OF EFFECTIVE LINES: {self.number_of_effective_line_of_code}
        - NUMBER OF METHODS: {self.number_of_methods}
        - NUMBER OF FORCE UNWRAP (!): {self.number_of_force_unwrap}
        - NUMBER OF COMMENTS (ALL TIPES): {self.number_of_comments}
        - NUMBER OF TO-DO COMMENTS: {self.number_of_todo_commnets}
        - NUMBER OF FIX COMMENTS: {self.number_of_fix_commnets}
        - NUMBER OF UNOWNED REFERENCES: {self.number_of_unowned}
        - NUMBER OF VARIABLES DECALRED (var): {self.number_of_variable_declaration}
        - NUMBER OF CONSTANTS DECALRED (let): {self.number_of_constant_declaration}
        - NUMBER OF PRINTS: {self.number_of_prints}
        '''

class Analiser:
    __k_empty_text = ''
    __k_spacing_text = ' '
    __k_line_breaker = '\n'
    
    def __init__(self, page, page_path, page_name) -> None:
        self.page = page
        self.page_path = page_path
        self.page_name = page_name

    def __count_number_of_imports(self) -> int:
        import_identifier = 'import '
        return self.page.count(import_identifier)

    def __count_number_of_class_declaration(self) -> int:
        class_identifier = 'class '
        return self.page.count(class_identifier)

    def __count_number_of_extensions_declared(self) -> int:
        extension_identifier = 'extension '
        return self.page.count(extension_identifier)

    def __count_number_of_lines(self) -> int:
        lines = self.page.split(self.__k_line_breaker)
        return len(lines)

    def __count_effective_number_of_code_lines(self) -> int:
        lines = self.page.replace(self.__k_spacing_text, self.__k_empty_text).split(self.__k_line_breaker)
        while(self.__k_empty_text in lines):
            lines.remove(self.__k_empty_text)
        return len(lines)

    def __count_number_of_methods(self) -> int:
        function_identifier = 'func '
        return self.page.count(function_identifier)

    def __count_number_of_forceUnwrap(self) -> int:
        force_unwrap_identifier = '! '
        return self.page.count(force_unwrap_identifier)

    def __count_number_of_comments(self) -> int:
        comment_identifier = '//'
        return self.page.count(comment_identifier)

    def __count_number_of_todo_comments(self) -> int:
        todo_comment_identifier = '//todo'
        dash_identifier = '-'
        return self.page.replace(self.__k_spacing_text, self.__k_empty_text).replace(dash_identifier, self.__k_empty_text).lower().count(todo_comment_identifier)

    def __count_number_of_fix_comments(self) -> int:
        fix_comment_identifier = '//fix'
        return self.page.replace(self.__k_spacing_text, self.__k_empty_text).lower().count(fix_comment_identifier)

    def __count_number_of_unowned_reference(self) -> int:
        unowned_identifier = '[unowned'
        return self.page.replace(self.__k_spacing_text, self.__k_empty_text).lower().count(unowned_identifier)

    def __count_number_of_variable_assinging(self) -> int:
        variable_identifier = 'var '
        return self.page.count(variable_identifier)

    def __count_number_of_constant_assinging(self) -> int:
        constant_identifier = 'let '
        return self.page.count(constant_identifier)

    def __count_number_of_prints(self) -> int:
        print_identifier = 'print('
        return self.page.count(print_identifier)

    def statistic(self) -> FileStatisticDTO:
        return FileStatisticDTO(
            path = self.page_path, 
            name = self.page_name, 
            number_of_imports = self.__count_number_of_imports(),
            number_of_class_namespaces = self.__count_number_of_class_declaration(),
            number_of_extensions = self.__count_number_of_extensions_declared(),
            number_of_lines = self.__count_number_of_lines(),
            number_of_effective_line_of_code = self.__count_effective_number_of_code_lines(),
            number_of_methods = self.__count_number_of_methods(),
            number_of_force_unwrap = self.__count_number_of_forceUnwrap(),
            number_of_comments = self.__count_number_of_comments(),
            number_of_todo_commnets = self.__count_number_of_todo_comments(),
            number_of_fix_commnets = self.__count_number_of_fix_comments(),
            number_of_unowned = self.__count_number_of_unowned_reference(),
            number_of_variable_declaration = self.__count_number_of_variable_assinging(),
            number_of_constant_declaration = self.__count_number_of_constant_assinging(),
            number_of_prints = self.__count_number_of_prints()
        )

# route example => /Users/prols/Arquivos/dev/github-repos/swift/health-tracker-app/health-tracker/App/FitFica/Source/Features/Scenes/Login/Model/
K_SWIFT_EXTENSION = '.swift'
READ_FILE_MODE = 'r'
route = input('Path: ')
initial_directory = "."
file_with_properties = []
for root, dirs, files in os.walk(route + initial_directory):
    for name in files:
        if name.endswith(K_SWIFT_EXTENSION):
            path = f'{root}/{name}'
            with open(path, READ_FILE_MODE) as file:
                page = file.read()
                analiser = Analiser(page, path, name)
                object = analiser.statistic()
                file_with_properties.append(object)


# IMPROMINDO
for file in file_with_properties:
    print(file)
            