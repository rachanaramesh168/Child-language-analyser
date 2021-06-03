'''
Student ID: 29905257
Name: Rachana Ramesh
Start Date: 26th September 2018
End Date: 8th October 2018
Last Modified Date: 11th October 2018
This program reads the TD and SLI datasets from the folder
(Folder name: D:\Python - 29905257\Assignment 2\ENNI Dataset-20180920\ENNI Dataset)
and extracts the *CHI statements with filters listed below:
* Removes angular brackets < >
* Removes common parenthesis except (.)
* Removes statements present inside [] except [/], [//] , [* m:+ed] and [* m]
* Removes words starting with + and &
The cleaned files are present in the folder (folder name: D:\Python - 29905257)
for TD and SLI correspondingly.
The function pre_processing does the above functions.
The main function checks if the folder exists and if exists calls the pre_processing function
'''
import os


def pre_processing(path, file, count):
    list_of_statements = []
    list_rm_sp = []
    list_split_words = []
    list_words_final = []
    temp = ''
    list_to_string = ""
    chk_flag = False
    result = ''

    file_path = os.path.join(path, file)
    if os.path.exists(file_path):                 # Checking if the directory is empty
        if file_path.endswith(".txt"):   # Performs following operation if text file else prints not a txt file
            if os.path.getsize(file_path) > 0:    # Checking if the file is empty
                with open(file_path, "r") as infile:
                    for line in infile.readlines():
                        start = line.find("[^ ")   # Removing examiner statements in Child statement line
                        end = line.find("]", start)
                        if start > 0 and end > 0:
                            result = line[start:end + 1]
                            line = line.replace(result, '')

                # Loop to remove words followed by '&'

                        for i in line:
                            char_amb_st = line.find("&")
                            char_amb_nd = line.find(" ",char_amb_st)
                            if char_amb_st > 0 and char_amb_nd > 0:
                                amb_word = line[char_amb_st:char_amb_nd +1]
                                line = line.replace(amb_word, '')

                        if '%mor' in line:                  # Condition to append the 2 line *CHI lines
                            chk_flag = False
                            list_of_statements.append(temp)
                            temp = ''
                        if '*EXA' in line:          # Condition to append *CHI line which is followed by *EXA
                            chk_flag = False
                            list_of_statements.append(temp)
                            temp = ''
                        if chk_flag and not '*CHI' in line:  # Condition to append *CHI statements followed in
                            line = line.replace('\n', '')    # the second line
                            line = line.replace('\t', '')
                            line = line.replace('<', '')
                            line = line.replace('>', '')
                            temp += ' ' + line
                            list_of_statements.append(temp)
                            temp = ''
                        elif not chk_flag and '*CHI' in line:  # Condition to append *CHI line
                            chk_flag = True
                            line = line.replace('\n', '')
                            line = line.replace('\t', '')
                            line = line.replace('<', '')
                            line = line.replace('>', '')
                            temp += line[5:]
                        elif chk_flag and '*CHI' in line:      # Condition to append back to back *CHI lines
                            list_of_statements.append(temp)
                            temp = ''
                            line = line.replace('\n', '')
                            line = line.replace('\t', '')
                            line = line.replace('<', '')
                            line = line.replace('>', '')
                            temp += line[5:]

                for item in list_of_statements:  # loop to remove space added in previous filter
                    if item != '':
                        list_rm_sp.append(item)

                for item in list_rm_sp:          # loop to split each statement into words.
                    item = item.split()
                    list_split_words.append(item)  # This contains list of statements and each statement
                                                    # is a list item split into words.
                for item in list_split_words:   # Removing words that starts with [ or ends with ] thus omitting
                    for i in item:              # words like [+ bch], [!] and retaining special character words
                        if "[" in i and i not in ("[//]", "[/]", "[*]", "[*", "m:+ed]", "m]"):
                            s = i.find("[")
                            r = i[s:]
                            i = i.replace(r, '')
                            list_words_final.append(i)
                        elif not (i.startswith("[") or i.endswith("]")):  # retaining words that does not start or
                            list_words_final.append(i)                    # end with [ or ].
                        elif i in ("[//]", "[/]", "[*]", "[*", "m:+ed]", "m]"):
                            list_words_final.append(i)

                for n, item in enumerate(list_words_final):  # Loop to add end of each statement with new line
                    if item in ('.','!','?'):                # so as to print each statement line by line
                        list_words_final[n] = item+"\n"

                    if item.__contains__("(") or item.__contains__(")"):  # Replacing common parenthesis except
                        if item not in ("(.)"):                           # '(.)'
                            item = item.replace("(","")
                            item = item.replace(")","")
                            list_words_final[n] = item

                    if item.startswith('+') and item.endswith('.'):  # removal of word starting with +. Since the
                        st = item.find("+")                      # datasets have words that starts with '+'
                        en = item.find(".", st)                  # and ends with '.' such as +..., +/. and +//.
                        res = item[st:en]                        # so removing the whole word. In many places the
                        item = item.replace(res, '\n')           # word starting with + is end of line so taking
                        list_words_final[n] = item               # '.' as end of word

                    list_to_string = " ".join(list_words_final)

                if file.startswith("TD"):              # Printing TD cleaned files in a directory
                    if os.path.exists("D:/Python - 29905257/TD_Cleaned"):
                        os.chdir("D:/Python - 29905257/TD_Cleaned")
                    else:
                        os.makedirs("D:/Python - 29905257/TD_Cleaned")
                        os.chdir("D:/Python - 29905257/TD_Cleaned")

                    opfile = open("TD_Cleaned" + str(count) + ".txt", "w")
                    opfile.writelines(list_to_string)
                    opfile.close()

                if file.startswith("SLI"):              # Printing SLI cleaned files in a directory
                    if os.path.exists("D:/Python - 29905257/SLI_Cleaned"):
                        os.chdir("D:/Python - 29905257/SLI_Cleaned")
                    else:
                        os.makedirs("D:/Python - 29905257/SLI_Cleaned")
                        os.chdir("D:/Python - 29905257/SLI_Cleaned")

                    opfile = open("SLI_Cleaned" + str(count) + ".txt", "w")
                    opfile.writelines(list_to_string)
                    opfile.close()
                infile.close()
            else:
                print("This file is empty: ", file_path)
        else:
            print("Not a text file!", file_path)  # Prints the file name if it is not a text file
    else:
        print("No files exist in this path!!!!")


def main():
    td_path = "D:/Python - 29905257/Assignment 2/ENNI Dataset/TD"
    sli_path = "D:/Python - 29905257/Assignment 2/ENNI Dataset/SLI"
    count = 0

    if os.path.isdir(td_path):   # Checking if the path provided for TD dataset is a valid path
        for file in os.listdir(td_path):
            pre_processing(td_path, file, count)
            count += 1
    else:
        print("Invalid path for TD. Please give the correct path to access the datasets!!")

    count = 0
    if os.path.isdir(sli_path):   # Checking if the path provided for SLI dataset is a valid path
        for file in os.listdir(sli_path):
            pre_processing(sli_path, file, count)
            count += 1
    else:
        print("Invalid path for SLI. Please give the correct path to access the datasets!!")


if __name__ == '__main__':
    main()
