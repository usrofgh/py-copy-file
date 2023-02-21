def copy_file(command: str) -> None:
    cp_command, old_file, new_file = command.split()
    if cp_command != "cp" or old_file == new_file:
        raise ValueError("Write a command correctly. "
                         "Example: cp file1.txt file2.txt")

    with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
        file_out.write(file_in.read())
