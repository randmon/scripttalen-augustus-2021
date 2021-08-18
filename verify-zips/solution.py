import zipfile

for i in range(100):
    j = str(i).rjust(3, "0")
    zip = zipfile.ZipFile(f'data\sub{j}.zip')
    files = zip.namelist()
    if len(files) != 3 or 'file-a' not in files or 'file-b' not in files or 'file-c' not in files:
        print(f'sub{j}.zip')
#fdbeb615dab3648016a5de42b9