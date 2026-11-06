import os

from acdh_tei_pyutils.tei import TeiReader

index_files = ["listperson.xml", "listplace.xml"]

for x in index_files:
    file = os.path.join("data", "indices", x)
    doc = TeiReader(file)
    for bad in doc.any_xpath("//tei:person[not(.//tei:note[@type='mentions'])]"):
        bad.getparent().remove(bad)
    for bad in doc.any_xpath("//tei:place[not(.//tei:note[@type='mentions'])]"):
        bad.getparent().remove(bad)
    doc.tree_to_file(file)
