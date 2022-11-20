import os
from FileAnaliser import FileAnaliser
from FileStats import FileStats

class DerectoryStats:
    number_of_imports = 0
    number_of_classes = 0
    number_of_extension = 0
    number_of_lines = 0
    number_of_effective_line = 0
    number_of_methods = 0
    number_of_force_unwrap = 0
    number_of_comments = 0
    number_of_todo_commnets = 0
    number_of_fix_commnets = 0
    number_of_unowned = 0
    number_of_variables = 0
    number_of_constants = 0
    number_of_prints = 0

    def __init__(self, route, list_of_file_stats) -> None:
        self.route = route
        self.list_of_file_stats = list_of_file_stats
        self.calculate_all_stats_for_field()

    def calculate_all_stats_for_field(self):
        for file_stats in self.list_of_file_stats:
            self.number_of_imports += file_stats.number_of_imports
            self.number_of_classes += file_stats.number_of_class_namespaces
            self.number_of_extension += file_stats.number_of_extensions
            self.number_of_lines += file_stats.number_of_lines
            self.number_of_effective_line += file_stats.number_of_effective_line_of_code
            self.number_of_methods += file_stats.number_of_methods
            self.number_of_force_unwrap += file_stats.number_of_force_unwrap
            self.number_of_comments += file_stats.number_of_comments
            self.number_of_todo_commnets += file_stats.number_of_todo_commnets
            self.number_of_fix_commnets += file_stats.number_of_fix_commnets
            self.number_of_unowned += file_stats.number_of_unowned
            self.number_of_variables += file_stats.number_of_variable_declaration
            self.number_of_constants += file_stats.number_of_constant_declaration
            self.number_of_prints += file_stats.number_of_prints

    def __str__(self) -> str:
        route = self.route
        list_of_path = route.split('/')
        last_index = len(list_of_path) - 1
        director_name = list_of_path[last_index]
        header = f'* DIRECTOR: {director_name} *'
        separator = len(header) * '*'
        return f'''
        {header}
        {separator}
        - PATH: {route}
        - NUMBER OF IMPORTS: {self.number_of_imports}
        - NUMBER OF CLASSES: {self.number_of_classes}
        - NUMBER OF EXTENSIONS: {self.number_of_extension}
        - NUMBER OF LINES (LOC): {self.number_of_lines}
        - NUMBER OF EFFECTIVE LINES: {self.number_of_effective_line}
        - NUMBER OF METHODS: {self.number_of_methods}
        - NUMBER OF FORCE UNWRAP (!): {self.number_of_force_unwrap}
        - NUMBER OF COMMENTS (ALL TIPES): {self.number_of_comments}
        - NUMBER OF TO-DO COMMENTS: {self.number_of_todo_commnets}
        - NUMBER OF FIX COMMENTS: {self.number_of_fix_commnets}
        - NUMBER OF UNOWNED REFERENCES: {self.number_of_unowned}
        - NUMBER OF VARIABLES DECALRED (var): {self.number_of_variables}
        - NUMBER OF CONSTANTS DECALRED (let): {self.number_of_constants}
        - NUMBER OF PRINTS: {self.number_of_prints}
        '''

# route example => /Users/prols/Arquivos/dev/github-repos/swift/health-tracker-app/health-tracker/App/FitFica/Source/Features/Scenes/Login/Model/
def analise_all_font(route):
    K_SWIFT_EXTENSION = '.swift'
    READ_FILE_MODE = 'r'
    initial_directory = ""
    file_with_properties = []
    for root, dirs, files in os.walk(route + initial_directory):
        for name in files:
            if name.endswith(K_SWIFT_EXTENSION):
                path = f'{root}/{name}'
                with open(path, READ_FILE_MODE) as file:
                    page = file.read()
                    analiser = FileAnaliser(page, path, name)
                    object = analiser.statistic()
                    file_with_properties.append(object)
    return file_with_properties

def print_stats(file_stats: FileStats):
    for stats in file_stats:
        print(stats)


if __name__ == '__main__':
    # route = input('Path: ')
    route = '/Users/prols/Arquivos/dev/github-repos/essential-feed-case-study/EssentialFeed/EssentialFeed'
    file_stats = analise_all_font(route)
    print(DerectoryStats(route, file_stats))
    # print_stats(file_stats)
