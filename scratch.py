# # import json
# #
# # SOLR_QUERY = 'Select {cols} from {table} where solr_query=\'{solr_json}\'' \
# #             ' Limit {limit}'
# # solr_json={"q": "*:*","fq":"(client_name:{client_name})","fq":"(status:{status})"}
# # print(solr_json.fq)
# # client_name = "TAINGUYE-RN3R5"
# # status = "Failure"
# #
# # # t = solr_json.format(client_name=client_name, status=status)
# # # print(t)
# # QUERY_SN='select * from mfgsecurity.secure_events where solr_query = {solr_json};'
# #
# #
# # query = QUERY_SN
# #
# # print(query)
# # #t = query.format(client_name=client_name, status=status)
# # print(query)
#
# test_data = [{"[json]":
#                   '{'
#                   '"cas_timestamp": """",'
#                   '"client_name": "TAINGUYE-RN3R5",'
#                   '"client_version": "ATOM_5.0.6",'
#                   '"environment": "E5",'
#                   '"event_log": """",'
#                   '"event_time": "2019-11-08 23:26:32.000Z",'
#                   '"function": "get",'
#                   '"identity": "",'
#                   '"level": "csaregional",'
#                   '"partner_transaction_id": """",'
#                   '"process_time": "0.0",'
#                   '"product_id": "CP-WL-730-C",'
#                   '"request": "",'
#                   '"request_id": "6d7c25fe9505438c879d4bdff80554ab",'
#                   '"response_id": "",'
#                   '"response_size": "1062",'
#                   '"serial_number": "SN0000044",'
#                   '"server_name": "sngcsmstgapp1",'
#                   '"server_version": "Apollo",'
#                   '"service": "virtual_parts",'
#                   '"site_code": "rtp",'
#                   '"solr_query": """",'
#                   '"source": """",'
#                   '"status": "Success",'
#                   '"status_code": "0",'
#                   '"status_message": "SUCCESS",'
#                   '"transaction_id": "4ccfbd1e-b83c-4b2d-9f05-96392529547a",'
#                   '"tsd_timestamp": """",'
#                   '"type": "service",'
#                   '"url": "/apollo/cesiumsvcs/components/virtual_parts/get",'
#                   '"user_company": """",'
#                   '"user_name": "ODMUser"'
#                   '}'}]
#
# expected_output = [
#                 '{'
#                   '"cas_timestamp": """",'
#                   '"client_name": "TAINGUYE-RN3R5",'
#                   '"client_version": "ATOM_5.0.6",'
#                   '"environment": "E5",'
#                   '"event_log": """",'
#                   '"event_time": "2019-11-08 23:26:32.000Z",'
#                   '"function": "get",'
#                   '"identity": "",'
#                   '"level": "csaregional",'
#                   '"partner_transaction_id": """",'
#                   '"process_time": "0.0",'
#                   '"product_id": "CP-WL-730-C",'
#                   '"request": "",'
#                   '"request_id": "6d7c25fe9505438c879d4bdff80554ab",'
#                   '"response_id": "",'
#                   '"response_size": "1062",'
#                   '"serial_number": "SN0000044",'
#                   '"server_name": "sngcsmstgapp1",'
#                   '"server_version": "Apollo",'
#                   '"service": "virtual_parts",'
#                   '"site_code": "rtp",'
#                   '"solr_query": """",'
#                   '"source": """",'
#                   '"status": "Success",'
#                   '"status_code": "0",'
#                   '"status_message": "SUCCESS",'
#                   '"transaction_id": "4ccfbd1e-b83c-4b2d-9f05-96392529547a",'
#                   '"tsd_timestamp": """",'
#                   '"type": "service",'
#                   '"url": "/apollo/cesiumsvcs/components/virtual_parts/get",'
#                   '"user_company": """",'
#                   '"user_name": "ODMUser"'
#                   '}'
# ]
#
# print(test_data[0]['[json]'])
# print(str(expected_output[0]))
#
# assert test_data[0]['[json]']==str(expected_output[0])



# dic={"q": "*:*","fq":"(client_name:'')","fq":"(status:'')"}
# print(dic['fq'])

#z='select * from mfgsecurity.secure_events where solr_query = \'{\"q\": \"*:*\",\"fq\":\"(client_name:{})\",\"fq\":\"(status:{})\"}\';'
# z='select * from mfgsecurity.secure_events where solr_query = ""'
# z = '''
#         Select *  from mfgsecurity.secure_events
#         where  solr_query='{{"q": "*:*",  "fq":"uuttype:({x})"}}' limit 300;
#         '''

# x="TAINGUYE - RN3R5"
# z=z.format( x = x)

# print(z)

# y="\'Failure\'"
# print(z.format(x,y))
import math
import os
#print(os.environ)

