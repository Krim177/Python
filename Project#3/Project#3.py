# You should start by copying your note_to_int and NOTES code here.

from musicbox import MusicBox
my_music = MusicBox(0)

# Your code goes here

NOTES = [("C", 60), ("D", 62), ("E", 64), ("F", 65), ("G", 67), ("A", 69), ("B", 71)]

major_scale_intervals = [2, 2, 1, 2, 2, 2, 1] 

def note_to_int(note):
    num_octaves = note.rfind("^") + 1
    letter = note[num_octaves]
    letter_value = 0
    for n in range(len(NOTES)):
        if letter == NOTES[n][0]:
            letter_value = NOTES[n][1]
    adjustment = note[len(note)-1]
    if adjustment == "#":
        return (12 * num_octaves) + letter_value + 1
    elif adjustment == 'b':
        return (12 * num_octaves) + letter_value - 1 
    else:
        return (12 * num_octaves) + letter_value
 


def play_song(song_file_name):
    for line in open(song_file_name):
        space = 0
        for c in line:
            if c == " ":
                space +=1
        location_space = line.rfind(" ")
        num = line[location_space + 1:]
        note = line[:location_space]
        split_note = note.split(" ")
        if split_note[0] == "//":
            continue
        elif line[0] == "I":
            my_music.set_instrument(int(num))
        elif space == 1:
            if line[0] == "P":
                my_music.pause(int(num))
            else:
                my_music.play_note(note_to_int(note),int(num))
        elif space >=2:
            chord = []
            for e in split_note:
                new_note = note_to_int(e)
                chord.append(new_note)
            my_music.play_chord(chord, int(num))
        





if __name__ == "__main__":
    file = input("Please enter a file name: \n")
    play_song(file)

