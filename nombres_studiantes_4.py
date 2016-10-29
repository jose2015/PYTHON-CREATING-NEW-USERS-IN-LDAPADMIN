#!/usr/bin/python
import string as st
import sys
import os


def f_file_write(fileName, stringVar):
	""" This is  a method to open in write mode a single file and it write 
	the content on the string. """
	fileTemp =open(fileName,'w')
	text=fileTemp.write(stringVar); fileTemp.close()

def f_file_read(fileName='micro1ro.txt'):
	""" This is  a method to open in read mode a single file and return the 
	content of the file after we close it. """
	fileTemp =open(fileName,"r")
	text=fileTemp.read(); fileTemp.close()
	return text

def functionName2Login(listNameSepVar):
	if len(listNameSepVar[-2])>2:
		login=st.lower(listNameSepVar[0][0]+listNameSepVar[-2])
	else:
			if len(listNameSepVar[-3])>2:
				login=st.lower(listNameSepVar[0][0]+listNameSepVar[-3])
			else:
				login=st.lower(listNameSepVar[0][0]+listNameSepVar[-4])
	return login

def functionLoginNameUsers( listNameVar, varReturn='list' ):
	listLoginName=map(lambda student: functionName2Login(student),listNameVar)

	# print listLoginName
	if varReturn=='list':
		return listLoginName

	if varReturn=='dict':
		dictioLoginName=dict((functionName2Login(name), name) for name in listNameVar)
		return dictioLoginName



def testLdapadmin(loginVar, userName='nadie'):	
	if userName!='nadie' and not int(str(os.system("ldapadmin -s -F sn="+username+" | grep 'sn:'"))):
		return None
	else:
		if int(str(os.system("ldapadmin -s -F cn="+loginVar+" | grep 'cn:'"))):
			return 1
		else:
			return 0


def proveExistenceLogin(loginVar, userNameVar='nadie'):
	
	loginVarFixed=loginVar
	proveResult=os.system('/root/codigos/chequeaUname.sh'+loginVar)
	if proveResult:
		while os.system('/root/codigos/chequeaUname.sh '+loginVarFixed):
			if not loginVarFixed[-1] in st.digits:
				loginVarFixed=loginVarFixed+'1'
				# return loginVarFixed
			else:
				loginVarFixed=loginVarFixed[0:-1]+str(int(loginVarFixed[-1])+1)
				# return loginVarFixed
	else:
		if proveResult==None:
			loginVar=None
			# return loginVarFixed
		else:
			loginVarFixed=loginVar
	return loginVarFixed

def main():

	fileContent=f_file_read()
	listNameStud=st.split(fileContent, sep='\n')
	listNameStudSplitted=[st.split(student,sep=' ') for student in listNameStud]

	# print functionLoginNameUsers(listNameStudSplitted)
	# listTemp=[]
	# for login in functionLoginNameUsers(listNameStudSplitted):
	# 	listTemp+=[proveExistenceLogin(login)]
	# print listTemp 

	# fileResult=open('salidaLoginPython.txt','w')
	# for login in listTemp:
	# 	fileResult.write(login)
	# fileResult.close()

if __name__ == '__main__':
	main()

# print listLoginName[33]
 # (int(str(os.system("ldapadmin -s -F cn="+userName+"| grep 'cn:'"))) or 
# for i in range(len(listLoginName)): 
# 	if listLoginName[i]=="mde":
# 		print str(i+1)+ listLoginName[i]
# listLoginName=map(lambda x: st.lower(x[0][0]+x[-2]),listNameStudSplitted)

# [["",",","",""],["","",""],["","",""]]

# listNameLastName=map(lambda student: map(lambda x:[x[0]]+[x[-2]],student),listNameSecNameSplited)
# """ ldapadmin -s -F cn=jfuentes | grep 'cn:'"""

# def fRead(fileName):fileTemp=open(fileName,"r");text=fileTemp.read();fileTemp.close();return text


# ----------------------------------------------------------------------------------
# Name: creaUsersEmail.py
# Author: Jose Manuel Alonso
# 
# History: Created 20 Oct 2016
# 	           20 Oct.  2016
# Python script file for create login data of email. 
#
# Facultad de Fisica (FF)
# Universidad de la Habana
#
# Copyright (C) 2016 by Jose Manuel Alonso Tejera   
# jmalonso@estudiantes.fisica.uh.cu
# 
# This program is free software; you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation; either version 2 of the License, or     
# (at your option) any later version.                                   
#                                                                         
#  This program is distributed in the hope that it will be useful,       
#  but WITHOUT ANY WARRANTY; without even the implied warranty of        
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         
#  GNU General Public License for more details.                          
#                                                                         
#  You should have received a copy of the GNU General Public License     
#  along with this program; if not, write to the                      
#  Free Software Foundation, Inc.,                                       
#  59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.             
# 
# -----------------------------------------------------------------------------------






