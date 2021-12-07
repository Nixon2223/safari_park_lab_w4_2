from db.run_sql import run_sql

from models.animal import Animal
from models.staff import Staff

def save(animal):
    sql = "INSERT INTO animals (name, type, staff_id) VALUES (%s, %s, %s) RETURNING *"
    values = [animal.name, animal.type, animal.staff]
    results = run_sql(sql, values)
    id = results[0]['id']
    animal.id = id
    return animal


def select_all():
    animal_list = []

    sql = "SELECT * FROM animals"
    results = run_sql(sql)

    for row in results:
        animal = Animal(row['name'], row['type'], row['staff_id'], row['id'] )
        animal_list.append(animal)
    return animal_list


def select(id):
    animal = None
    sql = "SELECT * FROM animals WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        animal = Animal(result['name'], result['type'], result['staff_id'], result['id'] )
    return animal


def delete_all():
    sql = "DELETE  FROM animals"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM animals WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(animal):
    sql = "UPDATE animals SET (name, type, staff_id ) = (%s, %s, %s WHERE id = %s"
    values = [animal.name, animal.type, animal.staff_id, animal.id]
    run_sql(sql, values)

def animals(staff):
    tasks = []

    sql = "SELECT * FROM animals WHERE staff_id = %s"
    values = [staff.id]
    results = run_sql(sql, values)

    for row in results:
        task = Animal(row['name'], row['staff_id'], row['type'], row['id'] )
        tasks.append(task)
    return tasks