import re
from datetime import datetime, timedelta

# location of the pipeline
logstash_conf_file = "/etc/logstash/conf.d/pipeline.conf"

def update_logstash_conf(file_path):
    """
    Update the pDATEFROM and pDATETO values ​​in the Logstash configuration file
    to cover a 5 minute interval based on the current time.

    :param file_path:
    """
    # Calculate new dates (5 minute dynamic range)
    now = datetime.now()
    pDATEFROM = (now - timedelta(minutes=5)).strftime("%Y-%m-%dT%H:%M:%S")
    pDATETO = now.strftime("%Y-%m-%dT%H:%M:%S")

    # Read the contents of the configuration file
    with open(file_path, "r") as file:
        config_content = file.read()

    # Search and replace the values ​​of pDATEFROM and pDATETO
    config_content = re.sub(
        r"(?<=<tns:pDATEFROM>)(.*?)(?=</tns:pDATEFROM>)",
        pDATEFROM,
        config_content,
    )
    config_content = re.sub(
        r"(?<=<tns:pDATETO>)(.*?)(?=</tns:pDATETO>)",
        pDATETO,
        config_content,
    )

    # Write the new contents to the configuration file
    with open(file_path, "w") as file:
        file.write(config_content)

    print(f"Configuration updated successfully in {file_path}:")
    print(f"  pDATEFROM: {pDATEFROM}")
    print(f"  pDATETO: {pDATETO}")

# Run script
if __name__ == "__main__":
    update_logstash_conf(logstash_conf_file)
