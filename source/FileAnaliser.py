from FileStats import FileStats

class FileAnaliser:
    __k_empty_text = ''
    __k_spacing_text = ' '
    __k_line_breaker = '\n'
    
    def __init__(self, page, page_path, page_name) -> None:
        self.page = page
        self.page_path = page_path
        self.page_name = page_name

    def count_number_of_imports(self) -> int:
        import_identifier = 'import '
        page = self.page
        return page.count(import_identifier)

    def count_number_of_class_declaration(self) -> int:
        class_identifier = 'class '
        page = self.page
        return page.count(class_identifier)

    def count_number_of_extensions_declared(self) -> int:
        extension_identifier = 'extension '
        page = self.page
        return page.count(extension_identifier)

    def count_number_of_lines(self) -> int:
        page = self.page
        lines = page.split(self.__k_line_breaker)
        return len(lines)

    def count_effective_number_of_code_lines(self) -> int:
        page = self.page
        page = page.replace(self.__k_spacing_text, self.__k_empty_text)
        lines = page.split(self.__k_line_breaker)
        while(self.__k_empty_text in lines):
            lines.remove(self.__k_empty_text)
        return len(lines)

    def count_number_of_methods(self) -> int:
        function_identifier = 'func '
        page = self.page
        return page.count(function_identifier)

    def count_number_of_public_methods(self) -> int:
        function_identifier = 'public func '
        page = self.page
        return page.count(function_identifier)

    def count_number_of_private_methods(self) -> int:
        function_identifier = 'private func '
        page = self.page
        return page.count(function_identifier)

    def count_number_of_fileprivate_methdos(self) -> int:
        function_identifier = 'fileprivate func '
        page = self.page
        return page.count(function_identifier)

    def count_number_of_forceUnwrap(self) -> int:
        force_unwrap_identifier = '! '
        page = self.page
        return page.count(force_unwrap_identifier)

    def count_number_of_comments(self) -> int:
        comment_identifier = '//'
        page = self.page
        return page.count(comment_identifier)

    def count_number_of_todo_comments(self) -> int:
        todo_comment_identifier = '//todo'
        dash_identifier = '-'
        page = self.page
        page = page.replace(self.__k_spacing_text, self.__k_empty_text)
        page = page.replace(dash_identifier, self.__k_empty_text)
        page = page.lower()
        return page.count(todo_comment_identifier)

    def count_number_of_fix_comments(self) -> int:
        fix_comment_identifier = '//fix'
        page = self.page
        page = page.replace(self.__k_spacing_text, self.__k_empty_text)
        page = page.lower()
        return page.count(fix_comment_identifier)

    def count_number_of_unowned_reference(self) -> int:
        unowned_identifier = '[unowned'
        page = self.page
        page = page.replace(self.__k_spacing_text, self.__k_empty_text)
        page = page.lower()
        return page.count(unowned_identifier)

    def count_number_of_variable_assinging(self) -> int:
        variable_identifier = 'var '
        page = self.page
        return page.count(variable_identifier)

    def count_number_of_constant_assinging(self) -> int:
        constant_identifier = 'let '
        page = self.page
        return page.count(constant_identifier)

    def count_number_of_prints(self) -> int:
        print_identifier = 'print('
        page = self.page
        return page.count(print_identifier)
    
    def count_number_of_structs(self) -> int:
        struct_identifier = 'struct '
        page = self.page
        return page.count(struct_identifier)

    def count_number_of_concrete(self) -> int:
        n_structs = self.count_number_of_structs()
        n_classes = self.count_number_of_class_declaration()
        return n_structs + n_classes

    def statistic(self) -> FileStats:
        return FileStats(
            path = self.page_path, 
            name = self.page_name, 
            number_of_imports = self.count_number_of_imports(),
            number_of_class_namespaces = self.count_number_of_class_declaration(),
            number_of_extensions = self.count_number_of_extensions_declared(),
            number_of_lines = self.count_number_of_lines(),
            number_of_effective_line_of_code = self.count_effective_number_of_code_lines(),
            number_of_methods = self.count_number_of_methods(),
            number_of_public_methods = self.count_number_of_public_methods(),
            number_of_private_methods = self.count_number_of_private_methods(),
            number_of_fileprivate_methods = self.count_number_of_fileprivate_methdos(),
            number_of_force_unwrap = self.count_number_of_forceUnwrap(),
            number_of_comments = self.count_number_of_comments(),
            number_of_todo_commnets = self.count_number_of_todo_comments(),
            number_of_fix_commnets = self.count_number_of_fix_comments(),
            number_of_unowned = self.count_number_of_unowned_reference(),
            number_of_variable_declaration = self.count_number_of_variable_assinging(),
            number_of_constant_declaration = self.count_number_of_constant_assinging(),
            number_of_prints = self.count_number_of_prints(),
            number_of_structs = self.count_number_of_structs(),
            number_of_concretes = self.count_number_of_concrete()
        )