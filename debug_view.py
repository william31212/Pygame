from imgui_pygame_intergation import PygameRenderer
import imgui

class dbg_view:
	def __init__(self, size):
		io = imgui.get_io()
	    io.fonts.add_font_default()
	    io.display_size = size

	    self.renderer = PygameRenderer()

	def new_frame(self):
		imgui.new_frame()

	def render(self):
		imgui.render()

	def handle_event(self, e):
		self.render.process_event(e)