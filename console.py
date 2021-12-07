import pdb
from models.staff import Staff
from models.animal import Animal

import repositories.staff_repository as staff_repository
import repositories.animal_repository as animal_repository

animal_repository.delete_all()
staff_repository.delete_all()


staff1 = Staff("staff 1", "2015-01-12", "dep 1", 0)
staff_repository.save(staff1)
staff2 = Staff("staff 2", "2014-05-22", "dep 2", 5)
staff_repository.save(staff2)

staff1 = Staff("staff 1", "2015-01-12", "dep 1", 1, staff1.id)
staff_repository.update(staff1)

animal1 = Animal("animal1", "type1", staff1.id)
animal_repository.save(animal1)

staff_repository.delete(staff2.id)

staff_repository.select_all()
staff_repository.select(staff1.id)
animal_repository.animals(staff1)

pdb.set_trace()