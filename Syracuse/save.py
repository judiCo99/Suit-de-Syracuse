# By judi_Co
author = "judi_Co"

import yaml
import json

#===============================

# SET VALU 
def YamlSet(Dic,File):
	LoadDataYaml = YamlLoad(File)
	LoadDataYaml.update(Dic)
	yaml_file = open(File, 'w')
	yaml.safe_dump(LoadDataYaml, yaml_file)

#CRUCH
def JsonSet(Dic,File):
	LoadDataJson = JsonLoad(File)
	LoadDataJson.update(Dic)
	json_file = open(File, 'w')
	json.dump(LoadDataJson, json_file)

#===============================
# CHECK si le file et vide ou ineistent on le set avec "{}" de dent
# si la variable nexiste pas

def YamlCheck():
	pass

def JsonCheck():
	pass

#===============================
# Remove

def YamlRemove(Dic,File):
	LoadDataYaml = YamlLoad(File)

	for Clef, Value in Dic.items():
		
		if type(Value) == list:
			x = []
			for i in range(len(Dic[Clef])):
				x.append(LoadDataYaml[Clef].index(Dic[Clef][0]))
				del Dic[Clef][0]
			for i in range(len(x)):
				if i == 0:
					del LoadDataYaml[Clef][x[0]]
					del x[0]
				else:
					x[0] += -1
					del LoadDataYaml[Clef][x[0]]
					del x[0]

		elif type(Value) == dict:
			dell = {}
			dell.update(Dic[Clef].items())
			for Clef1, Value1 in dell.items():
				del LoadDataYaml[Clef][Clef1]

		elif type(Value) == str or int or float:
			del LoadDataYaml[Clef]

	yaml_file = open(File, 'w')
	yaml.safe_dump(LoadDataYaml, yaml_file)

def JsonRemove(Dic,File):
	LoadDataJson = JsonLoad(File)

	for Clef, Value in Dic.items():
		
		if type(Value) == list:
			x = []
			for i in range(len(Dic[Clef])):
				x.append(LoadDataJson[Clef].index(Dic[Clef][0]))
				del Dic[Clef][0]
			for i in range(len(x)):
				if i == 0:
					del LoadDataJson[Clef][x[0]]
					del x[0]
				else:
					x[0] += -1
					del LoadDataJson[Clef][x[0]]
					del x[0]

		elif type(Value) == dict:
			dell = {}
			dell.update(Dic[Clef].items())
			for Clef1, Value1 in dell.items():
				del LoadDataJson[Clef][Clef1]


		elif type(Value) == str or int or float:
			del LoadDataJson[Clef]

	Json_file = open(File, 'w')
	json.dump(LoadDataJson, Json_file)

#===============================
# READ

def YamlLoad(File):
	yaml_file = open(File, 'r')
	yaml_content = yaml.safe_load(yaml_file)
	return yaml_content

def JsonLoad(File):
	read_file = open(File, "r")
	json_content = json.load(read_file)
	return json_content

#===============================

'''
maitre un loge pour indiquer si il y a une errore
'''

YamlFile = "dataYaml.yml"
JsonFile = "dataJson.json"
TestFile = "testFile.yml"

Dict = {"nom": "tibo", "prenom": "safon", "age": 19, "sexe": "homme", "situaction amoureur": "celib for ever","passtion": ["informatique","jeux video"],"test": {"Nom": "judi", "prenom": "co", "age": 22}}
DelDic = {"nom": "tibo","passtion": ["informatique"],"test":{"Nom":"judi","age": 22}}

#==========================================
#SET
#print(YamlSet(Dict,YamlFile))
#print(JsonSet(Dict,JsonFile))

#========================================== 
#Remove
#YamlRemove(DelDic,YamlFile)
#JsonRemove(DelDic,JsonFile)
#gérer les exeption  dans les liste si un input et inexistent

#==========================================
#LOAD
#print(YamlLoad(YamlFile))
#print(JsonLoad(JsonFile))



