#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

# import os
sys.path.append('gstore_api')
import conv_node_edge
import conv_table
from gstore_api.GstoreConnector import GstoreConnector
import template_search as ts
import json

def entity_search(str):
    # 长于四个字,认为是机构
    if len(str) > 4:
        sparql = 'select ?x ?y ?z\n{\n\t?x <http://cn.info/vocab/organization_ORGNAME> "' + str + '".\n\t?x ?y ?z.\n}'
    else:
        sparql = 'select ?x ?y ?z\n{\n\t?x <http://cn.info/vocab/naturalperson_PERSONNAME> "' + str + '".\n\t?x ?y ?z.\n}'
    # print(sparql)
    answer = query_result(sparql)
    # with open('search1_result.txt', 'r', encoding='utf-8') as f:
    #     answer = f.read()
    # os.remove(os.path.dirname(os.path.abspath(__file__))+'\\search1_result.txt')
    json_str = conv_node_edge.conv2graph(answer)
    # with open('search1_result.txt', 'w', encoding='utf-8') as f:
    #     f.write(json_str)
    return json_str


def query_result(sparql):
    gc = GstoreConnector('127.0.0.1', 3305)
    # 如果未提前加载数据库,则取消下行代码注释
    # gc.load('cninfo_db')

    # # sparql = '''select ?x ?y ?z
    # # {
    # #     ?x <http://cn.info/vocab/organization_ORGNAME> "南华生物医药股份有限公司".
    # #     ?x ?y ?z.
    # # }'''
    # sparql = '''select ?y ?z{
    #     <http://cn.info/securities/810> ?y ?z.
    # }'''
    # 因为最后一行是NUT字符,所以切片掉
    answer = (gc.query(sparql))
    # print(answer)
    return answer
    # print(answer)
    # with open('search1_result.txt', 'w', encoding='utf-8') as f:
    #     f.write(answer)


def plus_search(data_id):
    sparql = 'select ?y ?z\n{\n\t<' + data_id + '> ?y  ?z.\n}'
    answer = query_result(sparql)
    json_plus = conv_node_edge.plus2graph(answer, data_id)
    return json_plus

# answer = entity_search("南华生物医药股份有限公司")
# with open('results_end.txt', 'w', encoding='utf-8') as f:
#     f.write(answer)
def template_search(str_to_solve):
    sparql=''

    if str_to_solve.find('证券号') >= 0:
        sparql = ts.sparqlquery4(str_to_solve)
    elif str_to_solve.find('处罚情况') >= 0:
        sparql = ts.sparqlquery2(str_to_solve)
    elif str_to_solve.find('法律纠纷') >= 0:
        sparql = ts.sparqlquery3(str_to_solve)
    elif str_to_solve.find('管理人员') >= 0:
        sparql = ts.sparqlquery5(str_to_solve)
    elif str_to_solve.find('股本变动') >= 0:
        sparql = ts.sparqlquery1(str_to_solve)
    print(sparql)
    answer=query_result(sparql)
    # print(answer)
    # print(answer)
    answer_list=conv_node_edge.to_triples_list(answer)
    json_list=conv_table.conv2table(answer_list)
    json_list=json.dumps(json_list)
    return json_list

# print(template_search('公司的证券号是多少？'))
# template_search('南华生物医药股份有限公司的证券号是多少')