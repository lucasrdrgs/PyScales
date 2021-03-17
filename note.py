NOTES_SHARP = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
NOTES_FLAT  = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']

class Note(object):
	def __init__(self, note, notation = None):
		if len(note) < 1 or len(note) > 2 \
		or note.lower() not in list(map(lambda x: x.lower(), (NOTES_SHARP + NOTES_FLAT))):
			raise Exception('Invalid note.')
		note = note[0].upper() + note[1:].lower()
		original_notation = notation
		if len(note.lower()) == 2:
			if note.lower()[-1] == 'b':
				original_notation = 'b'
			elif note.lower()[-1] == '#':
				original_notation = '#'
			else:
				raise Exception('Invalid note.')
		self.notation = notation if notation is not None else original_notation
		self.__index = (NOTES_SHARP.index(note) if original_notation == '#' else NOTES_FLAT.index(note))
	def to_flat(self):
		self.notation = 'b'
		return self
	def to_sharp(self):
		self.notation = '#'
		return self

	@property
	def note(self):
		return self.__repr__()

	def __add__(self, o):
		if not isinstance(o, int):
			raise Exception('Cannot sum <Note> and', type(o))
		new_index = (self.__index + o) % len(NOTES_SHARP)
		return Note(NOTES_SHARP[new_index] if self.notation == '#' else NOTES_FLAT[new_index], self.notation)
	def __sub__(self, o):
		if not isinstance(o, int):
			raise Exception('Cannot subtract <Note> and', type(o))
		new_index = self.__index - o
		return Note(NOTES_SHARP[new_index] if self.notation == '#' else NOTES_FLAT[new_index], self.notation)

	def __repr__(self):
		return NOTES_SHARP[self.__index] if self.notation == '#' else NOTES_FLAT[self.__index]

	def __str__(self):
		return self.__repr__()
	
	def __eq__(self, o):
		return self.__repr__() == o.__repr__()
	
	def __hash__(self):
		return hash(self.__index)