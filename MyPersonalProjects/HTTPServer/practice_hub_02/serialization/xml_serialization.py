import xml.etree.ElementTree as ET

person = ET.Element('Person')
name = ET.SubElement(person, 'Name')
name.text = 'Alice'
age = ET.SubElement(person, 'Age')
age.text = '30'

tree = ET.ElementTree(person)
tree.write('person.xml')

tree = ET.parse('person.xml')
root = tree.getroot()

print(root.tag)  # 'Person'
for child in root:
    print(child.tag, child.text)

'''
    Optional: Pretty Printing
    
        To write with indentation (human-readable format):
    
            import xml.dom.minidom

            xml_str = ET.tostring(person, encoding='unicode')
            pretty_xml = xml.dom.minidom.parseString(xml_str).toprettyxml()

            with open('person_pretty.xml', 'w') as f:
                f.write(pretty_xml)
                
        
        This would give you:

            xml

                <?xml version="1.0" ?>
                <Person>
                    <Name>Alice</Name>
                    <Age>30</Age>
                </Person>

'''


'''

import xml.etree.ElementTree as ET

    Imports the ElementTree module from Python’s standard library.

    ElementTree (commonly abbreviated ET) is used for creating, parsing, and modifying XML documents.

This module:

    Represents XML elements using Element objects.

    Allows you to build XML trees in memory and write them to files.
    
person = ET.Element('Person')

    Creates a root element named <Person>.

        This is like:

            xml

                <Person></Person>
                
ET.Element('Person') returns an object of type xml.etree.ElementTree.Element.

name = ET.SubElement(person, 'Name')

    Adds a child element called <Name> inside the <Person> element.

        Now your XML looks like this in memory:

            xml

                <Person>
                    <Name></Name>
                </Person>
                
name.text = 'Alice'

    Sets the text content of the <Name> element to "Alice".

        The <Name> tag becomes:

            xml

                <Name>Alice</Name>
                
        So far, in memory:

            xml

                <Person>
                    <Name>Alice</Name>
                </Person>
                
age = ET.SubElement(person, 'Age')

    Adds another child element <Age> under <Person>.

        Your tree now contains both children:

            xml

                <Person>
                    <Name>Alice</Name>
                    <Age></Age>
                </Person>

age.text = '30'

    Sets the text content of the <Age> element to "30".

        So now you have:

            xml

                <Age>30</Age>
                
        Now your complete XML tree in memory looks like this:

            xml

                <Person>
                    <Name>Alice</Name>
                    <Age>30</Age>
                </Person>

tree = ET.ElementTree(person)

    Wraps the root element (person) in an ElementTree object.

    This represents the entire XML document, and enables methods like write(), find(), parse(), etc.

tree.write('person.xml')

    Writes the entire XML tree to a file called person.xml.

    By default:

        The output is UTF-8 encoded

        No pretty printing (no indentation or newlines unless you format it yourself)
        
        Resulting file: 
        
            person.xml

                xml

                    <Person><Name>Alice</Name><Age>30</Age></Person>

'''