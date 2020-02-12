employee = [
    {"name": 'Steve', "gender" : 'male', "hobbies" : ['Video games', 'Football']},
    {"name": 'Lina', "gender" : 'female', "hobbies" : ['Shop', 'Cook']},
    {"name": 'Reynald', "gender" : 'male', "hobbies" : ['Run', 'Hide', 'Jump']}
]

for i in employee:
    # i = {"name", "gender", "hobbies"}
    # Jika gendernya adalah laki laki, tambahkan kata Mr.
    # Jika bukan, tambahkan kata Mrs.
    if i["gender"] == 'male':
        i["name"] = 'Mr.' + i["name"]
    else :
        i["name"] = 'Mrs.' + i["name"]

    name = i["name"]
    # Menggabungkan semua data pada list menggunakan ", "
    hobbies = ", ".join(i["hobbies"])
    # Mencari tahu jumlah hobby yang dimiliki
    lenHob = len(i["hobbies"])

    print(
        f'{name} has {lenHob} hobbies, they are {hobbies}'
    )
