import os
import json
from pathlib import Path

class CodingAgent:
    def __init__(self):
        self.config = self.load_config()
        self.projects = self.config['projects']

    def load_config(self):
        with open(Path(__file__).parent / 'config.json') as f:
            return json.load(f)

    def analyze_directory(self, project_name, dir_type='development'):
        project = self.projects.get(project_name)
        if not project:
            return None

        path = Path(project[f'{dir_type}_path'])
        analysis = {
            'files': [],
            'directories': [],
            'last_modified': {}
        }

        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = Path(root) / file
                analysis['files'].append(str(file_path))
                analysis['last_modified'][str(file_path)] = file_path.stat().st_mtime

            for dir in dirs:
                analysis['directories'].append(str(Path(root) / dir))

        return analysis

    def implement_changes(self, project_name, changes):
        # Implement code changes here
        pass