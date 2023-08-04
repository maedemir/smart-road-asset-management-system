# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import os
import splitfolders


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    camera = 0
    donation_box = 0
    flag = 0
    footbridge = 0
    galvanized_trash_bin = 0
    powerbox = 0
    street_name_sign = 0
    telephone = 0
    traffic_cylinder = 0
    traffic_light = 0
    # assign directory
    directory = '/Users/maedehmirzazadeh/Desktop/dataset-final/train/labels'

    # iterate over files in
    # that directory
    print('number of train images is: ',len(os.listdir(directory)))
    print('number of instances of each class:')
    print()

    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            file = open(f, 'r')
            lines = file.readlines()
            for i in lines:
                if i[0] == '0':
                    camera = camera+1
                elif i[0] == '1':
                    donation_box = donation_box+1
                elif i[0] == '2':
                    flag = flag + 1
                elif i[0] == '3':
                    footbridge = footbridge + 1
                elif i[0] == '4':
                    galvanized_trash_bin = galvanized_trash_bin + 1
                elif i[0] == '5':
                    powerbox = powerbox + 1
                elif i[0] == '9':
                    street_name_sign = street_name_sign + 1
                elif i[0] == '6':
                    telephone = telephone + 1
                elif i[0] == '7':
                    traffic_cylinder = traffic_cylinder + 1
                elif i[0] == '8':
                    traffic_light = traffic_light + 1

    print("camera: ", camera)
    print("donation_box: ", donation_box)
    print("flag: ", flag)
    print("footbridge: ", footbridge)
    print("galvanized_trash_bin: ", galvanized_trash_bin)
    print("powerbox: ", powerbox)
    print("street_name_sign: ", street_name_sign)
    print("telephone: ", telephone)
    print("traffic_cylinder: ", traffic_cylinder)
    print("traffic_light: ", traffic_light)

    # Split with a ratio.
    # To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
    # splitfolders.ratio("/Users/maedehmirzazadeh/Desktop/dataset", output="/Users/maedehmirzazadeh/Desktop/dataset-final",
    #                    seed=497, ratio=(.8, .2), group_prefix=None, move=False)  # default values










