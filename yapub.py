import yaml
document = """
  a: 1
  b:
    c: 3
    d: 4
"""

# print yaml.dump(yaml.load(document))


document = """
    title: My awesome paper
    authors:
        - name:  AAA
          organization: ORAAA
          email: a@a.com
          id: a_id
    
        - name:  BBB
          organization: ORBBB
          email: b@b.com
          id: b_id
      
    sections: 
        - section: first section
          subsections:        
            - top approach: |
                This is my top approach
            - bottom approach: |
                This is my button approach
        
        - section: fruits section
          subsections:        
            - apple 
            - orange

        - section: free section
          body: |
            This is some kind of free section
          subsections: 
            - VU: |
                This university name is VU
            - UVa: |
                This university name is UVa

        
"""
print yaml.dump(yaml.load(document))

from ieee_keys import keys

y = yaml.load(document)

print("\n=================\n")
print y["title"]
for a in y["authors"]:
    print(a["name"])
    print(a["email"])


def html_from_yaml_key(yaml_dict, key_ref, proc_order):
    """
    :param yaml_dict: parsed yaml document
    :param key_ref: key laws/structure to transform the yaml to html
    :param proc_order: the process order
    :return: html
    """
    html_header_start = """
    <!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>IEEE Conference Proceedings Format</title>
    <link rel="stylesheet" href="css/pubcss-ieee.css">
    <style>


    </style>
  </head>
  <body>
    """
    html_header_end = """
          </body>
</html>
    """
    html_content = ""
    for o in proc_order:
        # if key_ref[o]["cardi"] == "single":
        #     html_content += key_ref[o]["pre"] + yaml_dict[o] + key_ref[o]["post"]
        print "o: "+str(o)
        p = key_ref[o]["parse"](v=yaml_dict[o])
        html_content += p
    return html_header_start + html_content + html_header_end


print ("\n>>>>>>>>>>>>>>>\n")

# print(html_from_yaml_key(y, keys, ["title", "authors", "sections"]))
#print(html_from_yaml_key(y, keys, ["title", "authors"]))
html_from_yaml_key(y, keys, ["title", "authors", "sections"])

