from note import Note
from scale import Scale
import json

def main():
	scales_json = json.load(open('scales.json', 'r'))
	scales = []
	for scale in scales_json:
		scales.append(Scale(scale['name'], scale['semitones']))
	scales = sorted(scales, key = lambda x: x.name)
	print('1. Build scale from root note')
	print('2. Build all scales from root note')
	print('3. Find scale(s) from notes')
	print('4. Find scale(s) from semitones')
	opt = None
	while opt not in range(1, 5):
		opt = int(input('> '))

	if opt == 1:
		print('\n\n')
		print('Please select a scale:')
		padding = len(scales)
		for i in range(len(scales)):
			print(str(i + 1).rjust(padding) + '. ' + scales[i].name)
		opt = None
		while opt not in range(1, len(scales) + 1):
			opt = int(input('> '))
		root_note = Note(input('Note: '))
		sharps = scales[opt - 1].from_root(root_note, notation = '#')
		flats = scales[opt - 1].from_root(root_note, notation = 'b')
		print('\n\n\n' + scales[opt - 1].name + ' scale starting from ' + str(root_note) + ':')
		print('Sharp notation:', sharps)
		print('Flat notation: ', flats)
	elif opt == 2:
		root_note = Note(input('Note: '))
		print('\n')
		for scale in scales:
			sharps = scale.from_root(root_note, notation = '#')
			flats = scale.from_root(root_note, notation = 'b')
			print('\n' + scale.name + ' scale starting from ' + str(root_note) + ':')
			print('Sharp notation:', sharps)
			print('Flat notation: ', flats)
	elif opt == 3:
		notes = input('Notes (separated by spaces): ').split(' ')
		notes = [Note(note) for note in notes]
		possible_scales = []
		for scale in scales:
			sharps = scale.from_root(notes[0], notation = '#')
			flats = scale.from_root(notes[0], notation = 'b')
			all_notes = list(set(sharps + flats))
			if all([note in all_notes for note in notes]):
				possible_scales.append(scale.name)
		print('\n\nI have found the following scale(s):')
		print('\n'.join(['- ' + scale for scale in possible_scales]))
	elif opt == 4:
		possible_scales = []
		semitones = [int(x) for x in input('Semitones (separated by spaces): ').split(' ')]
		for scale in scales:
			if semitones == scale.semitones:
				possible_scales.append(scale.name)
		print('\n\nI have found the following scale(s):')
		print('\n'.join(['- ' + scale for scale in possible_scales]))

if __name__ == '__main__':
	main()