from keywordlookup.keyword import KeywordLookup

if __name__ == "__main__":
    keyword = KeywordLookup("beam")
    definitions = keyword.get_definitions()

    print("Found {} definitions:".format(len(definitions)))

    for definition in definitions:
        print(definition + "\n")
