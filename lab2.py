import statistics
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    number = input().split(",")
    return [float(x) for x in number]


def calc_average(list):
    total = 0
    for number in list:
        total = total + number
    average = total / len(list)
    return average


def find_min_max(lists):
    min_num = min(lists)
    max_num = max(lists)
    return min_num, max_num




def calc_median_temperature(middle):
    mid = statistics.median(middle)
    return mid


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(calc_average(num_list))
    print(find_min_max(num_list))
    print(calc_median_temperature(num_list))


if __name__ == "__main__":
    main()





"""
#def calc_median_temperature():

def sort_temperature():
"""
