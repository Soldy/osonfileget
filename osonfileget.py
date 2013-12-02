# -*- coding: utf-8 -*-
"""
Created on Mon Dec 2 00:13:26 2013

@author: testa
"""

import os

def makehtml():
    htmlout = "<!DOCTYPE html><html>"
    htmlout += "</html>"    
    return htmlout

"""
headtaglist 

array['tag']

tag - s : 
tittle - page title
favicon - favico

"""
def makehead(headtaglist):
    headout = "<head><meta charset='UTF-8'>"
    headout = "<title>"+headtaglist['tittle']+"</title>"
    headout += "</head>"
    return headout

def scripthread(scriptdir, scriptlist):
    scriptreadout = "<script type='text/javascript'>"
    for oute in scriptlist:
        page_file = open(os.path.join(scriptdir,oute),'r')
        scriptplus = page_file.read()
        page_file.close()
        scriptreadout += scriptplus+"/n"
    scriptreadout += "</script>"
    return scriptreadout

def csshread(cssdir, csslist):
    cssreadout = "<style type='text/css'>"
    for oute in csslist:
        page_file = open(os.path.join(cssdir,oute),'r')
        cssplus = page_file.read()
        page_file.close()
        cssreadout += cssplus+"/n"
    cssreadout += "</style>"
    return cssreadoutt



def scriptread(scriptdir, scriptlist):
    scriptreadout = "<script type='text/javascript'>"
    for oute in scriptlist:
        page_file = open(os.path.join(scriptdir,oute),'r')
        scriptplus = page_file.read()
        page_file.close()
        scriptreadout += scriptplus+"/n"
    scriptreadout += "</script>"
    return scriptreadout

def cssread(cssdir, csslist):
    cssreadout = "<style type='text/css'>"
    for oute in csslist:
        page_file = open(os.path.join(cssdir,oute),'r')
        cssplus = page_file.read()
        page_file.close()
        cssreadout += cssplus+"/n"
    cssreadout += "</style>"
    return cssreadout


def bodyread(bodydir, bodylist):
    bodyreadout = "<body>"
    for oute in bodylist:
        page_file = open(os.path.join(bodydir,oute),'r')
        bodyplus = page_file.read()
        page_file.close()
        bodyreadout += bodyplus+"/n"
    bodyreadout += "</body>"
    return bodyreadout


def scriptbread(scriptdir, scriptlist):
    scriptreadout = "<script type='text/javascript'>"
    for oute in scriptlist:
        page_file = open(os.path.join(scriptdir,oute),'r')
        scriptplus = page_file.read()
        page_file.close()
        scriptreadout += scriptplus+"/n"
    scriptreadout += "</script>"
    return scriptreadout

def cssbread(cssdir, csslist):
    cssreadout = "<style type='text/css'>"
    for oute in csslist:
        page_file = open(os.path.join(cssdir,oute),'r')
        cssplus = page_file.read()
        page_file.close()
        cssreadout += cssplus+"/n"
    cssreadout += "</style>"
    return cssreadout