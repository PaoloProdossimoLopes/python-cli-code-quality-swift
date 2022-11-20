class FileStats:
    def __init__(
        self, path, name, number_of_imports, 
        number_of_class_namespaces, number_of_extensions, 
        number_of_lines, number_of_effective_line_of_code,
        number_of_methods, number_of_public_methods, number_of_private_methods, 
        number_of_fileprivate_methods, number_of_force_unwrap,
        number_of_comments, number_of_todo_commnets, 
        number_of_fix_commnets, number_of_unowned,
        number_of_variable_declaration,
        number_of_constant_declaration,
        number_of_prints, number_of_structs, number_of_concretes
    ) -> None:

        self.path = path
        self.name = name
        self.number_of_imports = number_of_imports
        self.number_of_class_namespaces = number_of_class_namespaces
        self.number_of_extensions = number_of_extensions
        self.number_of_lines = number_of_lines
        self.number_of_effective_line_of_code = number_of_effective_line_of_code
        self.number_of_methods = number_of_methods
        self.number_of_public_methods = number_of_public_methods
        self.number_of_private_methods = number_of_private_methods
        self.number_of_fileprivate_methods = number_of_fileprivate_methods
        self.number_of_force_unwrap = number_of_force_unwrap
        self.number_of_comments = number_of_comments
        self.number_of_todo_commnets = number_of_todo_commnets
        self.number_of_fix_commnets = number_of_fix_commnets
        self.number_of_unowned = number_of_unowned
        self.number_of_variable_declaration = number_of_variable_declaration
        self.number_of_constant_declaration = number_of_constant_declaration
        self.number_of_prints = number_of_prints
        self.number_of_structs = number_of_structs
        self.number_of_concretes = number_of_concretes

    def __str__(self) -> str:
        header = f'* FILE: {self.name} *'
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
        - NUMBER OF PUBLIC METHODS: {self.number_of_public_methods}
        - NUMBER OF PRIVATE METHODS: {self.number_of_private_methods}
        - NUMBER OF FILEPRIVATE METHODS: {self.number_of_fileprivate_methods}
        - NUMBER OF FORCE UNWRAP (!): {self.number_of_force_unwrap}
        - NUMBER OF COMMENTS (ALL TIPES): {self.number_of_comments}
        - NUMBER OF TO-DO COMMENTS: {self.number_of_todo_commnets}
        - NUMBER OF FIX COMMENTS: {self.number_of_fix_commnets}
        - NUMBER OF UNOWNED REFERENCES: {self.number_of_unowned}
        - NUMBER OF VARIABLES DECALRED (var): {self.number_of_variable_declaration}
        - NUMBER OF CONSTANTS DECALRED (let): {self.number_of_constant_declaration}
        - NUMBER OF PRINTS: {self.number_of_prints}
        '''