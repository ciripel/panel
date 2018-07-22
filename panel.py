#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 21:56:30 2018

@author: ciripel
"""
from flask import Flask, render_template
from random import randint
from flask_table import Table, Col
from requests import get
import math

app = Flask(__name__)


class ItemTable(Table):
    miner = Col('Miner')
    miner_ip = Col('IP')
    uptime = Col('Uptime')
    total_hash = Col('Total Hash')
    gpu_hash = Col('Detailed Hash / GPU')
    temp = Col('Temp')
    none = Col('')
    name = Col('Nume')
    amount = Col('Amount')
    coin = Col('Coin')
    html_attrs = {'id': 'customers'}


class Item(object):
    def __init__(self, miner, miner_ip, uptime, total_hash, gpu_hash, temp,
                 none, name, amount, coin):
        self.miner = miner
        self.miner_ip = miner_ip
        self.uptime = uptime
        self.total_hash = total_hash
        self.gpu_hash = gpu_hash
        self.temp = temp
        self.none = none
        self.name = name
        self.amount = amount
        self.coin = coin


@app.route("/mineri/")
def hello():
    response = get("http://ronta1.ethosdistro.com/?json=yes")
    data = response.json()
    miner1 = data["rigs"]["018662"]["rack_loc"]
    miner_ip1 = data["rigs"]["018662"]["ip"]
    uptimesecs1 = data["rigs"]["018662"]["uptime"]
    days = int(math.floor(int(uptimesecs1)/60/60/24))
    hours = int(math.floor((int(uptimesecs1) - math.floor(int(uptimesecs1)/60/60/24)*60*60*24)/60/60))
    minutes = int(math.floor((int(uptimesecs1) - math.floor(int(uptimesecs1)/60/60)*60*60)/60))
    seconds = int((int(uptimesecs1) - math.floor(int(uptimesecs1)/60)*60))
    if days == hours == minutes == 0:
        seq = (str(seconds), "s")
    elif days == hours == 0 != minutes:
        seq = (str(minutes), "m ", str(seconds), "s")
    elif days == 0 != hours:
        seq = (str(hours), "h ", str(minutes), "m ", str(seconds), "s")
    else:
        seq = (str(days), "d ", str(hours), "h ", str(minutes), "m ", str(seconds), "s")

    uptime1 = ''.join(seq)
    total_hash1 = data["rigs"]["018662"]["hash"]
    gpu_hash1 = data["rigs"]["018662"]["miner_hashes"]
    temp1 = data["rigs"]["018662"]["temp"]

    response = get("http://ronta2.ethosdistro.com/?json=yes")
    data = response.json()
    miner2 = data["rigs"]["018616"]["rack_loc"]
    miner_ip2 = data["rigs"]["018616"]["ip"]
    uptimesecs2 = data["rigs"]["018616"]["uptime"]
    days = int(math.floor(int(uptimesecs2)/60/60/24))
    hours = int(math.floor((int(uptimesecs2) - math.floor(int(uptimesecs2)/60/60/24)*60*60*24)/60/60))
    minutes = int(math.floor((int(uptimesecs2) - math.floor(int(uptimesecs2)/60/60)*60*60)/60))
    seconds = int((int(uptimesecs2) - math.floor(int(uptimesecs2)/60)*60))
    if days == hours == minutes == 0:
        seq = (str(seconds), "s")
    elif days == hours == 0 != minutes:
        seq = (str(minutes), "m ", str(seconds), "s")
    elif days == 0 != hours:
        seq = (str(hours), "h ", str(minutes), "m ", str(seconds), "s")
    else:
        seq = (str(days), "d ", str(hours), "h ", str(minutes), "m ", str(seconds), "s")

    uptime2 = ''.join(seq)
    total_hash2 = data["rigs"]["018616"]["hash"]
    gpu_hash2 = data["rigs"]["018616"]["miner_hashes"]
    temp2 = data["rigs"]["018616"]["temp"]

    response = get("http://rontb1.ethosdistro.com/?json=yes")
    data = response.json()
    miner3 = data["rigs"]["66afbd"]["rack_loc"]
    miner_ip3 = data["rigs"]["66afbd"]["ip"]
    uptimesecs3 = data["rigs"]["66afbd"]["uptime"]
    days = int(math.floor(int(uptimesecs3)/60/60/24))
    hours = int(math.floor((int(uptimesecs3) - math.floor(int(uptimesecs3)/60/60/24)*60*60*24)/60/60))
    minutes = int(math.floor((int(uptimesecs3) - math.floor(int(uptimesecs3)/60/60)*60*60)/60))
    seconds = int((int(uptimesecs3) - math.floor(int(uptimesecs3)/60)*60))
    if days == hours == minutes == 0:
        seq = (str(seconds), "s")
    elif days == hours == 0 != minutes:
        seq = (str(minutes), "m ", str(seconds), "s")
    elif days == 0 != hours:
        seq = (str(hours), "h ", str(minutes), "m ", str(seconds), "s")
    else:
        seq = (str(days), "d ", str(hours), "h ", str(minutes), "m ", str(seconds), "s")

    uptime3 = ''.join(seq)
    total_hash3 = data["rigs"]["66afbd"]["hash"]
    gpu_hash3 = data["rigs"]["66afbd"]["miner_hashes"]
    temp3 = data["rigs"]["66afbd"]["temp"]

    response = get("http://rontg1.ethosdistro.com/?json=yes")
    data = response.json()
    miner4 = data["rigs"]["f68192"]["rack_loc"]
    miner_ip4 = data["rigs"]["f68192"]["ip"]
    uptimesecs4 = data["rigs"]["f68192"]["uptime"]
    days = int(math.floor(int(uptimesecs4)/60/60/24))
    hours = int(math.floor((int(uptimesecs4) - math.floor(int(uptimesecs4)/60/60/24)*60*60*24)/60/60))
    minutes = int(math.floor((int(uptimesecs4) - math.floor(int(uptimesecs4)/60/60)*60*60)/60))
    seconds = int((int(uptimesecs4) - math.floor(int(uptimesecs4)/60)*60))
    if days == hours == minutes == 0:
        seq = (str(seconds), "s")
    elif days == hours == 0 != minutes:
        seq = (str(minutes), "m ", str(seconds), "s")
    elif days == 0 != hours:
        seq = (str(hours), "h ", str(minutes), "m ", str(seconds), "s")
    else:
        seq = (str(days), "d ", str(hours), "h ", str(minutes), "m ", str(seconds), "s")

    uptime4 = ''.join(seq)
    total_hash4 = data["rigs"]["f68192"]["hash"]
    gpu_hash4 = data["rigs"]["f68192"]["miner_hashes"]
    temp4 = data["rigs"]["f68192"]["temp"]

    """
    response = get("http://rontg2.ethosdistro.com/?json=yes")
    data = response.json()
    miner5 = data["rigs"]["874d6d"]["rack_loc"]
    miner_ip5 = data["rigs"]["874d6d"]["ip"]
    uptimesecs5 = data["rigs"]["874d6d"]["uptime"]
    days = int(math.floor(int(uptimesecs5)/60/60/24))
    hours = int(math.floor((int(uptimesecs5) - math.floor(int(uptimesecs5)/60/60/24)*60*60*24)/60/60))
    minutes = int(math.floor((int(uptimesecs5) - math.floor(int(uptimesecs5)/60/60)*60*60)/60))
    seconds = int((int(uptimesecs5) - math.floor(int(uptimesecs5)/60)*60))
    if days == hours == minutes == 0:
        seq = (str(seconds), "s")
    elif days == hours == 0 != minutes:
        seq = (str(minutes), "m ", str(seconds), "s")
    elif days == 0 != hours:
        seq = (str(hours), "h ", str(minutes), "m ", str(seconds), "s")
    else:
        seq = (str(days), "d ", str(hours), "h ", str(minutes), "m ", str(seconds), "s")

    uptime5 = ''.join(seq)
    total_hash5 = data["rigs"]["874d6d"]["hash"]
    gpu_hash5 = data["rigs"]["874d6d"]["miner_hashes"]
    temp5 = data["rigs"]["874d6d"]["temp"]
    """

    """
    response = get("http://aka.pool.sexy/api/accounts/0x04cfa4f946e2841b79d3e895e857f9ad3a951c04")
    data = response.json()
    curr_hash = data["currentHashrate"]
    seq = (str(math.floor(int(curr_hash)/10**4)/100), "Mh")
    curr_hash_a = ' '.join(seq)
    balance_cPS = data["stats"]["balance"]

    response = get("http://aka.pool.sexy/api/accounts/0xd355a084e7a6d8fce012628a3355f4d594507307")
    data = response.json()
    curr_hash = data["currentHashrate"]
    seq = (str(math.floor(int(curr_hash)/10**4)/100), "Mh")
    curr_hash_b = ' '.join(seq)
    balance_bPS = data["stats"]["balance"]

    response = get("http://aka.pool.sexy/api/accounts/0xFbE0dc3E824c68eF5A123E2F1a5760D46fC8A7bC")
    data = response.json()
    curr_hash = data["currentHashrate"]
    seq = (str(math.floor(int(curr_hash)/10**4)/100), "Mh")
    curr_hash_g = ' '.join(seq)
    balance_gPS = data["stats"]["balance"]

    response = get("http://api.akroma.io/addresses/0x04cfa4f946e2841b79d3e895e857f9ad3a951c04")
    data = response.json()
    balance_cM = data["balance"]

    response = get("http://api.akroma.io/addresses/0x80363B2956B00946D8F05D8B56DeAA2672613faf")
    data = response.json()
    balance_cMn = data["balance"]

    response = get("http://api.akroma.io/addresses/0xd355a084e7a6d8fce012628a3355f4d594507307")
    data = response.json()
    balance_bM = data["balance"]

    response = get("http://api.akroma.io/addresses/0xFbE0dc3E824c68eF5A123E2F1a5760D46fC8A7bC")
    data = response.json()
    balance_gM = data["balance"]

    bal_cPS = math.floor(balance_cPS/10**7)/100
    bal_cM = math.floor(float(balance_cM)*100)/100
    bal_cMn = math.floor((float(balance_cMn)-5000)*100)/100
    bal_bPS = math.floor(balance_bPS/10**7)/100
    bal_bM = math.floor(float(balance_bM)*100)/100
    bal_gPS = math.floor(balance_gPS/10**7)/100
    bal_gM = math.floor(float(balance_gM)*100)/100
    seq = (bal_cPS, bal_cM, bal_cMn, bal_bPS, bal_bM, bal_gPS, bal_gM)
    bal_total = math.floor(math.fsum(seq)*100)/100

    items = [Item(miner1, miner_ip1, uptime1, total_hash1, gpu_hash1, temp1,
                  "", "Ciripel Pool Sexy", bal_cPS, "AKA"),
             Item(miner2, miner_ip2, uptime2, total_hash2, gpu_hash2, temp2,
                  "", "Ciripel Mining", bal_cM, "AKA"),
             Item(miner3, miner_ip3, uptime3, total_hash3, gpu_hash3, temp3,
                  "", "Ciripel MN Rest", bal_cMn, "AKA"),
             Item(miner4, miner_ip4, uptime4, total_hash4, gpu_hash4, temp4,
                  "", "Banica Pool Sexy", bal_bPS, "AKA"),
             Item(miner5, miner_ip5, uptime5, total_hash5, gpu_hash5, temp5,
                  "", "Banica Mining", bal_bM, "AKA"),
             Item("", "", "", "", "", "", "", "Georgel Pool Sexy", bal_gPS,
                  "AKA"),
             Item("", "", "Ciripel Pool Sexy", curr_hash_a, "", "", "",
                  "Georgel Mining", bal_gM, "AKA"),
             Item("", "", "Banica Pool Sexy", curr_hash_b, "", "", "",
                  "", "", ""),
             Item("", "", "Georgel Pool Sexy", curr_hash_g, "", "", "",
                  "Total", bal_total, "AKA"),
             Item("", "", "", "", "", "", "", "Rest pana la MN",
                  5000-bal_total, "AKA"),
             Item("", "", "", "", "", "", "", "", "", ""), ]
    """
    items = [Item(miner1, miner_ip1, uptime1, total_hash1, gpu_hash1, temp1,
                  "", "", "", ""),
             Item(miner2, miner_ip2, uptime2, total_hash2, gpu_hash2, temp2,
                  "", "", "", ""),
             Item(miner3, miner_ip3, uptime3, total_hash3, gpu_hash3, temp3,
                  "", "", "", ""),
             Item(miner4, miner_ip4, uptime4, total_hash4, gpu_hash4, temp4,
                  "", "", "", ""),
	     Item("", "", "", "", "", "",
                  "", "", "", ""),
	     Item("", "", "", "", "", "", "", "", "", ""), ]

    table = ItemTable(items)
    return render_template("template.html", **locals())

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=3331)
