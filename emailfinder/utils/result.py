class Result:
    """Result class

    Functions:
       get_metadata: Return all metadata collected.
       get_authors: Returns all authors found in a list.
       get_software: Returns all software found in a list.
    """
    def __init__(self, metadata):
        self._metadata = metadata
        self._authors, self._software = self._configure_data(metadata)
    
    def get_metadata(self):
        return self._metadata
    
    def get_authors(self):
        return self._authors
    
    def get_software(self):
        return self._software

    def _configure_data(self, metadata):
        authors = []
        software = []
        for key, value in metadata.items():
            for v in value["metadata"]:
                if v and v == "Author" and value["metadata"][v] not in authors:
                    authors.append(value["metadata"][v])
                elif v and (v == "Producer" or  v == "Creator") and value["metadata"][v] not in software:
                    software.append(value["metadata"][v])
        return authors, software