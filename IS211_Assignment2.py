__author__ = 'Terence Jeremiah'


import urllib2
import logging
import argparse
import random
import datetime
import pprint

def main():

    def downloadData(url):
        get_url=urllib2.urlopen(url)
        return get_url

    def processData(contents):
        persondict={}
        csvFichier=csv.reader(contents)
        csvFichier.next()

        for t in csvFichier:
            try:
                t[2]=datetime.datetime.strptime(t[2], "%d/%m/%Y")
            except ValueError:
                numb=int(t[0])
                line=int(t[0])+1
                logger=logging.getLogger("assiment 2")
                logger.error("Error processing line#{} for ID #{}.".format(line,numb))
            persondict[int(t[0])]=(t[1],t[2])
        return persondict

    def displayPerson(id,personData):
        try:
            response = "Person #{idnum} is {name} with a birthday of {date}"
            print response.format(idnum=id,name=personData[id][0],date=personData[id][1])
        except KeyError:
            print "Error on Person ID."

    parser=argparse.ArgumentParser()
    parser.add_argument("--url", help="URL searching for files.")
    args=parser.parse_args()
    logging.basicConfig(filename="errors.log", level=logging.ERROR)

    if args.url:
        csvData=downloadData(args.url)
        personData=processData(csvData)
        msg="Enter  ID number. To exit press 0 or a negative number."

        while True:
            try:
                user=int(raw_input(msg))
            except ValueError:
                print "Try again please."
                continue
            if user > 0:
                displayPerson(user,personData)
            else:
                print "Thank You!!!"
    else:
        print "Enter correct URL."

if __name__ == '_main__':
main()

