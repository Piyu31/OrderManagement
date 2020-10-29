from pymongo import MongoClient
import datetime
import sys

from bson.objectid import ObjectId

global con
global db
global col

def connect_db():
	global con
	global db
	global col
	con = MongoClient('mongodb+srv://test:test@cluster0.kw4id.mongodb.net/Order_management_db?retryWrites=true&w=majority')
	db = con.Order_management_db
	col = db.order_mgmt_records


def get_orders_details():
	global col
	connect_db()
	orderinfo_from_db = col.find({})
	return orderinfo_from_db

def save_orders_details(orders_info):
	global col
	connect_db()
	col.insert(orders_info)
	return "saved Successfully"


def get_orders_records_to_update(orders_id):
	global col
	connect_db()
	orderdata_from_db = col.find({"_id": ObjectId(orders_id)})
	return orderdata_from_db



def update_one_record(orders_id, Data):
    global col
    connect_db()    
    col.update_one({"_id": ObjectId(orders_id)}, {'$set' :{'orderId':Data["orderId"],
    													   'retailer_Id':Data["retailer_Id"], 
    													   'retailer_Name':Data["retailer_Name"], 
    													   'retailer_Email_Id':Data["retailer_Email_Id"], 
    													   'retailer_phone_number':Data["retailer_phone_number"], 
    													   'installer_Id':Data["installer_Id"], 
    													   'installer_Name':Data["installer_Name"], 
    													   'installer_Email_Id':Data["installer_Email_Id"], 
    													   'installer_phone_number':Data["installer_phone_number"], 
    													   'dcbasicinfo_Id':Data["dcbasicinfo_Id"], 
    													   'dcbasicinfo_Name':Data["dcbasicinfo_Name"], 
    													   'dcbasicinfo_Email_Id':Data["dcbasicinfo_Email_Id"], 
    													   'dcbasicinfo_phone_number':Data["dcbasicinfo_phone_number"], 
    													   'consumer_Id':Data["consumer_Id"], 
    													   'consumer_Name':Data["consumer_Name"], 
    													   'consumer_Email_Id':Data["consumer_Email_Id"], 
    													   'consumer_phone_number':Data["consumer_phone_number"]} })
    return


def search_ordercenter_by_id(id):
   global col
   connect_db() 
   searched_data = col.find({'orderId':str(id)})
   return searched_data