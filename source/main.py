import os
from FileAnaliser import FileAnaliser
from FileStats import FileStats
from DirectoryStats import DirectoryStats

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
    print(DirectoryStats(route, file_stats))
    # print_stats(file_stats)
