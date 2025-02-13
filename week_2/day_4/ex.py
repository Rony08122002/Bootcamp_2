#1

#2
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
data = json.loads(sampleJson)
salary = data["company"]["employee"]["payable"]["salary"]
data["company"]["employee"]["birth_date"] = "1990-05-15"
with open("updated_data.json", "w") as file:
    json.dump(data, file, indent=4)
print(f"the amount of the salery is {salary} US dollars.")