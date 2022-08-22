"""
Class that manages files
"""

import json


class FileManager:
    JSON_FILE: str = "files/jobs.json"

    def save_as_json_file(self, data: list) -> None:
        """
        Saves job offers to a json file
        :param data: list of job offers
        """
        with open(self.JSON_FILE, 'w', encoding='utf8') as file:
            json.dump([ob.__dict__ for ob in data], file, ensure_ascii=False, indent=4)
