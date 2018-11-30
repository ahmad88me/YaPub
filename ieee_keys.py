# keys = {
#     "title": [
#         """  <head>
#     <meta charset="utf-8" />
#     <title>""",
#         """"</title>
#         <link rel="stylesheet" href="css/pubcss-ieee.css">
#       </head>"""
#     ],
#     "section": [
#         "<h1>",
#         "</h1>"
#     ],
#     "subsec": [
#         "<h2>",
#         "</h2>"
#     ],
#     "enumerate": [
#         "<ol>",
#         "</ol>"
#     ],
#     "itemize": [
#         "<ul>",
#         "</ul>"
#     ]
#
#
# }

# keys = {
#     "title": {
#         "pre": """  <head>
#     <meta charset="utf-8" />
#     <title>""",
#         "post":  """"</title>
#         <link rel="stylesheet" href="css/pubcss-ieee.css">
#       </head>""",
#         "cardi": "single",
#     },
#     "section": {
#         "pre": "<h1>",
#         "post": "</h1>",
#         "cardi": "multi",
#         "child-enc": {
#             "pre": "<section>",
#             "post": "</section>"
#         }
#     },
#     "subsec": {
#         "pre": "<h2>",
#         "post": "</h2>",
#         "cardi": "multi",
#     },
# }


def parser_title(v, k="title"):
    return keys[k]["pre"] + v + keys[k]["post"]


def parser_sections(v, k="sections"):
    return keys[k]["pre"] + str(v) + keys[k]["post"]


def parser_authors(v, k="authors"):
    html = ""
    print("authors list: ")
    print(v)
    for a in v:
        html += parser_author(a)
    return keys[k]["pre"] + html + keys[k]["post"]


def parser_author(v, k="author"):
    a = {
        "affiliation": "",
        "organization": "",
        "country": "",
        "city": "",
        "email": ""
    }
    print("author value:")
    print(v)
    v["xyz"] = "something new"
    print(v)
    for ak in a.keys():
        if ak not in v:
            v[ak] = ""
    html = """
        <div>%s</div>
        <div>%s</div>
        <div>%s</div>
        <div>%s</div>
    """ % (v["affiliation"], v["organization"], v["city"]+", "+v["country"], v["email"])
    return keys[k]["pre"]+html+keys[k]["post"]


keys = {
    "title": {
        "pre": """  <head>
    <meta charset="utf-8" />
    <title>""",
        "post":  """"</title>
        <link rel="stylesheet" href="css/pubcss-ieee.css">
      </head>""",
        "cardi": "single",
        "parse": parser_title,
    },
    "authors": {
        "pre": """<div class="authors col-2">\n""",
        "post": """</div>""",
        "parse": parser_authors,
    },
    "author": {
        "pre": """<div class="author">\n""",
        "post": "</div>",
        "parse": parser_author,
    },
    "sections": {
        "pre": "",
        "post": "",
        "parse": parser_sections,
    },
    "section": {
        "pre": "<h1>",
        "post": "</h1>",
        "cardi": "multi",
        # "parse": parser_section,
        # "child": {
        #     "pre": "<section>",
        #     "post": "</section>"
        # }
    },
    "subsec": {
        "pre": "<h2>",
        "post": "</h2>",
        "cardi": "multi",
    },
}

