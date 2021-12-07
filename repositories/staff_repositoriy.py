from db.run_sql import run_sql

from models.staff import Staff


def save(staff):
    sql = "INSERT INTO tasks (name, start_date, department) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [staff.name, staff.start_date, staff.department, staff.performance]
    results = run_sql(sql, values)
    id = results[0]['id']
    staff.id = id
    return staff


def select_all():
    tasks = []

    sql = "SELECT * FROM tasks"
    results = run_sql(sql)

    for row in results:
        staff = Staff(row['name'], row['start_date'], row['department'], row['performance'], row['id'] )
        tasks.append(staff)
    return tasks


def select(id):
    staff = None
    sql = "SELECT * FROM tasks WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        staff = Staff(result['name'], result['start_date'], result['department'], result['performance'], result['id'] )
    return staff


def delete_all():
    sql = "DELETE  FROM tasks"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM tasks WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(staff):
    sql = "UPDATE tasks SET (name, , start_date, department) = (%s, %s, %s, %s) WHERE id = %s"
    values = [staff.name, staff.start_date, staff.department, staff.performance, staff.id]
    run_sql(sql, values)