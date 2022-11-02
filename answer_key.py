###########################################################################################
# This code provides introductory examples for using genomic data in Python.              #
# Make sure that the provided data is in the './data' directory.                          #
# Joshua L. Mincer 10/31/2022                                                             #
###########################################################################################

#Read in a file. 
data = []
with open("./data/example.vcf") as file:
    for line in file:
        print(line.split("\t"))