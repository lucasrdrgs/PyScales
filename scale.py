from note import Note
class Scale(object):
	def __init__(self, name, semitones):
		self.name = name
		self.semitones = semitones
	def from_root(self, root, notation = None):
		root_note = None
		if isinstance(root, str):
			root_note = Note(root, notation)
		else:
			root_note = root
			if notation == '#': root_note.to_sharp()
			elif notation == 'b': root_note.to_flat()
		scale = [root_note]
		for i, semitone in enumerate(self.semitones):
			scale.append(scale[i] + semitone)
		return scale