# import pandas as pd
# import json
# import lxml.etree as et
# import xlrd
# import dicttoxml
# xls = pd.ExcelFile("prasad.xlsx")
# df = xls.parse(xls.sheet_names[0], skiprows=0, index_col=None, na_values=['None'])
# data_dict = df.to_dict()
# #{'Asset': {0: 'edfe', 1: 'dsds', 2: nan, 3: nan, 4: nan, 5: 'hvhvhvh'}, 'Location_Name': {0: 'sds', 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Parent': {0: nan, 1: 'sds', 2: nan, 3: nan, 4: nan, 5: nan}, 'Description': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Change_Date': {0: nan, 1: nan, 2: nan, 3: 'jyf', 4: nan, 5: nan}, 'Change_By': {0: nan, 1: nan, 2: 'jhh', 3: nan, 4: nan, 5: nan}, 'Status': {0: 'Active', 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Asset_Tag': {0: nan, 1: 'jhj', 2: nan, 3: nan, 4: nan, 5: nan}, 'Assigned_User': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Assigned_User_Name': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'BU_Name': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'SO ': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'SO_Line': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'SO_Date': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Comments': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Company_Code': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Department_Name': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Department ': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Financial_Owner_Name': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Financial_Owner_Number': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Subledger_Active': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Functional_Name': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Functional_Unit': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Manufacturer': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Metro': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Model_Mfg_Part_Number': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'PO': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'PO_Date': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'PO Line': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'PR': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'PR_Creator_Name': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'PR_Creator_Number': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'PR_Date': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Record_Creation_Date': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Subledger_Relevant_RFID_Tag_Required': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'GL_Account': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Book_Type': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Requestor_Name': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Requestor_Number': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Serial ': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Source': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Created_By': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Last_Seen_Date': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Asset_Update_Source_Reference': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Operation': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Read_Source': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Exception': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Exception_Category': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Exception_Category_Description': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Exception_Sub_Category': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Exception_Sub_Category_Description': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Exception_Comments': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Host_Name': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Last_Bar_Code_Scan_Date': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Last_ Bar_Code_Scan_By': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Last_Bar_Code_Scan_Location': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'PO_Asset_Identifier': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'SO_Asset_Identifier': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Ship_To_Person': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Revenue_Generating_Model': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Cisco_Premise': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Program_Name': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Program_Other': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Deal_ID': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Address': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'City': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'State_Province': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'ZIP_Postal Code': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}, 'Country': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan}}
# odict={}
# print(data_dict)
# i=0
# while i<=5:
#     temp={}
#     for x in data_dict:
#         print(data_dict[x][i])
#         temp[x]=data_dict[x][i]
#     odict[str(i)]=temp
#     i+=1
# print(dicttoxml.dicttoxml(odict))
from numpy.ma import floor, ceil
import math
# arr = [2, 6, 7, 5, 8]
# pre = [0, 0, 0, 0, 0]
# pre[0] = arr[0]
# n=5
# c=0
# if ((ceil(math.log(pre[0], 2)) == floor(math.log(pre[0], 2))) and pre[0] != 0):
#     c += 1
# for i in range(1, n):
#
#     pre[i] = pre[i - 1] ^ arr[i]
#     if ((ceil(math.log(pre[i], 2)) == floor(math.log(pre[i], 2))) and pre[i] != 0):
#         c += 1
#
# for i in range(n):
#
#     for j in range(i,n):
#
#         pre[j] = pre[j] ^ arr[i]
#         if ((ceil(math.log(pre[i], 2)) == floor(math.log(pre[i], 2))) and pre[i] != 0):
#             c += 1
#
# print(c)


