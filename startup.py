import os
import sys

ui_path = "/opt/render/project/src/.venv/lib/python3.14/site-packages/autogenstudio/web/ui"

for root, dirs, files in os.walk(ui_path):
    for file in files:
        if file.endswith('.js') or file.endswith('.html') or file.endswith('.json'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                if 'AutoGen Studio' in content:
                    content = content.replace('AutoGen Studio', 'AgentPilot Studio')
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"UPDATED: {file}")
            except Exception as e:
                print(f"SKIPPED: {file} - {e}")

print("Branding complete! Starting server...")
os.execv(sys.executable, [sys.executable, '-m', 'autogenstudio.cli', 'ui', '--port', '8080', '--host', '0.0.0.0'])