employee = [
    {"name": 'Steve', "gender" : 'male', "hobbies" : ['Video games', 'Football']},
    {"name": 'Lina', "gender" : 'female', "hobbies" : ['Shop', 'Cook']},
    {"name": 'Reynald', "gender" : 'male', "hobbies" : ['Run', 'Hide', 'Jump']}
]



for i in range(0,len(employee)):
    if employee[i]["gender"] == 'male' :
        nama = employee[i]["name"]
        kelamin = 'Mr'
        jmlHobi = len(employee[i]["hobbies"])
        hobi = ','.join(employee[i]["hobbies"])
        print(f'{kelamin} {nama} has {jmlHobi} hobbies, they are {hobi}.')
    else :
        nama = employee[i]["name"]
        kelamin = 'Ms'
        jmlHobi = len(employee[i]["hobbies"])
        hobi = ','.join(employee[i]["hobbies"])
        print(f'{kelamin} {nama} has {jmlHobi} hobbies, they are {hobi}.')










