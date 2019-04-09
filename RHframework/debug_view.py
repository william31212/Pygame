from imgui_pygame_intergation import PygameRenderer
import imgui

class dbg_view:
	def __init__(self, size):
		io = imgui.get_io()
		io.fonts.add_font_default()
		io.display_size = size

		self.renderer = PygameRenderer()

	def update(self):
		imgui.new_frame()

	def render(self):
		imgui.render()

	def handle_event(self, e):
		self.renderer.process_event(e)

def dbprint(s):
	dbg_print.get_dbg_print().add_str(s)

class dbg_print:
	instance = None
	line_limit = 10

	@staticmethod
	def get_dbg_print():
		if not dbg_print.instance:
			dbg_print.instance = dbg_print()
		return dbg_print.instance

	def __init__(self):
		assert dbg_print.instance == None
		self.str_list = []

	def add_str(self, s):
		self.str_list.append(s)

	def draw(self):
		imgui.begin("log_window", flags=imgui.WINDOW_NO_RESIZE)
		imgui.begin_child("log", 200, 300, border=True)
		for i in range(len(self.str_list)-1, -1, -1):
			imgui.text(self.str_list[i])
		imgui.end_child()
		if imgui.button('Clear'):
			self.str_list = []
		imgui.end()