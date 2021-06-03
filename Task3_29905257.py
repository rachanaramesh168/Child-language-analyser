'''
Student ID: 29905257
Name: Rachana Ramesh
Start Date: 26th September 2018
End Date: 8th October 2018
Last Modified Date: 11th October 2018
This program reads the cleaned TD and SLI datasets from the folder
(Folder name: D:\Python - 29905257)
and calls the method Analyse_script of Analyser class from Task2_29905257 to receive the statistics
and prints the dataFrame and computes average and prints a bar graph of the average of each statistic

The class Visualiser is declared with __init__, initial_func, compute_averages and visualise_statistics methods.
* The __init__ method receives the TD and SLI statistics and prints the dataFrame
* The initial_func method returns both the statistics in a tuple
* The compute_averages method computes the averages of each statistics individually
* The visualise_statistics method prints the bar graph
'''

import os
import Task2_29905257 as t2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Visualiser:
    def __init__(self, td, sli):

        self.header = ['Length of Transcripts', 'Size of Vocabulary', 'Repeat Words', 'Retrace Words',
                       'Number of Pauses', 'Grammar Errors']
        self.stats_td = []
        self.stats_sli = []
        self.td = td
        self.sli = sli

        # Storing TD and SLI stats in separate variables to print data frame
        for item in self.td:
            self.stats_td.append(item)

        for item in self.sli:
            self.stats_sli.append(item)

        # Combining both TD and SLI list into a dictionary
        data_dict = {'TD': self.stats_td, 'SLI': self.stats_sli}

        # Printing a dataframe for both TD and SLI values
        dataframe = pd.DataFrame(data_dict, self.header)
        print(dataframe)

        self.length = self.stats_td[0]
        self.vocab_size = self.stats_td[1]
        self.rep_words = self.stats_td[2]
        self.ret_words = self.stats_td[3]
        self.gram_err = self.stats_td[4]
        self.pause = self.stats_td[5]

        self.length = self.stats_sli[0]
        self.vocab_size = self.stats_sli[1]
        self.rep_words = self.stats_sli[2]
        self.ret_words = self.stats_sli[3]
        self.gram_err = self.stats_sli[4]
        self.pause = self.stats_sli[5]

    def initial_func(self):  # Method to return the values received in the init function
        return self.stats_td, self.stats_sli

    def compute_averages(self, stats):  # Method to compute average of statistics of TD and SLI individually
        avg_statistics = []

        length_avg = stats[0]/10
        size_avg = stats[1]/10
        rep_avg = stats[2]/10
        ret_avg = stats[3]/10
        gram_err_avg = stats[4]/10
        pause_avg = stats[5]/10

        avg_statistics.append(length_avg)  # The averages for each are stored in a list
        avg_statistics.append(size_avg)
        avg_statistics.append(rep_avg)
        avg_statistics.append(ret_avg)
        avg_statistics.append(gram_err_avg)
        avg_statistics.append(pause_avg)

        return avg_statistics

    def visualise_statistics(self, td, sli):    # Method for visualizing the data
                                                # Method is called with the average values computed in the
        td = td                                 # compute_averages method
        sli = sli

        x = np.arange(6)                        # arranging x-axis for evenly spaced values
        bar_width = 0.20

        # labels and adjusting x till it is centered and plotting bar graph for TD and SLI
        fig, ax = plt.subplots()
        td_graph = plt.bar(x, td, width=bar_width, color='green', zorder=2, label='TD Statistics')
        sli_graph = plt.bar(x + bar_width, sli, width=bar_width, color='purple', zorder=2, label='SLI Statistics')

        ax.set_xticks(x+bar_width/2)            # setting the bar width
        ax.set_xticklabels(self.header)         # Setting the x-axis labels
        ax.set_title('Graphical representation of mean difference between TD and SLI children',fontweight='bold')
        ax.set_xlabel('Statistics', fontweight='bold')
        ax.set_ylabel('Mean values', fontweight='bold')
        ax.legend()

        def label(rects, xpos='center'):        # function to print the values on the top of each bar
            xpos = xpos.lower()                 # normalize the case of the parameter
            ha = {'center': 'center', 'right': 'left', 'left': 'right'}
            offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}

            for rect in rects:
                height = rect.get_height()
                ax.text(rect.get_x() + rect.get_width() * offset[xpos], 1.01 * height,
                        '{}'.format(height), ha=ha[xpos], va='bottom')

        label(td_graph, "left")
        label(sli_graph, "right")
        plt.show()


def main():
    td_path = "D:/Python - 29905257/TD_Cleaned"
    sli_path = "D:/Python - 29905257/SLI_Cleaned"

    # Reading TD cleaned files and calling the Analyser function from Task2 to return the statistical values
    td = t2.Analyser()  # Instance for task2

    if os.path.isdir(td_path):  # Checking if the path provided for TD cleaned dataset is a valid path
        for file in os.listdir(td_path):
            td.analyse_script(td_path, file)
    else:
        print("Invalid path for TD. Please give the correct path to access the cleaned datasets!!")

    td_statistics = td.stat_list()

    # Reading SLI cleaned files and calling the Analyser function from Task2 to return the statistical values
    sli = t2.Analyser()

    if os.path.isdir(sli_path):  # Checking if the path provided for SLI cleaned dataset is a valid path
        for file in os.listdir(sli_path):
            sli.analyse_script(sli_path, file)
    else:
        print("Invalid path for SLI. Please give the correct path to access the cleaned datasets!!")

    sli_statistics = sli.stat_list()

    # Instance for the class Visualiser
    t3 = Visualiser(td_statistics, sli_statistics)

    # Receiving the statistics for both TD and SLI in a tuple and then allocating it separately
    statistics = t3.initial_func()
    t3_td = statistics[0]
    t3_sli = statistics[1]

    # Calling method to compute average for each TD child group's statistics
    td_final_statistics = t3.compute_averages(t3_td)

    # Calling method to compute average for each SLI child group's statistics
    sli_final_statistics = t3.compute_averages(t3_sli)

    # Calling method to visualize the statistics
    t3.visualise_statistics(sli_final_statistics, td_final_statistics)


if __name__ == '__main__':
    main()
