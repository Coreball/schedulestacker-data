
two_word_rooms = {"GYM", "Rm", "R", "Theatre"}


def make_csv():
    read_name = input("Read from: ")
    write_name = input("Write to: ")
    with open(read_name, encoding="utf8") as r, open(write_name, 'w') as w:
        lines = r.readlines()
        for line in lines:
            if line != '\n' and line[0] != '#':
                print(line)
                w.write(line[0] + ',')  # Type
                w.write(line[2:(line.rindex(' ', 0, line.index('(A-E)')))] + ',')  # Course Name
                w.write(line[(line.rindex(' ', 0, line.index('(A-E)')) + 1):line.index('(A-E)')] + ',')  # Period
                chopped = line[(line.index('(A-E)') + 6):]
                w.write(chopped[:chopped.index(' ')] + ',')  # Semester
                w.write(chopped[(chopped.index(' ') + 1):chopped.index(',')] + ',')  # Last Name
                m_c = chopped[(chopped.index(',') + 2):].split()
                first_name = str()
                if m_c[-1] in two_word_rooms:
                    for word in m_c[:-2]:
                        first_name += word + ' '  # First Name
                    w.write(first_name.strip())
                    w.write(',')
                    for room in m_c[-2:]:
                        w.write(room + ' ')  # Room
                else:
                    for word in m_c[:-1]:
                        first_name += word + ' '  # First Name
                    w.write(first_name.strip())
                    w.write(',')
                    w.write(m_c[-1])
                w.write('\n')
                # Note that First Name and Room may be off because the formatting of the original is ambiguous.
                # You'll need to fix the S GYM and Dance Rm things manually.
                # I fixed that, now make sure to FIX HYPHENS and FIX BOM UTF8


if __name__ == '__main__':
    make_csv()
