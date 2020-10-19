from django.apps import AppConfig
import pyrebase

config = {
  "apiKey": "AIzaSyCUsi0_jT6xGsJcufGS40DBDuFrMfitKZs",
  "authDomain": "abacus-dental-auth.firebaseapp.com",
  "databaseURL": "https://abacus-dental-auth.firebaseio.com",
  "storageBucket": "abacus-dental-auth.appspot.com"
}

firebase = pyrebase.initialize_app(config)


class InventoryConfig(AppConfig):
    name = 'abacusinventory'
    verbose_name = 'Abacus Dental Inventory Microservice'
