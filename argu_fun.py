def greet(country="india"):
    print("hello from " + country)
greet("India")
greet()

def greterNum(*number):
    print("greater number is", max(number))
greterNum(1, 3, 2)

def full_name(fname, Iname):
    print(fname + " " + Iname)
full_name("Sneha", "Jadhav")

def introduce(**info):
    print("My name is " + info["name"] + " and I am from " + info["city"])
introduce(name="Sneha", city="Phaltan")

def student_info(**details):
    print("Student name is " + details["fname"] + " " + details["Iname"])
student_info(fname="Sneha", Iname="Jadhav")

def address(city, state):
    print("I live in " + city + ", " + state)
address("Phaltan", "Maharashtra")