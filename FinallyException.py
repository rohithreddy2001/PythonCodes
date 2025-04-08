def process_file():
   try:
       f = open(r"C:\Users\rohit\OneDrive\Documents\Cricket Data Analysis.txt")
       x = 1/0

   except FileNotFoundError as e:
       print("File not found")

   except ZeroDivisionError as e:
       print("Zero Division Error")

   finally:
       print("cleaning up file")
       f.close()

process_file()