import pandas as pd
data1= [
        {
            "client_name": "BDFEEB79-9746-4A83-A0D5-AABC95C6F7E5",
            "identity": "4B36601A-FFB5-48A8-ADE4-A419C2B2B376",
            "request_id": "E7D13ED2-679D-46EF-B204-88C42E1436D2",
            "server_version": "5840350C-3551-404F-A3BF-E5ACF47AA7AB",
            "service": "5F25A690-B649-4E2A-B3FF-5E143AFDFBB7",
            "site_code": "B9484639-82E2-4C7C-80B7-FA6C76A0F218",
            "status": "BFD4BA0E-3D67-47D6-B460-1D45A9736FEE",
            "status_code": 0,
            "status_message": "84A5EB1C-8D9A-4FDC-805F-9EBB44AC61EC",
            "user_name": "F03A08F8-2917-4BA9-BE48-71F3B44DFE27"
        },
        {
            "client_name": "DBB42AE6-D7A6-47BA-B5DB-73BCD1DA8BEE",
            "identity": "A31ABA5B-7420-42CB-B1EC-1C51EAEE117F",
            "request_id": "9807BABC-6BC4-41BB-AA03-74BEFB4E667E",
            "server_version": "E473C2A2-C484-4BDC-9DEB-B049D64A24F4",
            "service": "472D6392-1B8C-4398-9242-301A705E28C0",
            "site_code": "19815D61-BBDA-43D3-988B-F416CD609B97",
            "status": "46BF8AEC-C2E9-4699-8ACA-755437585525",
            "status_code": 0,
            "status_message": "ED7CBCD2-0AF2-4A2F-BB5B-B2C4AE1382A5",
            "user_name": "6B51915C-CDCA-4C5C-B46B-F14FE44E02E8"
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:0050569496F4",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "sjc12yubi1",
            "identity": "ATOM Virtual:005d73efc85a",
            "request_id": "8f4d3f66ca1748c49a49bd1f0df6834d",
            "server_version": "Apollo_CSA_Dev1-94-3",
            "service": "virtual_parts",
            "site_code": "cisco",
            "status": "Failure",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "rtonukun"
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:0050569496F4",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "5509DDF3-9665-4A42-B299-EE6E24920A97",
            "identity": "6378FAED-5E9A-4638-89AB-4200975BBF46",
            "request_id": "08D1ADE5-F2BF-498B-8320-7F31AA5B206D",
            "server_version": "CB1DB1C0-E4FA-46F3-A097-EA6AA2D04F01",
            "service": "E295DDB9-154A-45F8-BC7D-5FEC5C8FBC68",
            "site_code": "BF885251-3B91-43AB-B503-4FBAE7AF1FB1",
            "status": "46FC7230-264C-4337-AD5D-E3203D7AC14E",
            "status_code": 0,
            "status_message": "A1086ED0-488F-4790-942C-895811D90665",
            "user_name": "0309A6EE-8037-4E48-A132-B0B34BD952A9"
        },
        {
            "client_name": "DC0BC571-9D97-430E-AF96-79E15BA77039",
            "identity": "CAE54784-D295-4445-9802-8EBCDEB406AC",
            "request_id": "1BB9CE57-88B0-47F3-8DA6-7C4C82D3C784",
            "server_version": "DDBCECEB-7403-427A-B8FD-9FAB310A5888",
            "service": "727D6193-FC79-43AE-B42A-1FFDA882D6CF",
            "site_code": "0F3848A6-E46F-47FE-B7D8-E147C0D49860",
            "status": "CA794D96-7A78-4170-8623-9D175D44B594",
            "status_code": 0,
            "status_message": "D064984E-1F09-4AA0-BAB5-A953D7B9071D",
            "user_name": "FACBAC62-0310-4D9D-8333-482BDD9F1D34"
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:00505694E10C",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "SBOJANAP-QAC65",
            "identity": "ATOM:9596801",
            "request_id": "f744f9a9c3f24d978756367d1abb64e7",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "virtual_parts",
            "site_code": "sjd",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "tempuser"
        },
        {
            "client_name": "sjc12yubi1",
            "identity": "ATOM Virtual:005d73efc85a",
            "request_id": "270fe4c21d9841858d966165caf07838",
            "server_version": "Apollo_CSA_Dev1-94-3",
            "service": "virtual_parts",
            "site_code": "cisco",
            "status": "Failure",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "rtonukun"
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:0050569496F4",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:00505694E10C",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "SBOJANAP-QAC65",
            "identity": "ATOM:9596686",
            "request_id": "f2bb161b8003469b9590dea8c49248a4",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "virtual_parts",
            "site_code": "cisco",
            "status": "Failure",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "tempuser"
        },
        {
            "client_name": "sjc12yubi1",
            "identity": "ATOM Virtual:005d73efc85a",
            "request_id": "d75512a5b5e3431d8321b037a1a1a709",
            "server_version": "Apollo_CSA_Dev1-94-3",
            "service": "virtual_parts",
            "site_code": "cisco",
            "status": "Failure",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "rtonukun"
        },
        {
            "client_name": "RTONUKUN-JAG2X",
            "identity": "ATOM Virtual:005d73efc85a",
            "request_id": "4e013d63141146b7937e170ab81e7593",
            "server_version": "Apollo_CSA_Dev1-94-3",
            "service": "virtual_parts",
            "site_code": "cisco",
            "status": "Failure",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "ehampshi"
        },
        {
            "client_name": "sjc12yubi1",
            "identity": "ATOM Virtual:005d73efc85a",
            "request_id": "60e2b1d8216a4cd0ac99832e25b89df2",
            "server_version": "Apollo_CSA_Dev1-94-3",
            "service": "virtual_parts",
            "site_code": "cisco",
            "status": "Failure",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "rtonukun"
        },
        {
            "client_name": "sjc12yubi1",
            "identity": "ATOM Virtual:005d73efc85a",
            "request_id": "84e076981e5e453db99a9aac1eb30339",
            "server_version": "Apollo_CSA_Dev1-94-3",
            "service": "virtual_parts",
            "site_code": "cisco",
            "status": "Failure",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "rtonukun"
        },
        {
            "client_name": "sjc12yubi1",
            "identity": "ATOM Virtual:005d73efc85a",
            "request_id": "125e92ff68ae47bc8b0d3e0154795105",
            "server_version": "Apollo_CSA_Dev1-94-3",
            "service": "virtual_parts",
            "site_code": "sjd",
            "status": "Failure",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "pid"
        },
        {
            "client_name": "482467CB-9FAA-4643-A0EB-293ABEC4E3C9",
            "identity": "7CE2E50B-C24F-4D60-9319-CC92C39BDE43",
            "request_id": "F3AE3580-27FD-4205-B574-BC656664F1C4",
            "server_version": "632D797C-FD09-4C9A-A666-767021A4D253",
            "service": "712EB66A-306E-4E32-88C4-3F5E9A0A6ADF",
            "site_code": "E16A34D7-71C2-4F4B-AAC5-FF4639081D8C",
            "status": "30B32426-9B13-406D-89E6-D4C9CDFFE5F6",
            "status_code": 0,
            "status_message": "797EE771-9B57-4986-BB69-9F79F2B30CE5",
            "user_name": "BD14498D-F34E-47E4-B8B0-A86745BFCF6F"
        },
        {
            "client_name": "7DF574F6-B9B4-4594-AA6B-6D906D5A45C7",
            "identity": "21FF9F3B-EBCB-4C26-BF42-0986EC12D151",
            "request_id": "0A1934E9-174C-404E-B99C-98895F5ECD61",
            "server_version": "852D5D0C-60B5-4B15-B37F-73E4FF73C23E",
            "service": "3863910D-E513-403D-8332-2450C7D5D71A",
            "site_code": "1F316868-9FBF-48E3-A0AB-D218536C6813",
            "status": "A9816E26-9E21-4E2A-836D-1EAA9A7E8B60",
            "status_code": 0,
            "status_message": "D8FC70C9-41D4-4DEE-B401-AA1114970526",
            "user_name": "B3A97AF6-127C-4021-B61E-44C4B6025473"
        },
        {
            "client_name": "78F86EDC-B1E4-4568-A886-EAEB5240F519",
            "identity": "91935C6B-6904-47A2-8D44-60FBAF1FDF63",
            "request_id": "D3E57D1A-E018-42CF-A1DA-5F7283303D6E",
            "server_version": "CE1D72A1-B324-473E-8BFF-BCF83BD54D20",
            "service": "B73584FD-A5F6-4957-B483-374385BE0C2E",
            "site_code": "57954603-9CB3-4430-9A73-FD136513045D",
            "status": "68A3BA9A-EC6C-4C13-9DBA-8B2FB1E6C118",
            "status_code": 0,
            "status_message": "0389B56D-6B02-4DD0-B12A-CE7A1438A392",
            "user_name": "0C272BF8-46E2-4E6B-BE65-1F591EB2E483"
        },
        {
            "client_name": "sjc12yubi1",
            "identity": "ATOM Virtual:005d73efc85a",
            "request_id": "fff7e404ea5b411db356341e8cdef5cd",
            "server_version": "Apollo_CSA_Dev1-94-3",
            "service": "virtual_parts",
            "site_code": "cisco",
            "status": "Failure",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "rtonukun"
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:0050569496F4",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:00505694E10C",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:0050569496F4",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:00505694E10C",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "7D262919-E38C-461D-8BC5-0AA756559BDE",
            "identity": "DE57A0F6-79BA-4085-9064-A50396D275A0",
            "request_id": "5B2A4C0A-CCF3-40FE-A943-EEA03EBBC122",
            "server_version": "2928C73F-DAAA-4E22-A415-6D180F5990B0",
            "service": "180F7509-8480-4169-855B-AB7585AC9919",
            "site_code": "2B6FEF84-F477-4154-9018-1901AD7B7FDA",
            "status": "7664CC4C-DBA0-4163-817F-4F52B9E6415B",
            "status_code": 0,
            "status_message": "C7D6ACF9-3296-4508-8830-02410FDD5B3C",
            "user_name": "A6EB8F30-DFB9-4BA8-A917-80DBDCB7E5E0"
        },
        {
            "client_name": "sjc12yubi1",
            "identity": "ATOM Virtual:005d73efc85a",
            "request_id": "70a527d3d8044d93b1cc6cf3adcd6b36",
            "server_version": "Apollo_CSA_Dev1-94-3",
            "service": "virtual_parts",
            "site_code": "cisco",
            "status": "Failure",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "rtonukun"
        },
        {
            "client_name": "sjc12yubi1",
            "identity": "ATOM Virtual:005d73efc85a",
            "request_id": "3cc2fcb168fc493088aef2b355606fb4",
            "server_version": "Apollo_CSA_Dev1-94-3",
            "service": "virtual_parts",
            "site_code": "Cisco",
            "status": "Failure",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "rtonukun"
        },
        {
            "client_name": "sjc12yubi1",
            "identity": "ATOM Virtual:005d73efc85a",
            "request_id": "d3efe7e104e6480f8908b09fe0e3e782",
            "server_version": "Apollo_CSA_Dev1-94-3",
            "service": "virtual_parts",
            "site_code": "cisco",
            "status": "Failure",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "rtonukun"
        },
        {
            "client_name": "17876E23-02CD-4594-8730-8DB46E357ACF",
            "identity": "F93691D3-FB11-49A6-A81F-95BF0FBC17C1",
            "request_id": "803E1A79-FCFF-47DD-9E9B-E6EDBBDF4FAD",
            "server_version": "A66E6F1C-D9E7-4681-A567-F806E2764ED7",
            "service": "3902BEB3-401B-491E-9054-D7B09ED15210",
            "site_code": "4ECBBA38-EFF0-48C3-B518-AFDB850EEA8C",
            "status": "55059256-49EA-479D-8BDB-3F5A784C0BB5",
            "status_code": 0,
            "status_message": "36EB811D-88AA-4C0E-8F38-9881913DABD0",
            "user_name": "4B2AA96D-BD0B-4851-B857-5028E588A3A7"
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:0050569496F4",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "sjc12yubi1",
            "identity": "ATOM Virtual:005d73efc85a",
            "request_id": "d82962fdef7f463bafb6a408753f9058",
            "server_version": "Apollo_CSA_Dev1-94-3",
            "service": "virtual_parts",
            "site_code": "cisco",
            "status": "Failure",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "rtonukun"
        },
        {
            "client_name": "SBOJANAP-QAC65",
            "identity": "ATOM:9596801",
            "request_id": "5be33e78169b4485886cefe8b3f6ba93",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "virtual_parts",
            "site_code": "sjd",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "ODMUser"
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:00505694E10C",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:0050569496F4",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "sjc12yubi1",
            "identity": "ATOM Virtual:005d73efc85a",
            "request_id": "3967ef6803a945c48cd2705f023980d7",
            "server_version": "Apollo_CSA_Dev1-94-3",
            "service": "virtual_parts",
            "site_code": "cisco",
            "status": "Failure",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "rtonukun"
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:00505694E10C",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "AA2A2E99-87EB-4F3D-8629-9EB105AF53F2",
            "identity": "D59785D8-189E-4261-90A6-356E66BF75AC",
            "request_id": "979F36CB-708E-475C-90FF-ABC00046B7E7",
            "server_version": "D9122873-CA66-4459-BDB3-0BB951894A56",
            "service": "3B5440F9-D8A7-44A7-A457-E3545F95DE58",
            "site_code": "F3FBCF67-D7F6-4795-9DB4-9979AE481934",
            "status": "D4E6CA67-C6AB-49B5-B0F1-5CE0A994AE08",
            "status_code": 0,
            "status_message": "24F54F2B-E6E4-4D7B-B281-EF935F58A09E",
            "user_name": "B9E16658-AC82-4B74-AE21-58FC34274A2A"
        },
        {
            "client_name": "5848F59B-6B8F-49D8-B192-F1A7F48E27D6",
            "identity": "AD0387EA-3E31-4EBE-B2F2-C9B76D787E7E",
            "request_id": "B370AFDA-8344-4FC0-84AA-32E6729CD18E",
            "server_version": "6BDF7E42-864C-48CC-9CA6-1B5935A62D23",
            "service": "17B87EDA-A6C9-4B98-95E0-C8CDD7337760",
            "site_code": "EBE7C536-8D8D-4236-84E6-AE016E422A65",
            "status": "7AC642B9-1915-4629-BA71-64699FA7467D",
            "status_code": 0,
            "status_message": "E5389A1D-4CE1-4E45-A9A3-ECAB3EC005CC",
            "user_name": "9E7BBC5A-D60D-4BFB-9418-4E1FCD459279"
        },
        {
            "client_name": "148BA427-CEFB-4C35-804C-3A03D7B69790",
            "identity": "0EB6D578-616E-4482-90F8-E7FBD4D5C127",
            "request_id": "191FCC5E-A9EA-4DD0-AB14-25EA8780330B",
            "server_version": "B7A969FE-C60A-4D0E-AD31-FDD89125DE33",
            "service": "D0C2E705-E6CB-4DC8-89D8-90AB43AB84B1",
            "site_code": "EB24085F-6918-47CA-947F-7A8FF2F422F1",
            "status": "843EE49B-C9FA-43C7-A0AE-271760A5E2AC",
            "status_code": 0,
            "status_message": "D0761281-2096-4C12-9C8E-35CF4289EE15",
            "user_name": "8B205CC5-7065-439C-8786-F23605E5E17D"
        },
        {
            "client_name": "C48465C4-D667-4612-B963-37ABF15CD83B",
            "identity": "2B760C08-1C5D-4C35-A899-D2E7AE2A97A3",
            "request_id": "6FFF1BD3-4363-4784-B589-FD34B1A0F900",
            "server_version": "0CD685E3-AA5D-41E1-A079-27916A4C078D",
            "service": "81807674-964F-412E-8FF5-0DC935D6DDB0",
            "site_code": "DCC8156E-A02A-48E9-ABD7-F0378D944B28",
            "status": "CCE031B6-0C28-4067-B57F-C0EEC806CB2A",
            "status_code": 0,
            "status_message": "64F8C3D5-D303-415D-A287-1E77666A6B45",
            "user_name": "64A4E374-E657-4FB7-82E6-DE2AE5BE148C"
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:0050569496F4",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:0050569496F4",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "sjc12yubi1",
            "identity": "ATOM Virtual:005d73efc85a",
            "request_id": "8b5d8c2b1ed2438aa4e51d519c5e933e",
            "server_version": "Apollo_CSA_Dev1-94-3",
            "service": "virtual_parts",
            "site_code": "cisco",
            "status": "Failure",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "rtonukun"
        },
        {
            "client_name": "sjc12yubi1",
            "identity": "ATOM Virtual:005d73efc85a",
            "request_id": "c84d33eada2542e88d4f91f13aa2dea9",
            "server_version": "Apollo_CSA_Dev1-94-3",
            "service": "virtual_parts",
            "site_code": "cisco",
            "status": "Failure",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "rtonukun"
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:00505694E10C",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:00505694E10C",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "sjc12yubi1",
            "identity": "ATOM Virtual:005d73efc85a",
            "request_id": "5b25eb75126745c3bee59d4c58571690",
            "server_version": "Apollo_CSA_Dev1-94-3",
            "service": "virtual_parts",
            "site_code": "cisco",
            "status": "Failure",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "pid"
        },
        {
            "client_name": "D339BA3D-3E9E-425B-9016-741FB10625F5",
            "identity": "035C0DDF-164A-47CB-A708-0D56C2DE7BC3",
            "request_id": "DE05C5A1-7991-4A23-B617-F4407ADD2C3C",
            "server_version": "C8A53691-BDBD-43ED-AA77-B7ED20C8C42B",
            "service": "4BFF0150-7C73-467B-9ADE-522E40F8D89D",
            "site_code": "4DBC355F-B494-49CE-9DD4-CFF0687D1D65",
            "status": "BB0AEDF7-0F01-4CCE-A4D2-6778A4E16407",
            "status_code": 0,
            "status_message": "5DCC5DB1-0D85-4A27-A9E5-3865DCDAD6C0",
            "user_name": "84CEB22F-2C16-4D8B-8D91-C6A211BB7EA1"
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:00505694E10C",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:00505694E10C",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "sjc12yubi1",
            "identity": "ATOM Virtual:005d73efc85a",
            "request_id": "b6df39d48cb6497d99f9413bfa4503c1",
            "server_version": "Apollo_CSA_Dev1-94-3",
            "service": "virtual_parts",
            "site_code": "cisco",
            "status": "Failure",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "rtonukun"
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:00505694E10C",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:00505694E10C",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:0050569496F4",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:0050569496F4",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "sjc12yubi1",
            "identity": "ATOM Virtual:005d73efc85a",
            "request_id": "a4aa5dc0cbab45e1bf08eac4b81a6980",
            "server_version": "Apollo_CSA_Dev1-94-3",
            "service": "virtual_parts",
            "site_code": "sjd",
            "status": "Failure",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "pid"
        },
        {
            "client_name": "sjc12yubi1",
            "identity": "ATOM Virtual:005d73efc85a",
            "request_id": "e6ac136aa8b0459680fa81a373983ee0",
            "server_version": "Apollo_CSA_Dev1-94-3",
            "service": "virtual_parts",
            "site_code": "Cisco",
            "status": "Failure",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "rtonukun"
        },
        {
            "client_name": "3920EC9A-6E28-432A-977E-39F9150FE97D",
            "identity": "7630E95B-FC23-4CDD-91AF-D3D8EEC7B863",
            "request_id": "7BF34145-2A5B-4251-A902-A212E66D8888",
            "server_version": "AFBF6365-BAA4-44FE-9F5B-5FF5712FF14D",
            "service": "6998C0AB-82A7-4580-ADCB-475BC4C73982",
            "site_code": "63539CB5-2EBE-432E-A5C2-C4B9C6CB014C",
            "status": "11CB63AB-8642-4A6E-99E1-A93962232FA8",
            "status_code": 0,
            "status_message": "A7677B64-1DDF-4A44-A93C-32ADF89FC8B7",
            "user_name": "9FC4B989-6653-48DB-BF60-A3DD7C6DB4E2"
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:0050569496F4",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:00505694E10C",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:0050569496F4",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "747857D1-2FC9-49EB-9639-69D04B712FCD",
            "identity": "9F2F08A2-51C1-4B0B-94EC-6BD34043B922",
            "request_id": "D37EED5D-60E5-4AE9-94BD-C4414BA786CB",
            "server_version": "579A00D4-1F13-483E-BE48-48AF84EFE2B0",
            "service": "DA5DB58A-C38F-4152-A5F7-5C80052C7FD5",
            "site_code": "E3C41255-DA00-4273-920E-40BFC5FE86A1",
            "status": "E222CFE0-0C0E-48C9-A015-39511D282BA0",
            "status_code": 0,
            "status_message": "FE3EE4E1-DE04-4001-B774-FCA987B47F9A",
            "user_name": "1DD6E576-4419-4FC4-A39B-7F0EFE5A3A44"
        },
        {
            "client_name": "sjc12yubi1",
            "identity": "ATOM Virtual:005d73efc85a",
            "request_id": "02a5fc4433bd4a3dbe4298ca323e9d44",
            "server_version": "Apollo_CSA_Dev1-94-3",
            "service": "virtual_parts",
            "site_code": "cisco",
            "status": "Failure",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "rtonukun"
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:0050569496F4",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "0FB50C45-1B89-4C6B-8680-F1E5DA7D2B75",
            "identity": "12112BFD-061F-4291-B5FF-7165523BB522",
            "request_id": "F8D7D74F-28C0-4629-B9AD-B42B7E4B5EFD",
            "server_version": "F4D7EB83-B122-44C5-A60D-08C762F84344",
            "service": "DC54E826-EADC-4E1D-921B-D226D40EC152",
            "site_code": "B41ABAA8-562D-4047-AFA0-13A7F37C0B54",
            "status": "ECE7F5BB-C0F7-44DF-891B-D4161C999E7E",
            "status_code": 0,
            "status_message": "0C3B53EF-27D3-43D9-9809-3230E41FC93A",
            "user_name": "BA5A336F-6F1E-408F-B574-0429CA4BE755"
        },
        {
            "client_name": "DACD22EC-F800-4CA7-96F2-CFA5242FCD32",
            "identity": "669278A8-B45D-4321-9429-EA58FCA508E0",
            "request_id": "30894FD1-BF29-4F16-BF99-4CAA9ED5DB86",
            "server_version": "FA651351-4549-4120-8E28-683BA00B779A",
            "service": "F3010A6B-BA22-4D64-AD45-959D4CE4BED4",
            "site_code": "22073B27-25AC-4E57-AAB9-8CCF4CBBC3AE",
            "status": "7C54604D-3732-4EAF-9E50-CF0FA75E56F5",
            "status_code": 0,
            "status_message": "3F9293B2-3588-41D2-8312-77E2BFF232E7",
            "user_name": "5D045691-FC1D-4E58-A786-513C1CBE933D"
        },
        {
            "client_name": "DB059AB6-CCBC-411F-AECA-3C5123164DE6",
            "identity": "12F4F433-43D6-4496-A8AB-96C91D888BBF",
            "request_id": "69E6372D-3AB0-4E75-9F77-3711B81DDC5F",
            "server_version": "A7501FEE-0409-463A-813C-3C1370222A4F",
            "service": "8D8C2ACA-E0B8-405F-8A20-A794E017930B",
            "site_code": "B1185DA9-0FB8-4F41-B3C7-9312CEC105A9",
            "status": "CF1B0589-2486-4D96-8328-81719C562864",
            "status_code": 0,
            "status_message": "B1F42E03-E7A5-44EF-887D-0F23AB3ECE11",
            "user_name": "3F41AC5B-3AA2-4A35-A83D-4A6D45880D8F"
        },
        {
            "client_name": "A35F47FA-F008-456E-AA65-97C23ABFAF46",
            "identity": "E6D1A8AD-A428-40D1-8E0C-578AD96666F7",
            "request_id": "9C2ED636-93C5-493C-8A25-6147A089E51D",
            "server_version": "E8C340F7-5E84-49C1-9760-0FA7CFB61325",
            "service": "41014836-390A-48AB-B29D-401CDD3993D5",
            "site_code": "6EC654FA-38BE-4083-8AE1-3B31A4EEB2B9",
            "status": "04684053-8A85-47B2-89D9-0DA07056D7CB",
            "status_code": 0,
            "status_message": "69133183-4EF8-4B34-B1DF-EB8C226C37A1",
            "user_name": "B5081DCF-DB0F-474E-A1BB-862BC9D63A66"
        },
        {
            "client_name": "3FC7F15F-C213-46FC-8D48-3D8BF7608CF7",
            "identity": "790A594B-BED0-40CB-B309-B5316F9EC322",
            "request_id": "188D867F-80B9-4499-9598-6A1DD6691CE5",
            "server_version": "2D9AC84C-0A14-4CFC-9662-A9EB382C106A",
            "service": "64946F66-5C20-4FF5-B9F3-D7299DE9AE92",
            "site_code": "34876B36-5D02-4BAC-B33F-7983F85A762D",
            "status": "2AD408BB-C358-455D-B208-8125CC187791",
            "status_code": 0,
            "status_message": "4DCC2C05-E481-46D3-AF19-673C549223EB",
            "user_name": "92F82843-EE28-4213-833D-03EE63E28F68"
        },
        {
            "client_name": "E076A2BF-9D9A-418A-9C38-05790BBAD579",
            "identity": "0CE9981B-2894-4134-8FBB-A149F863221C",
            "request_id": "F3E6F32E-9682-4F44-A121-6CBBD269A245",
            "server_version": "EE6D24ED-C985-49DE-A750-E45D40D80FF4",
            "service": "A55CAB80-5EF6-434A-81CB-D7968A7AC0C4",
            "site_code": "496E440C-1D05-4E25-9733-BAC8F748E05D",
            "status": "738DF464-0E87-4D0E-91DC-35F5BD8BFE0A",
            "status_code": 0,
            "status_message": "738C157B-49EC-4DFF-A47F-3C86E5498A17",
            "user_name": "D3EE4AF5-2DFD-4973-AB4B-B092B4E4DD58"
        },
        {
            "client_name": "6A3C9875-82E4-4A26-893F-0BEC764C8277",
            "identity": "964FD417-41ED-42B7-9530-BB7BAAD653B8",
            "request_id": "7F9BCA29-1924-477C-8662-977053F1E3D8",
            "server_version": "0C880F9E-9AAB-4053-AC26-44D78E21F09F",
            "service": "73F5AB5F-E631-45CE-9859-99F13321BDED",
            "site_code": "E14435D1-6E1B-4AB1-BCC2-96CA3E797F40",
            "status": "C173C884-F5A8-4610-B3FC-003AC6201151",
            "status_code": 0,
            "status_message": "039E68D8-7840-4A5E-92B2-681EC9E6CF6E",
            "user_name": "7760CAA4-D4A6-4447-8BDE-6AE39222B415"
        },
        {
            "client_name": "F2C7600D-E35D-4AE6-B3F2-45CC2AFFA2C2",
            "identity": "D711CC4C-8B86-4700-BD1C-E9C07648AD0B",
            "request_id": "A035D00A-F29A-45E0-86A1-3C0D42BD401B",
            "server_version": "B39E7544-EECB-4EC7-9290-2A9E888AAE44",
            "service": "06132334-CDA0-491A-9A03-4F666EED63AF",
            "site_code": "6AC5F3EE-1C98-40FD-BF1E-D198B5E38475",
            "status": "7BF413F9-9CA5-400E-8472-2891B59572B5",
            "status_code": 0,
            "status_message": "E24F4562-4B81-4C36-A5F2-2006417FFD7B",
            "user_name": "2DAC849E-792F-46EF-9075-1906BA2A293A"
        },
        {
            "client_name": "B0DD4C3C-C41A-4F77-958D-1831EDB5334F",
            "identity": "159F2C9F-AD83-4F8B-AA14-FFB93099992C",
            "request_id": "601BABFD-6A5B-40BF-A67D-44AB7E998F4D",
            "server_version": "155395B7-C6DA-4A71-8283-EFFB3BE70878",
            "service": "ECB421FE-49FF-4D74-96DD-A05327D58F85",
            "site_code": "DE9DA1F7-8EDC-4282-929C-AABAFF965290",
            "status": "4E28A4A7-5147-41F8-80EE-97592DDF28E2",
            "status_code": 0,
            "status_message": "DC28402F-FB1E-4CC8-A964-507F41F5B277",
            "user_name": "7E8863F5-A37A-45F1-B495-95BAFC86FA58"
        },
        {
            "client_name": "sjc12yubi1",
            "identity": "ATOM Virtual:005d73efc85a",
            "request_id": "89c122df7ce64e33b9872e9b50a47ce8",
            "server_version": "Apollo_CSA_Dev1-94-3",
            "service": "virtual_parts",
            "site_code": "cisco",
            "status": "Failure",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "rtonukun"
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:0050569496F4",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "sjc12yubi1",
            "identity": "ATOM Virtual:005d73efc85a",
            "request_id": "5d9970185d7d47d5b4eeae1118796751",
            "server_version": "Apollo_CSA_Dev1-94-3",
            "service": "virtual_parts",
            "site_code": "cisco",
            "status": "Failure",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "rtonukun"
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:0050569496F4",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:0050569496F4",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "sjc12yubi1",
            "identity": "ATOM Virtual:005d73efc85a",
            "request_id": "a966696e049347b599b67bfa3a2ccedb",
            "server_version": "Apollo_CSA_Dev1-94-3",
            "service": "virtual_parts",
            "site_code": "cisco",
            "status": "Failure",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "rtonukun"
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:00505694E10C",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:00505694E10C",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:00505694E10C",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:0050569496F4",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "sjc12yubi1",
            "identity": "ATOM Virtual:005d73efc85a",
            "request_id": "bda75b60eae24fbdb2449ed84f738cd9",
            "server_version": "Apollo_CSA_Dev1-94-3",
            "service": "virtual_parts",
            "site_code": "cisco",
            "status": "Failure",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "rtonukun"
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:00505694E10C",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "sjc12yubi1",
            "identity": "ATOM Virtual:005d73efc85a",
            "request_id": "33896d1cdefe42c484e1e9dc79379919",
            "server_version": "Apollo_CSA_Dev1-94-3",
            "service": "virtual_parts",
            "site_code": "cisco",
            "status": "Failure",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "rtonukun"
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:00505694E10C",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:0050569496F4",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "sjc12yubi1",
            "identity": "ATOM Virtual:005d73efc85a",
            "request_id": "e3046cde5c024bafbe46cad1187cedc4",
            "server_version": "Apollo_CSA_Dev1-94-3",
            "service": "virtual_parts",
            "site_code": "cisco",
            "status": "Failure",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "rtonukun"
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:00505694E10C",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:00505694E10C",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:0050569496F4",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "sjc12yubi1",
            "identity": "ATOM Virtual:005d73efc85a",
            "request_id": "60e2b1d8216a4cd0ac99832e25b89df2",
            "server_version": "Apollo_CSA_Dev1-94-3",
            "service": "virtual_parts",
            "site_code": "cisco",
            "status": "Failure",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "rtonukun"
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:00505694E10C",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:0050569496F4",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:00505694E10C",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:0050569496F4",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:00505694E10C",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:0050569496F4",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:00505694E10C",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "sjc12yubi1",
            "identity": "ATOM Virtual:005d73efc85a",
            "request_id": "599e58d03e4d4531a035fcb8e2eba3e4",
            "server_version": "Apollo_CSA_Dev1-94-3",
            "service": "virtual_parts",
            "site_code": "sjd",
            "status": "Failure",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "rtonukun"
        },
        {
            "client_name": "sjc12yubi1",
            "identity": "ATOM Virtual:005d73efc85a",
            "request_id": "25102f032efe4ef7aac2dc1484e64460",
            "server_version": "Apollo_CSA_Dev1-94-3",
            "service": "virtual_parts",
            "site_code": "cisco",
            "status": "Failure",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "pid"
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:0050569496F4",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "sjc12yubi1",
            "identity": "ATOM Virtual:005d73efc85a",
            "request_id": "668a1525dee94432bd4ad3136c1cbaeb",
            "server_version": "Apollo_CSA_Dev1-94-3",
            "service": "virtual_parts",
            "site_code": "cisco",
            "status": "Failure",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "pid"
        },
        {
            "client_name": "sjc12yubi1",
            "identity": "ATOM Virtual:005d73efc85a",
            "request_id": "3cd3c67772d849c5ae40968b10e1112d",
            "server_version": "Apollo_CSA_Dev1-94-3",
            "service": "virtual_parts",
            "site_code": "cisco",
            "status": "Failure",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "pid"
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:00505694E10C",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:00505694E10C",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:00505694E10C",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "sjc12yubi1",
            "identity": "ATOM Virtual:005d73efc85a",
            "request_id": "f0ebba956bb04f45a7dc01faab9e1e9f",
            "server_version": "Apollo_CSA_Dev1-94-3",
            "service": "virtual_parts",
            "site_code": "cisco",
            "status": "Failure",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "pid"
        },
        {
            "client_name": "srglab22apollo",
            "identity": "ATOM Virtual:00505694E10C",
            "request_id": "ACT2 (RE)SUDI",
            "server_version": "Apollo_CSA_Dev1-114-0",
            "service": "get_sudi_certificate",
            "site_code": "",
            "status": "Success",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": ""
        },
        {
            "client_name": "sjc12yubi1",
            "identity": "ATOM Virtual:005d73efc85a",
            "request_id": "aaf6681ae49f414cb8261f09d5c32648",
            "server_version": "Apollo_CSA_Dev1-94-3",
            "service": "virtual_parts",
            "site_code": "cisco",
            "status": "Failure",
            "status_code": 0,
            "status_message": "SUCCESS",
            "user_name": "rtonukun"
        }
    ]



df = pd.Series(data1)

print(df)
#hello just adding some dummy data

