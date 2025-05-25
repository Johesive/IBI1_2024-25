#use os to change the directory to the current directory
#import datetime to get the current time, record the time when parsing starts and ends, and calculate the duration
#overall variables:
#term_namespace:molecular_function, biological_process, cellular_component
#term_name: the name of the term
#is_a_count: the number of is_a tags


#import xml.dom.minidom to parse the XML file with DOM
#create a list with tage name 'term': collection = DOMTree.documentElement, terms = collection.getElementsByTagName('term')
#create a dictionary to store three namespaces and their terms list with correspondingis_a count:{"molecular_function":([], 0), "biological_process":([], 0), "cellular_component":([], 0)}
#loop through the terms in the XML file
#if the is_a count is greater than the current maximum count, update the dictionary with the new term and is_a count
#if the is_a count is equal to the current maximum count, append the new term to the list of terms with the same is_a count
#print the term lists and their is_a count

#use xml.sax to parse the XML file with SAX
#following the practical instructions, create a class to handle the events of the XML file: 
#def __init__(self), def startElement(self, tag, attributes), def characters(self, content), def endElement(self, tag)
#create an identical dictionary as the DOM parser
#use the same if and elif statements to update the dictionary
#print the GO terms and their is_a count

#compare the time taken by the DOM and SAX parsers and print the faster one: SAX parser is faster.

import os
os.chdir("C:\\Users\\15041\\IBI1_2024-25\\Practical14")

import datetime


import xml.dom.minidom

DOM_start_time = datetime.datetime.now()

DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName('term')

count = {"molecular_function":([], 0), "biological_process":([], 0), "cellular_component":([], 0)}

for term in terms:
    term_namespace = term.getElementsByTagName('namespace')[0].firstChild.nodeValue
    term_name = term.getElementsByTagName('name')[0].firstChild.nodeValue
    is_a_list = term.getElementsByTagName('is_a')
    is_a_count = len(is_a_list)
    current_terms, current_max_count = count[term_namespace] #customize the dictionary with the current namespace and its current terms and is_a count

    if is_a_count > current_max_count:
        count[term_namespace] = ([term_name], is_a_count)
    elif is_a_count == current_max_count:
        current_terms.append(term_name)
    
for term_namespace, (term_name, is_a_count) in count.items():
    print(f"{term_namespace}:\nGO term:{term_name}\nis_a count:{is_a_count}")

DOM_end_time = datetime.datetime.now()
print(f"Time taken: {DOM_end_time - DOM_start_time}")


import xml.sax

SAX_start_time = datetime.datetime.now()

class termsHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_data = ""
        self.term_namespace = ""
        self.term_name = ""
        self.is_a_count = 0
        self.count = {"molecular_function":([], 0), "biological_process":([], 0), "cellular_component":([], 0)}

    def startElement(self, tag, attributes):
        self.current_data = tag
        if tag == "term":
            self.term_namespace = ""
            self.term_name = ""
            self.is_a_count = 0 #is_a count is a number

    def characters(self, content):
        if self.current_data == "namespace":
            self.term_namespace += content.strip()
        elif self.current_data == "name":
            self.term_name += content.strip()
        elif self.current_data == "is_a":
            self.is_a_count += 1
    
    def endElement(self, tag):
        if tag == "term":
            if self.term_namespace in self.count:
                current_terms, current_max_count = self.count[self.term_namespace]
                if self.is_a_count > current_max_count:
                    self.count[self.term_namespace] = ([self.term_name], self.is_a_count)
                elif self.is_a_count == current_max_count:
                    current_terms.append(self.term_name)

        self.current_data = "" #reset the current data


parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
Handler = termsHandler()
parser.setContentHandler(Handler)
parser.parse('go_obo.xml')

for term_namespace, (term_name, is_a_count) in Handler.count.items():
    print(f"{term_namespace}:\nGO term:{term_name}\nis_a count:{is_a_count}")

SAX_end_time = datetime.datetime.now()
print(f"Time taken: {SAX_end_time - SAX_start_time}")

# The SAX parser is faster than the DOM parser for large XML files.