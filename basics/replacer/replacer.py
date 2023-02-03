
#print("Hellooo")


def replace_content(text, old=" ", new="🐹"):
    modified_content = text.replace(old, new)
    return modified_content


if __name__ == "__main__":
    print("Single Mode")
    file_handle = open("gpl.txt", "r")
    file_content = file_handle.read()
    file_handle.close()

    #old_content = " "
    #new_content = "🐹"
    #modified_content = file_content.replace(old_content, new_content)
    #replace_content(file_content)

    file_handle = open("replaced.txt", "w")
    file_handle.write(replace_content(file_content, "t"))
    file_handle.close()
