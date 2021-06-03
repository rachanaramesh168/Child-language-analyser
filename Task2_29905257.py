'''
Student ID: 29905257
Name: Rachana Ramesh
Start Date: 26th September 2018
End Date: 8th October 2018
Last Modified Date: 11th October 2018
This program reads the cleaned TD and SLI datasets from the folder
(Folder name: D:\Python - 29905257)
and computes the total of the following:
* length of the transcript - Identified by the counting statements that ends with '.','?' and '!'.
* Size of the vocabulary - Identified by counting unique words of each file and summing it up for TD and SLI group
* Number of repetition words - Identified by counting [/]
* Number of retracing words - Identified by counting [//]
* Number of grammatical errors - Identified by counting [* m] and [* m:+ed]
* Number of pauses - Identified by counting (.)

The class Analyser is declared with __init__, __str__, stat_list and analyse_script methods.
* The __init__ method initialises the variables
* The __str__ method prints the final statistics in the required format
* The stat_list method performs the summation of values and stores in a list
* The analyse_script method performs the computation of values
'''
import os


class Analyser:
    def __init__(self):
        self.length = []
        self.vocab_size = []
        self.rep_words = []
        self.ret_words = []
        self.gram_err = []
        self.pause = []
        self.stat = [0] * 6

    def __str__(self):  # Formatting the string in a required format

        statistics_details = "Length of the transcript     : " + str(self.stat[0]) + "\n" +\
                             "Size of the vocabulary       : " + str(self.stat[1]) + "\n" +\
                             "Number of repetition words   : " + str(self.stat[2]) + "\n" +\
                             "Number of retracing words    : " + str(self.stat[3]) + "\n" +\
                             "Number of pauses             : " + str(self.stat[4]) + "\n" +\
                             "Number of grammatical errors : " + str(self.stat[5]) + "\n"

        return statistics_details

    def stat_list(self):  # computing the total of each statistic values

        self.stat[0] = sum(self.length)
        self.stat[1] = sum(self.vocab_size)
        self.stat[2] = sum(self.rep_words)
        self.stat[3] = sum(self.ret_words)
        self.stat[4] = sum(self.pause)
        self.stat[5] = sum(self.gram_err)

        return self.stat

    def analyse_script(self, path, file):
        self.path = path
        self.file = file
        statement_count = 0
        repeat = 0
        retrace = 0
        pauses = 0
        errors = 0
        size = set()
        vocab_count = 0
        punctuations = {"[/]", "[//]", "(.)", ".", "[*", "m:+ed]", "?", "..", "!", "...", "m]"}

        file_path = os.path.join(path, file)
        if os.path.exists(file_path):  # Checking if the directory is empty
            if file.endswith(".txt"):
                if os.path.getsize(file_path) > 0:  # Checking if the file is empty
                    with open(file_path, "r") as infile:
                        for line in infile.readlines():
                            if line.endswith(".\n") or line.endswith("?\n") or line.endswith("!\n")\
                                    or line.endswith(". \n"):
                                statement_count +=1      # count of Length of the statements
                            repeat += line.count("[/]")  # count of repeat words
                            retrace += line.count("//")  # count of retrace words
                            pauses += line.count("(.)")  # count of pauses
                            errors += line.count("[* ")  # count of errors
                            size.update(line.split())    # unique words for counting size
                            size = size - punctuations   # omitting the punctuations in counting unique words

                        vocab_count = len(size)              # Count of unique words
                        self.length.append(statement_count)
                        self.rep_words.append(repeat)
                        self.ret_words.append(retrace)
                        self.pause.append(pauses)
                        self.gram_err.append(errors)
                        self.vocab_size.append(vocab_count)
                    infile.close()

                else:
                    print("This file is empty", file_path)
            else:
                print("Not a text file", file_path)
        else:
            print("No files exist in this path!!!!")


def main():
    td_path = "D:/Python - 29905257/TD_Cleaned"
    sli_path = "D:/Python - 29905257/SLI_Cleaned"

    td = Analyser()

    if os.path.isdir(td_path):  # Checking if the path provided for TD cleaned dataset is a valid path
        for file in os.listdir(td_path):
            td.analyse_script(td_path, file)
            td.stat_list()
        print("Statistics for Typically Developed Children:-\n")
        print(td)
    else:
        print("Invalid path for TD. Please give the correct path to access the cleaned datasets!!")

    sli = Analyser()

    if os.path.isdir(sli_path):  # Checking if the path provided for SLI cleaned dataset is a valid path
        for file in os.listdir(sli_path):
            sli.analyse_script(sli_path, file)
            sli.stat_list()
        print("Statistics for Specific Language Impairment Children:-\n")
        print(sli)
    else:
        print("Invalid path for SLI. Please give the correct path to access the cleaned datasets!!")


if __name__ == '__main__':
    main()
