person={
        
        "name":"Farhana Akter",
            
        "address":"MAsterpara,Feni",
                
        "varsity":"CUET",
        
        "age":22,
    
        
        }

print(type(person))

print(person["name"])
print(person["age"])
person["phone"]="0186686"
print(person
      )

print(person.keys())

print(person.values())

print(person.items())

person2=person.copy()

print(person2)


del(person['age'])
print(person)

person.clear()
print(person)

print(len(person))


lis2=[
      
      {
           "name":"Farhana Ripa",
           "age":22
       
       },
       {
        "name":"abul kalam",
        "status":"Father"
        
        }
     
      ]

print(lis2[1])

print(lis2[1]["name"])

print(lis2[0]["name"])

