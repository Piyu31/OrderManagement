from flask import Flask,render_template,redirect,request,session,flash,url_for,g
import datetime
import sys
import random
import time

import json

import order_management_db

app = Flask(__name__)


app.secret_key="sdg75mkjs5hsdbyast4"


@app.route("/")
def index():
	#get all data from db
	orders_info = order_management_db.get_orders_details()
	order_manage_list = []
	for o in orders_info:
		order_manage_list.append(o)
	print(order_manage_list)
	return render_template('order_form.html', odermanagementlist = order_manage_list )


def setData():
	#Empty List
	orderRecords = {}
	#request data from UI
	#OrderID
	orderId = request.form['orderid']
	#set data to the Empty list
	orderRecords ["orderId"]=orderId

	#Retailer
	
	retailer_Id =  request.form['retailerid']
	retailer_Name = request.form['retailername']
	retailer_Email_Id = request.form['retaileremail_id']
	retailer_phone_number = request.form['retailerphone_num'] 

	# Retailer={"retailer_Id": request.form['retailerid'],
	# 		   "retailer_Name ": request.form['retailername'],
	# 			"retailer_Email_Id" : request.form['retaileremail_id'],
	#            "retailer_phone_number":request.form['retailerphone_num']
	#           }

	#set data to the Empty list
	orderRecords["retailer_Id"]=retailer_Id
	orderRecords["retailer_Name"]=retailer_Name
	orderRecords["retailer_Email_Id"]=retailer_Email_Id
	orderRecords["retailer_phone_number"]=retailer_phone_number
	
	#Installer
	# Installer={"installer_Id": request.form['installerid'],
	# 		   "installer_Name ": request.form['installername'],
	# 			"installer_Email_Id" : request.form['installeremail_id'],
	#            "installer_phone_number":request.form['installerphone_num']
	#           }
	
	installer_Id =  request.form['installerid']
	installer_Name= request.form['installername']
	installer_Email_Id = request.form['installeremail_id']
	installer_phone_number = request.form['installerphone_num']
	#set data to the Empty list
	orderRecords["installer_Id"]=installer_Id
	orderRecords["installer_Name"]=installer_Name
	orderRecords["installer_Email_Id"]=installer_Email_Id
	orderRecords["installer_phone_number"]=installer_phone_number

	#DoorCenter Basic Info
	# DoorCenter_Basic_Info={"dcbasicinfo_Id": request.form['dcbasicinfoid'],
	# 		   "dcbasicinfo_Name ": request.form['dcbasicinfoname'],
	# 			"dcbasicinfo_Email_Id" : request.form['dcbasicinfoemail_id'],
	#            "dcbasicinfo_phone_number":request.form['dcbasicinfophone_num']
	#           }
	
	dcbasicinfo_Id =  request.form['dcbasicinfoid']
	dcbasicinfo_Name= request.form['dcbasicinfoname']
	dcbasicinfo_Email_Id = request.form['dcbasicinfoemail_id']
	dcbasicinfo_phone_number = request.form['dcbasicinfophone_num']
	#set data to the Empty list
	orderRecords["dcbasicinfo_Id"]=dcbasicinfo_Id
	orderRecords["dcbasicinfo_Name"]=dcbasicinfo_Name
	orderRecords["dcbasicinfo_Email_Id"]=dcbasicinfo_Email_Id
	orderRecords["dcbasicinfo_phone_number"]=dcbasicinfo_phone_number

	#Consumer
	# Consumer={"consumer_Id": request.form['consumerid'],
	# 		   "consumer_Name ": request.form['consumername'],
	# 			"consumer_Email_Id" : request.form['consumeremail_id'],
	#            "consumer_phone_number":request.form['consumerphone_num']
	#           }

	
	consumer_Id =  request.form['consumerid']
	consumer_Name= request.form['consumername']
	consumer_Email_Id = request.form['consumeremail_id']
	consumer_phone_number = request.form['consumerphone_num']
	#set data to the Empty list
	orderRecords["consumer_Id"]=consumer_Id
	orderRecords["consumer_Name"]=consumer_Name
	orderRecords["consumer_Email_Id"]=consumer_Email_Id
	orderRecords["consumer_phone_number"]=consumer_phone_number

	# Data={"Details":{"orderDeatils":orderRecords,
	# 				  "retailerDetails":Retailer,
	# 				  "InsatllerDetails":Installer,
	# 				  "DoorCenterDeatils":DoorCenter_Basic_Info,
	# 				  "consumerDeatils":Consumer}}
	return orderRecords 

@app.route("/", methods=['POST'])
def save_data_to_ordermanagement():
	orderRecords = setData()
	#print records in cmd
	print(orderRecords)
	order_management_db.save_orders_details(orderRecords)
	return redirect(url_for('index'))


@app.route("/update", methods=['POST'])
def update_ordersinfo_records():
	orderRecords = setData()
	#print records in cmd
	print(orderRecords)
	print(request.form['id'])
	#send to db
	ordermanageid=request.form['id']
	order_management_db.update_one_record(ordermanageid, orderRecords)
	return redirect(url_for('index'))



@app.route("/edit/<orders_id>", methods=['POST'])
def edit_Record(orders_id):
    ordersid = orders_id
    one_order = order_management_db.get_orders_records_to_update(orders_id)
    return render_template('order_edit.html', odermanagementlist = one_order)


ordercenter = []
search_results_activate_orders = False

@app.route("/ordermanagecenter", methods=['GET'])
def ordercenterWrapper():
   global ordercenter
   global search_results_activate_orders
   order_center_list = []
   if search_results_activate_orders:
       order_center_list = ordercenter
   else:
       order_manage_list = order_management_db.get_orders_details()
       for orderm in order_manage_list:
           order_center_list.append(orderm)
   search_results_activate_orders = False
   return render_template('order_form.html',  odermanagementlist = order_center_list)


@app.route('/ordercenter/searchbyid', methods=['POST'])
def searchordermanagementByorderid():
   global ordercenter
   global search_results_activate_orders
   order_center_list = []
   ordercenter_id = request.form['searchbyorderid']
   order_manage_list = order_management_db.search_ordercenter_by_id(ordercenter_id)
   for orderm in order_manage_list:
       order_center_list.append(orderm)
   print(order_center_list)
   ordercenter = order_center_list
   search_results_activate_orders = True
   return redirect(url_for('ordercenterWrapper'))










if __name__ == '__main__':
	app.run(debug=True)

