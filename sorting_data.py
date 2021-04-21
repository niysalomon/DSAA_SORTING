Formated_data = []
other_data=[]


def Getting_data(file):
    try:
        with open(file, 'r') as Fil_name:
            for line in Fil_name:
                column = {}
                one_line = line.replace('\n', "")
                my_data = one_line.strip().split(' ')
                column['sequence'] = int(my_data[0])
                column['size'] = int(my_data[1])
                column['priority'] = my_data[2]
                if column['priority'] == 'HIGH':
                    column['priority'] = 2
                elif column['priority'] == 'MEDIUM':
                    column['priority'] = 1
                elif column['priority'] == 'LOW':
                    column['priority'] = 0
                Formated_data.append(column)
    except FileNotFoundError:
        pass
    return other_data


Final_load = Getting_data('items.txt')


def sorting_data(select, ordered):
    """Function to sort data"""
    if ordered == 'asc':
        after_sorting = sorted(Final_load, key=lambda el: el[select])
    else:
        after_sorting = sorted(Final_load, key=lambda el: el[select], reverse=True)
    return after_sorting


def get_final_file(data, sort_choice):
    """Function to create a file"""
    file = str(f'order_by_{sort_choice}.txt')
    try:
        with open(file, 'w') as get_final_data:
            final_file = ''
            for single_column in data:
                sequence = single_column['sequence']
                size = single_column['size']
                priority = single_column['priority']
                if priority == 2:
                    priority = 'HIGH'
                elif priority == 1:
                    priority = 'MEDIUM'
                elif priority == 0:
                    priority = 'LOW'
                final_file = str(f'{final_file}') + str(f'{sequence} {size} {priority}\n')
            get_final_data.write(final_file)
    except FileNotFoundError:
        pass
