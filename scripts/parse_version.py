import sys
import xml.etree.ElementTree as ET


def main():
    xml_data = sys.stdin.read()
    root = ET.fromstring(xml_data)

    # Navigate to the 'release' element under 'metadata/versioning'
    release = root.find(".//versioning/release")

    if release is None:
        raise Exception("Unable to find version")

    print(release.text)


if __name__ == "__main__":
    main()
