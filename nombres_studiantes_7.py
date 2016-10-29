#!/usr/bin/python
import string as st
import sys
import os


def f_file_write(fileName, stringVar):
	fileTemp =open(fileName,'w')
	text=fileTemp.write(stringVar); fileTemp.close()

def f_file_read(fileName='micro1ro.txt'):
	if len(sys.argv[1:])!=0:
		try:
			fileTemp =open(fileName,"r")
			text=fileTemp.read(); fileTemp.close()
	else:
		fileTemp =open(fileName,"r")
		text=fileTemp.read(); fileTemp.close()
	return text


def testLdapadmin(nameVar, testVar='exist login?'):	
	if testVar=='exist user?':
		if not int(str(os.system("ldapadmin -s -F sn="+nameVar+" | grep 'sn:'"))):
			return 1
		else:
			return 0

	if testVar=='exist login?':
		if int(str(os.system("ldapadmin -s -F cn="+nameVar+" | grep 'cn:'"))):
			return 1
		else:
			return 0

def functFixExistentLogin(loginVar):	
	proveResult=testLdapadmin(loginVar)
	loginVarFixed=loginVar

	if proveResult:
		while testLdapadmin(loginVarFixed):
			if not loginVarFixed[-1] in st.digits:
				loginVarFixed=loginVarFixed+'1'
			else:
				loginVarFixed=loginVarFixed[0:-1]+str(int(loginVarFixed[-1])+1)
	else:
		loginVarFixed=loginVar

	return loginVarFixed



def functionName2Login(listNameSepVar):
	if len(listNameSepVar[-2])>2:
		login=st.lower(listNameSepVar[0][0]+listNameSepVar[-2])
	else:
			if len(listNameSepVar[-3])>2:
				login=st.lower(listNameSepVar[0][0]+listNameSepVar[-3])
			else:
				login=st.lower(listNameSepVar[0][0]+listNameSepVar[-4])
	return login


def functLoginNameUsers( listNameVar, varReturn='list' ):

	if varReturn=='list':
		listLoginName=map(lambda student: functFixExistentLogin(functionName2Login(student)), listNameVar)
		# print listLoginName
		return listLoginName

	if varReturn=='dict':
		dictioLoginName=dict((st.join(name,sep=' '), functFixExistentLogin(functionName2Login(name))) for name in listNameVar)
		# print dictioLoginName
		return dictioLoginName


def main():

	fileContent=f_file_read()
	listNameStud=st.split(fileContent, sep='\n')
	
	listRepeatedUsers=[ student for student in listNameStud if testLdapadmin(student, 'user exist?')]
	listRealNewUsers=[ student for student in listNameStud if not testLdapadmin(student, 'user exist?')]
	
	listNameStudSplitted=[st.split(student, sep=' ') for student in listRealNewUsers]

	print functLoginNameUsers(listNameStudSplitted,'dict')
	# print functLoginNameUsers(listNameStudSplitted,'dict').keys()
	
	f_file_write('salidaLoginPython.txt', st.join(functLoginNameUsers(listNameStudSplitted,'dict').keys(),sep='\n' ))


if __name__ == '__main__':
	main()



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







