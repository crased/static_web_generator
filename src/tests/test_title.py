from get_title import extract_title
def main():
    md1 = "# Hello"
    print(extract_title(md1))  # expect: Hello

    md2 = "Intro\n# Tolkien Fan Club\nMore text"
    print(extract_title(md2))  # expect: Tolkien Fan Club

    md3 = "## Not a main title"
    # this should raise an exception
    try:
        print(extract_title(md3))
    except Exception as e:
        print("Got exception:", e)

if __name__ == "__main__":
   main()