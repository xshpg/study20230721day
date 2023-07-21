

def get_create_time_format(datas):
    datas_list = []
    for item in datas:
        day_str = item['create_time'].split('T')[0]
        hh_str =item['create_time'].split('T')[1].split('+')[0].split('.')[0]
        item['create_time'] = day_str + ' ' + hh_str
        datas_list.append(item)
    return datas_list


def get_detail_format(datas):
    day_str = datas['create_time'] .split('T')[0]
    hh_str = datas['create_time'].split('T')[1].split('+')[0].split('.')[0]
    datas['create_time'] = day_str + ' ' + hh_str
    return datas


if __name__ == '__main__':
    rest = get_detail_format()
    print(rest)