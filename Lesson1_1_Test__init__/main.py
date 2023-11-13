#1
from Lesson1_1_Work_with_packages import Allow
#2
#ImportError: cannot import name 'Restrict' from 'Lesson1_1_Work_with_packages'
#from Lesson1_1_Work_with_packages import Restrict
#3
import Lesson1_1_Work_with_packages
#1 Example
allow = Allow()
print(allow.AllowedFunction())
#3 AttributeError: module 'Lesson1_1_Work_with_packages' has no attribute 'Restrict'
restrict = Lesson1_1_Work_with_packages.Restrict()
print(restrict.RestrictedFunction())

#4 An example that can serve as a foundation for a project oriented towards the Domain-Driven Design (DDD) system.
'''
#lua
my_project/
|-- my_project/
|   |-- __init__.py
|   |-- main.py
|   |-- databasecontext/
|   |   |-- __init__.py
|   |   |-- database.py
|   |-- logger/
|   |   |-- __init__.py
|   |   |-- logger.py
|   |-- business_logic/
|       |-- __init__.py
|       |-- service.py
|-- tests/
    |-- __init__.py
    |-- test_database.py
    |-- test_logger.py
    |-- test_service.py
|-- requirements.txt
'''

'''
Domain-Driven Design (DDD) is an approach to software development that emphasizes the importance of understanding 
and modeling the business domain. 
It was introduced by Eric Evans in his book "Domain-Driven Design: Tackling Complexity in the Heart of Software."
In DDD, the core idea is to focus on the business domain and its logic, making sure that the software model closely 
reflects the real-world processes and concepts. 
It encourages collaboration between domain experts and software developers to create a shared understanding 
of the problem domain.

Key concepts and patterns in DDD include:
Ubiquitous Language: Establishing a common, shared language between developers and domain experts to ensure 
                     a consistent understanding of the business domain.
Bounded Contexts: Defining clear boundaries for different parts of the system to manage complexity 
                  and avoid ambiguity in terms and concepts.
Entities and Value Objects: Modeling domain entities (objects with distinct identities) 
                            and value objects (objects without identity, defined by their attributes) 
                            to represent business concepts.
Aggregates: Grouping related entities and value objects into aggregates, defining rules for consistency 
            and ensuring data integrity.
Repositories: Providing a mechanism for accessing and storing domain objects, abstracting away the details of data storage.
Services: Introducing domain services to handle operations that don't naturally fit into the responsibilities of entities 
          or value objects.
Domain Events: Capturing and responding to significant changes in the domain by using events.
Overall, Domain-Driven Design aims to create software that not only meets technical requirements but also aligns closely 
with the business needs and goals. It helps in building more maintainable, understandable, and adaptable systems.
'''