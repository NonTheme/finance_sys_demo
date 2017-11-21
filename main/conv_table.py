from source import translate_dict as td

name_list = ['naturalperson', 'organization', 'securities', 'top10circshareholder', 'top10shareholder']
name1_list = ['naturalperson', 'organization', 'securities']
name2_list = ['top10circshareholder', 'top10shareholder']
event_list = ['assets_frozen', 'assets_restructure', 'company_litigation', 'company_penalty', 'company_arbitration',
              'manager_serve', 'profit_prediction', 'share_capital_change', 'summary_profit_predict']
event_dict = {
    "assets_frozen": "资产冻结",
    "assets_restructure": "资产重组",
    "company_litigation": "公司诉讼",
    "company_penalty": "公司处罚",
    "company_arbitration": "公司仲裁",
    "manager_serve": "管理人员任职",
    "profit_prediction": "盈利预测",
    "share_capital_change": "股本变动",
    "summary_profit_predict": "盈利预测汇总"
}


def conv2table(answer_list):
    test_dict = answer_list[0]
    test_length_list = list(test_dict.keys())
    trans_key_list = list(td.trans_dict.keys())
    json_list = []
    if len(test_length_list) == 3:
        for i in answer_list:
            record_dict = {}
            x_value_splitted_list = i['x']['value'].split('/')
            if x_value_splitted_list[3] in name1_list:
                record_dict['x'] = x_value_splitted_list[5]
            elif x_value_splitted_list[3] in name2_list:
                record_dict['x'] = x_value_splitted_list[6]
            elif x_value_splitted_list[3] in event_list:
                record_dict['x'] = event_dict[x_value_splitted_list[3]] + x_value_splitted_list[4]
            else:
                record_dict['x'] = i['x']['value']
            if i['z']['type'] == 'uri':
                z_value_splitted_list = i['z']['value'].split('/')
                if z_value_splitted_list[3] in name1_list:
                    record_dict['z'] = z_value_splitted_list[5]
                elif z_value_splitted_list[3] in name2_list:
                    record_dict['z'] = z_value_splitted_list[6]
                elif z_value_splitted_list[3] in event_list:
                    record_dict['z'] = event_dict[z_value_splitted_list[3]] + z_value_splitted_list[4]
                else:
                    record_dict['z'] = i['z']['value']
            else:
                record_dict['z'] = i['z']['value']
            eng_desc = i['y']['value']
            # 判断英文描述是否在key中.
            if eng_desc in trans_key_list:
                record_dict['value'] = td.trans_dict[eng_desc]
            else:
                record_dict['value'] = i['y']['value'].split('/')[4]
            json_list.append(record_dict)
    if len(test_length_list) == 2:
        for i in answer_list:
            record_dict = {}
            if i['z']['type'] == 'uri':
                z_value_splitted_list = i['z']['value'].split('/')
                if z_value_splitted_list[3] in name1_list:
                    record_dict['z'] = z_value_splitted_list[5]
                elif z_value_splitted_list[3] in name2_list:
                    record_dict['z'] = z_value_splitted_list[6]
                elif z_value_splitted_list[3] in event_list:
                    record_dict['z'] = event_dict[z_value_splitted_list[3]] + z_value_splitted_list[4]
                else:
                    record_dict['z'] = i['z']['value']
            else:
                record_dict['z'] = i['z']['value']
            eng_desc = i['y']['value']
            # 判断英文描述是否在key中.
            if eng_desc in trans_key_list:
                record_dict['value'] = td.trans_dict[eng_desc]
            else:
                record_dict['value'] = i['y']['value'].split('/')[4]
            json_list.append(record_dict)
    if len(test_length_list) == 1:
        for i in answer_list:
            record_dict = {}
            if i['z']['type'] == 'uri':
                z_value_splitted_list = i['z']['value'].split('/')
                if z_value_splitted_list[3] in name1_list:
                    record_dict['z'] = z_value_splitted_list[5]
                elif z_value_splitted_list[3] in name2_list:
                    record_dict['z'] = z_value_splitted_list[6]
                elif z_value_splitted_list[3] in event_list:
                    record_dict['z'] = event_dict[z_value_splitted_list[3]] + z_value_splitted_list[4]
                else:
                    record_dict['z'] = i['z']['value']
            else:
                record_dict['z'] = i['z']['value']
            json_list.append(record_dict)
    return json_list
