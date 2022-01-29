from flask import Flask
from flask import request
from flask import Response
from ldap3 import Server, Connection, SUBTREE
from xml.etree.ElementTree import Element, SubElement, tostring

attr = ['cn', 'company', 'givenName', 'telephoneNumber']
AD_SERVER = 'ldap.srv.ip.addr'
AD_USER = 'DOMAIN\username'
AD_PASSWORD = 'password'
AD_SEARCH_TREE = 'DC=SEARCHPATH,DC=COM'
app = Flask(__name__)


@app.route("/search", methods=['GET', 'POST'])
def login():
    department = request.args.get('department')
    server = Server(AD_SERVER)
    conn = Connection(server, user=AD_USER, password=AD_PASSWORD)
    conn.bind()
    conn.search(AD_SEARCH_TREE, '(objectCategory=person)', SUBTREE, attributes=attr)

    root = Element('CiscoIPPhoneDirectory')
    child = SubElement(root, "Prompt")
    child.text = "Records 1 to 4 of 4"
    i = 0
    while i < len(conn.entries):
        if conn.entries[i][attr[1]] == department:
            child1 = SubElement(root, "DirectoryEntry")
            name = SubElement(child1, "Name")
            name.text = str(getattr(conn.entries[i], "givenName"))
            tel = SubElement(child1, "Telephone")
            tel.text = str(getattr(conn.entries[i], "telephoneNumber"))
        i += 1

    return Response(tostring(root), mimetype='text/xml')
