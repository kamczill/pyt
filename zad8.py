
file1 = open('plik.txt', "w+")
file1.writelines("""
    Hello,
    To jest przykladowy
    tekst
    ktory sprawdza program
    
    """)
file1.seek(0)
print(file1.read())
file1.close()