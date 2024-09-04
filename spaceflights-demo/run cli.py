import subprocess

def execute(command):
    try:
        # Execute the command
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        
        # Print the output
        print("Command output:")
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        # If the command fails, print the error
        print("An error occurred while running the command:")
        print(e.stderr)


# Run the Kedro project with the databricks environment
execute('pip install -r "requirements.txt"')
execute('kedro run --env=databricks')