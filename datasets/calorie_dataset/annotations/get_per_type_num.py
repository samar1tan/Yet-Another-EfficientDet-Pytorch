import json
import sys


def get_annotations_category_id_summary_dict(json_dict):
    category_id_summary = {}
    for annotation in json_dict['annotations']:
        category_id = annotation['category_id']
        if category_id not in category_id_summary.keys():
            category_id_summary[category_id] = 0
        category_id_summary[category_id] += 1
    return category_id_summary


if __name__ == '__main__':
    category_id2name = ['apple', 'banana', 'bean', 'beer', 'bread', 'broccoli', 'bun', 'cheese', 'coffee', 'cola',
                        'doughnut', 'egg', 'fired_dough_twist', 'grape', 'jerky', 'juice', 'lemon', 'litchi', 'mango', 'milk',
                        'mooncake', 'nut', 'onion', 'orange', 'pasta', 'peach', 'pear', 'pepper', 'plum', 'qiwi', 'sachima',
                        'sauce', 'tomato', 'waffle', 'watermelon', 'wine', 'coin']

    filename = sys.argv[1]
    print(filename)
    with open(filename, 'r') as f:
        json_dict = json.load(f)
    category_id_summary = get_annotations_category_id_summary_dict(json_dict)
    num_all = 0
    for i_category_id_name in range(len(category_id2name)):
        print('{0}: {1}'.format(category_id2name[i_category_id_name], category_id_summary[i_category_id_name + 1]))
        num_all += category_id_summary[i_category_id_name + 1]
    print(num_all)
