import os
import glob

def collect_code_files(directory, extensions=['.py', '.js', '.java', '.tsx', '.jsx', '.css', '.html']):
    code_contents = {}
    # Skip common directories that aren't needed for analysis
    skip_dirs = ['node_modules', 'venv', '__pycache__', '.git', 'build', 'dist']
    
    for ext in extensions:
        for root, dirs, files in os.walk(directory):
            # Skip unwanted directories
            dirs[:] = [d for d in dirs if d not in skip_dirs]
            
            for file in files:
                if file.endswith(ext):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            code_contents[file_path] = f.read()
                    except Exception as e:
                        print(f"Error reading {file_path}: {e}")
    return code_contents

def chunk_content(content, max_chunk_size=4000):
    """Break content into manageable chunks"""
    return [content[i:i + max_chunk_size] for i in range(0, len(content), max_chunk_size)]

def analyze_project(project_path):
    # Collect all code files
    repo_files = collect_code_files(project_path)
    
    # Print project structure
    print("Project Structure:")
    print("=================")
    for file_path in repo_files.keys():
        print(file_path)
    print("\n")
    
    # Analyze each file
    for file_path, content in repo_files.items():
        print(f"\nFile: {file_path}")
        print("=" * (len(file_path) + 6))
        
        chunks = chunk_content(content)
        for i, chunk in enumerate(chunks):
            print(f"\nChunk {i+1}/{len(chunks)}:")
            print("```")
            print(chunk)
            print("```\n")
        print("-" * 80)

if __name__ == "__main__":
    # Replace with your project path
    project_path = "../InstAanlyst-AI/InstAnalyst-AI"
    analyze_project(project_path)