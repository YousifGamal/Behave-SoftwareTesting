import os
import threading
from wsgiref import simple_server
from wsgiref.simple_server import WSGIRequestHandler
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service
from applications.app import app



def before_all(context):
    context.server = simple_server.WSGIServer(("",7777),WSGIRequestHandler) #create WSGIServer instance
    context.server.set_app(app) #set the app that will be called on getting requests
    context.appthread = threading.Thread(target=context.server.serve_forever) #create thread to call the function server_forever()
    context.appthread.start() #start the thread
    
    context.service = Service("./applications/geckodriver") #include the geckodriver
    context.browser = webdriver.Firefox(service=context.service) #initiate the firefox browser object
    context.browser.set_page_load_timeout(5000) #set the time out of the browser

def after_all(context):
    context.server.shutdown() #shutdown the server_for() loop
    context.browser.quit() #close the browser
    context.appthread.join() #kill the thread