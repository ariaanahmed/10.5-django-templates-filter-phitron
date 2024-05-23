from django.shortcuts import render
import datetime

def home(request):
    allMethods = {
        'author': 'William Shakespear',
        'age': 38,
        'char_length': 'This is my favorite Text',
        'add_val': 5,
        'add_slash': "'I'm Arian A'hmed'",
        'capitalize_first_letter': "this is me ariaan ahemd",
        'center_with_width': "Jay",
        'cut_the_space': "Hello Guys This Is Me Ariaan Ahmed",
        'dateObj': datetime.datetime.now(),
        'val_will_nothing': '',
        'dict_sort_val' : [
            {'name': 'zed', 'age': 19},
            {'name': 'amy', 'age': 22},
            {'name': 'joe', 'age': 31},
        ],
        'isItDivisibleByArgu': 45,
        'file_size_format' : 1024 * 1024,
        'return_first_item': ["apple", "orange", "banana"],
        'join_list_str': ["Ferrari", "Mercedes", "Volkswagon"],
        'return_last_item': ["apple", "orange", "banana"],
        'line_number' : 'one',
        'lower_case': "THIS IS GOING TO BE LOWERCASE",
        'making_list_str' : "Ariaan Ahmed",
        'making_list_int' : "01719475579",
        'random_val': ["arian", "raveen", "suhana", "asad", "revaan"],
        'slice_list': ["Jibon", "hridoy", "mominul", "jihad", "mahfuz"],
        'slugigy_text': "Suhana went to market yesterday",
        'time_fomat': datetime.datetime.now(),
        # 'blog_date': '',
        'title_case': "this is going to be the title case",
        'unordered_list_mthd': ['States', ['Kansas', ['Lawrence', 'Topeka'], 'Illinois']],
        'upper_case': "this is going to be the upper case",
        'words_count': "this is going to count the word available in the str"
    }
    return render(request, 'home.html', allMethods)