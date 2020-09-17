
course = "Python's Course for \"Beginners\""
print(course)
print("normal [index] indexing: "+ course[0])

# Positive Indizes: [0, n-1]
# Negative Indizes: [-1, -n] Fangen vom Ende des Strings an.
print("negative index indexing: " + course[-1])
print(course[-len(course)])

print(course[1:3])            # Nimmt alle chars von course, die von Index 1 bis Index 3 gehen. Index 1 eingeschlossen und Index 3 ausgeschlossen.
print(course[1:])             # Lässt man den zweiten Index weg, wird dieser als len(course) angenommen.
print(course[:len(course)-1]) # Lässt man den ersten Index weg, wird dieser als 0 angenommen.
print(course[:])              # Lässt man beide Indizes weg, werden diese als 0:len(course) angenommen.

multi_line_string = '''

Das ist 
ein String,
der über mehrere Zeilen geht.

'''
print(multi_line_string)

name = "Jennifer"
print(name[1:-2]) # Fängt beim ersten char an. Geht bis zum vorletzten, schließt diesen aber aus.