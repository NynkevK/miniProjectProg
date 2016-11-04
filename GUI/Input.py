# Geschreven door Mark


class Input:


    def get(self, entries):
        """krijgt input en verschoont het veld"""
        items = []

        for entry in entries:
            text = entry.get()
            entry.delete(0, "end")
            items.append(text)
        return items
