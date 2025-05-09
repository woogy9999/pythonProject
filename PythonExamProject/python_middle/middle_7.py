import xml.etree.ElementTree as ET
tree=ET.parse("sawon.xml")
"""
    xml = 문서형 데이터베이스
    
    <list name="강호동">
        <sabun>3</sabun>
        <dept>씨름부</dept>
        <job>부장</job>
        <etc year="1995" pay="20000"/>
    </list>
"""
root=tree.getroot()
print(root.tag)
for child in root:
    print(child.tag,child.attrib)


for etc in root.iter('etc'):
    print(etc.attrib)

for list in root.findall('list'):
    sabun=list.find('sabun').text
    dept=list.find('dept').text
    job=list.find('job').text
    print(sabun,dept,job)

for job in root.iter('job'):
    print(job.text)

    
